from datetime import datetime


class TaskManager:
    def __init__(self):
        self.tasks = []
        self.next_id = 1
    
    def create(self, task_data):
        """Create a new task"""
        task = {
            'id': self.next_id,
            'title': task_data['title'],
            'description': task_data.get('description', ''),
            'completed': task_data.get('completed', False),
            'created_at': datetime.now()
        }
        self.tasks.append(task)
        self.next_id += 1
        return task
    
    def read(self, task_id=None):
        """Read tasks - all or specific"""
        if task_id:
            return next((t for t in self.tasks if t['id'] == task_id), None)
        return self.tasks.copy()
    
    def update(self, task_id, update_data):
        """Update an existing task"""
        task = self.read(task_id)
        if task:
            task.update(update_data)
            return task
        return None
    
    def delete(self, task_id):
        """Delete a task"""
        self.tasks = [t for t in self.tasks if t['id'] != task_id]