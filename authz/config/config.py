from os import environ

class Config:

	##########   Global Configuration   ##########
	ENV = environ.get("SKOB_AUTHZ_ENV", "production")

	DEBUG = int(environ.get("SKOB_AUTHZ_DEBUG", "0"))

	TESTING = int(environ.get("SKOB_AUTHZ_TESTING", "0"))
 
	SECRET = environ.get("SKOB_AUTHZ_SECRET", "VERY-HARD-SECURE-SECRET-CODE")
 
	JWT_ALGO = environ.get("SKOB_AUTHZ_JWT_ALGO", "HS512")
 
	JWT_TOKEN_LIFETIME = int(environ.get("SKOB_AUTHZ_LWT_TOKEN_LIFETIME", "86400"))

	##########  database Configuration  ##########

	SQLALCHEMY_DATABASE_URI = environ.get("SKOB_AUTHZ_DATABASE_URI", None )    #"mysql+pymysql://authzuser:authzpass@127.0.0.1:3306/authz"     localhost

	SQLALCHEMY_TRACK_MODIFICATIONS = TESTING

	##########    User Configuration    ##########

	USER_DEFAULT_ROLE = environ.get("SKOB_AUTHZ_USER_DEFAULT_ROLE", "member")

	USER_DEFAULT_STATUS = environ.get("SKOB_AUTHZ_USER_DEFAULT_STATUS", "inactive")
