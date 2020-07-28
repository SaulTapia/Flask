from .models import User, Todo
def get_todos(username):
    user = User.query.filter(User.username==username).first()
    if user:
        user_id = user.id
        todolist = Todo.query.filter(Todo.user_id==user_id).join(User)
        return todolist
    else:
        return []

def get_user(username):
    user = User.query.filter(User.username==username).first()
    return user
