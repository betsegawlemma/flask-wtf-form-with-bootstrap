from flask import Flask, render_template
from forms import TaskForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '64ff70d5a501b3d6e54e626fba9722b4'

todos = []

@app.route('/todo', methods=['GET', 'POST'])
def get_todos():
    form = TaskForm()
    if form.validate_on_submit():
        todos.append({'title': form.title.data, 'due_date': form.due_date.data})
    return render_template('todo.html', form = form, todos = todos)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html', err = error)