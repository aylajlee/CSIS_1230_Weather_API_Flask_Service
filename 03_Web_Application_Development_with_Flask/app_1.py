# Import the Flask class
from flask import Flask, abort, render_template, redirect, request, url_for

from task_manager import TaskManager

# Create an instance of the Flask class. 
# __name__ helps Flask find template and static files.
app = Flask(__name__)

task_manager = TaskManager()
# Define a route with the @app.route decorator.
# This tells Flask what URL should trigger our function.
@app.route('/')
def home():

    return '<h1>Hi this is my first Flask app!</h1>'

@app.route('/tasks', methods=['GET', 'POST'])
def handle_tasks():
    if request.method == 'POST':
        # CREATE operation
        title = request.form.get('title')
        description = request.form.get('description', '')
        
        # Validation
        errors = []
        if not title:
            errors.append("Title is required")
        if len(title) > 100:
            errors.append("Title must be less than 100 characters")
        
        if errors:
            return render_template('tasks_form.html', errors=errors)
        
        # Business logic
        new_task = task_manager.create({
            'title': title,
            'description': description
        })
        
        # Post-create pattern (redirect to avoid duplicate submissions)
        return redirect(url_for('show_task', task_id=new_task['id']))
    
    else:
        # READ operation (list all)
        tasks = task_manager.read()
        return render_template('tasks/index.html', tasks=tasks)
    


@app.route('/tasks')
def tasks():
    tasks = task_manager.read()
    print(tasks)
    return render_template('tasks/index.html', tasks=tasks)

# Read One (Show)
@app.route('/tasks/<int:task_id>')
def show_task(task_id):
    task = task_manager.read(task_id)
    if not task:
        abort(404)  # Resource not found
    return render_template('tasks/show.html', task=task)

#### [월요일 수업] March 2nd 2026 
@app.route('/dashboard')
def dashboard(task_id):
    task = task_manager.read(task_id)
    if not task:
        abort(404)
        
@app.route('/tasks/<int:task_id>/edit', methods=['GET', 'POST'])
def edit_task(task_id):
    task = task_manager.read(task_id)
    if not task:
        abort(404)
    
    if request.method == 'POST':
        # UPDATE operation
        title = request.form.get('title')
        description = request.form.get('description', '')
        completed = 'completed' in request.form
        
        # Validation (reuse from create)
        errors = []
        if not title:
            errors.append("Title is required")
        
        if errors:
            return render_template('tasks/edit.html', task=task, errors=errors)
        
        # Partial update pattern
        task_manager.update(task_id, {
            'title': title,
            'description': description,
            'completed': completed
        })
        
        return redirect(url_for('show_task', task_id=task_id))
    
    else:
        # Pre-populate form with existing data
        return render_template('tasks/edit.html', task=task)
    
@app.route('/tasks/<int:task_id>/delete', methods=['POST'])
def delete_task(task_id):
    task = task_manager.read(task_id)
    if not task:
        abort(404)
    
    # DELETE operation
    task_manager.delete(task_id)
    
    # Post-delete pattern (redirect to index)
    return redirect(url_for('tasks'))



if __name__ == '__main__':
    app.run(debug=True)