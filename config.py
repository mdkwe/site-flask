import os

SECRET_KEY = '#d#JCqTTW\nilK\\7m\x0bp#\tj~#H'

FB_APP_ID = 217130940993843

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')

# print(SQLALCHEMY_DATABASE_URI)