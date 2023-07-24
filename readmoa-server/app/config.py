import os

basedir = os.path.abspath(os.path.dirname(__file__))

class DevelopmentConfig():
	# uncomment the line below to use postgres
	# SQLALCHEMY_DATABASE_URI = postgres_local_base
	DEBUG = True

	SECRET_KEY = "test1234"

	NAVER_CLIENT_ID = '7xDOu3PwGzHFWLOkO6u_'
	NAVER_CLIENT_SECRET = 'Ft8L2TYaZG'
	NAVER_CALLBACK = 'http://127.0.0.1:5000/naver_callback'




class ProductionConfig():
	DEBUG = False
	# uncomment the line below to use postgres
	# SQLALCHEMY_DATABASE_URI = postgres_local_base


config_by_name = dict(
	dev=DevelopmentConfig,
	prod=ProductionConfig
)

