from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv
from flask_bcrypt import Bcrypt

app = Flask(__name__)

#host=os.getenv('MYSQL_HOST1')
#user=os.getenv('MYSQL_USER')
#password=os.getenv('MYSQL_PASSWORD')


app.config['SQLALCHEMY_DATABASE_URI']=('mysql+pymysql://'+ getenv('MYSQL_USER')+':'+ getenv('MYSQL_PASSWORD') + '@' + getenv('MYSQL_HOST')+ '/' + getenv('MYSQL_DATABASE'))

app.config['SECRET_KEY'] = '552a662b772c882d1998'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)


from application import routes






