from flask_login import UserMixin
from cfg import db
class BaseModel(db.Model):
    """Base data model for all objects"""
    __abstract__ = True

    def __init__(self, *args):
        super().__init__(*args)

class User(BaseModel, UserMixin):
    def __init__(self, *args):
        super().__init__(*args)

    """model for one of your table"""
    __tablename__ = "users"
    # define your model

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False) 
    todos = db.relationship('Todo', backref='users', lazy=True)

    def __init__(self, username, password):
        self.username = username
        self.password = self.generate_pwd_hash(password)

    def generate_pwd_hash(self, password):
        return password

class Todo(BaseModel):
    def __init__(self, *args):
        super().__init__(*args)
    """model for one of your table"""
    __tablename__ = 'todos'
    # define your model

    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    content = db.Column(db.String)
    is_done = db.Column(db.SmallInteger, default=0)

    def __init__(self, user_id, content):
        self.user_id = user_id
        self.content = content
