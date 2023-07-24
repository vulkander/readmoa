import uuid,json
import metadata_parser
from app import app, db
from bson.json_util import dumps, loads
from flask import Flask, jsonify, request, session, redirect, url_for, render_template
from flask_cors import CORS,cross_origin
from flask_jwt import JWT, jwt_required, current_identity
import google.auth.transport.requests
import google.oauth2.id_token
import os, datetime
from firebase_admin import auth

from google.cloud import firestore

HTTP_REQUEST = google.auth.transport.requests.Request()
gul_ref = db.collection('gul')

def veryfyFireBaseAuth(request):
	# Verify Firebase auth.
	id_token = request.headers['Authorization'].split(' ').pop()
	claims = google.oauth2.id_token.verify_firebase_token(
		id_token, HTTP_REQUEST)
	if not claims:
		return 'Unauthorized', 401

@app.route('/', methods=['GET', 'POST'])
def index():
	user = auth.get_user('1FaoWtsHB9ZJkqq9PfB1NRvHF5P2')
	print('Successfully fetched user data: {0}'.format(user.__dict__))
	return "API SERVER"



@app.route('/parse_url', methods=['GET', 'POST'])
#@jwt_required()
def parse_url():
	target_url = request.args.get("url")
	print(target_url)
	headers = { 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
	page = metadata_parser.MetadataParser(url=request.args.get("url"),  only_parse_http_ok=False, support_malformed=True, search_head_only = False, url_headers = headers,)
	print(page.response)
	print(page.metadata)
	return page.metadata

@app.route('/writeAPI', methods=['POST'])
def writeAPI():

	#get user info
	try:
		user = auth.get_user(request.json['key'])
		print('Successfully fetched user data: {0}'.format(user.__dict__))
	except:
		return jsonify({"success": False, "message":"APIKEY 오류"}), 200




	#get page metainfo
	headers = { 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
	page = metadata_parser.MetadataParser(url=request.json["url"],  only_parse_http_ok=False, support_malformed=True, search_head_only = False, url_headers = headers,)

	new_id = str(uuid.uuid1())


	#url 중복 체크
	isExistsList=list(gul_ref.where('url', '==', request.json['url']).get())
	if(len(isExistsList) > 0):
		return jsonify({"success": False, "message":"이미 중복해서 URL이 존재합니다."}), 200

	try:
		request.json['title'] = page.metadata['og']['title']
	except:
		request.json['title'] = page.metadata['page']['title']

	try:
		request.json['domain'] = page.metadata['og']['url']
	except:
		request.json['domain'] = page.metadata['_internal']['url']
	try:
		request.json['link'] = page.metadata['page']['canonical']
	except:
		request.json['link'] = page.metadata['_internal']['url']
	try:
		request.json['description'] = page.metadata['og']['description']
	except:
		request.json['description'] = page.metadata['meta']['description']
	try:
		request.json['image'] = page.metadata['og']['image']
	except:
		request.json['image'] = page.metadata['meta']['image']
	user.__dict__['_data']['photoURL'] = user.__dict__['_data']['photoUrl']
	request.json['user']=user.__dict__['_data']

	request.json['create_time'] = datetime.datetime.now()
	request.json['id'] = new_id
	request.json['comments']=[{"comment":request.json['comment'], "create_time":datetime.datetime.now(), "user":user.__dict__['_data']}]
	gul_ref.document(new_id).set(request.json)

	return jsonify({"success": True}), 200


@app.route('/write', methods=['GET', 'POST'])
def write():
	veryfyFireBaseAuth(request)

	#url 중복 체크
	isExistsList=list(gul_ref.where('url', '==', request.json['url']).get())
	if(len(isExistsList) > 0):
		return jsonify({"success": False, "message":"이미 중복해서 URL이 존재합니다."}), 200


	new_id = str(uuid.uuid1())
	request.json['create_time'] = datetime.datetime.now()
	request.json['id'] = new_id
	request.json['comments']=[{"comment":request.json['comment'], "create_time":datetime.datetime.now(), "user":request.json['user']}]
	gul_ref.document(new_id).set(request.json)


	return jsonify({"success": True}), 200


@app.route('/writeComment', methods=['GET', 'POST'])
def writeComment():
	veryfyFireBaseAuth(request)
	id = request.json['id']
	request.json['create_time'] = datetime.datetime.now()

	gul_ref.document(id).update({u'comments': firestore.ArrayUnion([request.json])})



	return jsonify({"success": True, "result":request.json}), 200


@app.route('/list', methods=['GET'])
def read():
	#infinite load
	if(request.args.get('last_id')):
		start_document = gul_ref.document(request.args.get('last_id')).get()
		guls_stream = gul_ref.order_by(u'create_time', direction=firestore.Query.DESCENDING).start_after(start_document).stream()
		guls = [doc.to_dict() for doc in guls_stream]
		return jsonify(guls), 200
	else:
		guls_stream = gul_ref.order_by(u'create_time', direction=firestore.Query.DESCENDING).limit(3).stream()
		guls = [doc.to_dict() for doc in guls_stream]
		return jsonify(guls), 200

