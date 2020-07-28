from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from flask_login import LoginManager, UserMixin, login_user
from flask_sqlalchemy import SQLAlchemy
global sqlsessionclass
global app
global db
db = SQLAlchemy()
some_engine = create_engine('postgres://oeuvggnnhwwple:28b51e993089eff942c53fb403a780543a8\
ef6d2887c829371c46065659a5c83@ec2-50-16-198-4.compute-1.amazonaws.com:5432/d40jvmpmbjumr')
sqlsessionclass = sessionmaker(bind=some_engine)
from app_assets import create_app
app = create_app()
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://oeuvggnnhwwple:28b51e993089eff942c53fb403a780\
543a8ef6d2887c829371c46065659a5c83@ec2-50-16-198-4.compute-1.amazonaws.com:5432/d40jvmpmbjumr'

db.init_app(app)