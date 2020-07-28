from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from flask_login import LoginManager, UserMixin, login_user
from flask_sqlalchemy import SQLAlchemy
POSTGRES = {
    'user': 'postgres',
    'pw': 'left4craft',
    'db': 'flaskdata',
    'host': 'localhost',
    'port': '5432',
}
global sqlsessionclass
global app
global db
db = SQLAlchemy()
some_engine = create_engine('postgresql://%(user)s:\
%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES)
sqlsessionclass = sessionmaker(bind=some_engine)
from app import create_app
app = create_app()
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\
%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
db.init_app(app)