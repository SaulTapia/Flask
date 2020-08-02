import unittest
from flask import request, make_response, redirect, render_template, session, url_for, flash
from flask_bootstrap import Bootstrap
from flask_login import login_required, current_user
from cfg import app, db, sqlsessionclass
from app_assets.forms import TodoForm, DeleteTodoForm, UpdateTodoForm
from app_assets.queries import get_todos, get_user
from app_assets.models import Todo

@app.cli.command()
def create_tables():
    db.create_all()

@app.cli.command()
def test():
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)


@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html', error=error)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)

@app.route('/')
def index():
    user_ip = request.remote_addr

    response = make_response(redirect('/hello'))
    session['user_ip'] = user_ip

    return response


@app.route('/hello', methods=['GET', 'POST'])
@login_required
def hello():
    user_ip = session.get('user_ip')
    username = current_user.username
    todo_form = TodoForm()
    delete_form = DeleteTodoForm()
    update_form = UpdateTodoForm()
    context = {
        'user_ip' : user_ip, 
        'todos' : get_todos(username),
        'username' : username,
        'todo_form' : todo_form,
        'delete_form' : delete_form,
        'update_form' : update_form
    }
    if todo_form.validate_on_submit():
        todo = Todo(user_id = current_user.id,
                    content = todo_form.description.data)
        sqlsession = sqlsessionclass()
        sqlsession.add(todo)
        sqlsession.commit()
        flash('Nueva tarea añadida!')

        return redirect(url_for('hello'))


    return render_template('hello.html', **context)

@app.route('/todos/delete/<todo_id>', methods=['POST'])
@login_required
def delete(todo_id):
    user_id = current_user.id
    todo = Todo.query.filter(Todo.id==todo_id).first()
    if todo.user_id == user_id:
        db.session.delete(todo)
        db.session.commit()

    return redirect(url_for('hello'))

@app.route('/todos/update/<todo_id>/', methods=['POST'])
def update(todo_id):
    user_id = current_user.id
    todo = Todo.query.filter(Todo.id==todo_id).first()
    if user_id == todo.user_id:  
        todo.is_done = (todo.is_done + 1) % 2
        db.session.commit()

    return redirect(url_for('hello'))

if __name__ == "__main__":
    app.run(debug=False)
