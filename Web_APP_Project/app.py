from flask import Flask, render_template, jsonify, redirect, url_for, send_file, Response, abort, make_response
import json

app = Flask(__name__)

# 1. String response
# run my code
@app.route('/')
def home():
    return "Welcome to the home page"

# 2. HTML String response
@app.route('/html_string')
def html_string():
    return '<h1>Hi this is my first app!</h1>'

# 3. HTML template response
# 2번 3번 따로 작성해야함 함께 쓰면 못 봄!
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', user='John')

# 4. Passing python variables to your html page
@app.route('/cities')
def cities():
  cities = ["Chicago", "Austin", "New York"]
  return render_template('index.html', title="Weather Dashboard", cities=cities)

# 5. Redirect response
# 지정한 페이지로 돌아가는 것 
@app.route('/old-page')
def old_page():
    return redirect(url_for('dashboard'))

# 6. Return JSON API response
# Alice랑 Bob 화면 뜨는 거 볼 수 있음 
@app.route('/api/users')
def api_users():
    users = [{'id': 1, 'name': 'Alice'}, {'id': 2, 'name': 'Bob'}]
    return jsonify(users)

# 7. Tuple string response with status
## 다 지우고 작성하면, 여기서는 "Method not allowed"라고 뜸 
@app.route('/create', methods=['POST'])
def create():
    return "Item created", 201

# 8. Tuple JSON response with status
@app.route('/api/create', methods=['POST'])
def create_item():
    # Process data...
    
    return jsonify({'message': 'Item created', 'id': 123}), 201

# @app.errorhandler(405)
# def page_not_found(error):
#     return render_template('405.html'), 405

# 9. Passing parameters through URL routes to html
# @app.route('/user/<name>')
# def user_profile(name):
#     return render_template('profile.html', 
#                          username=name, 
#                          email=f"{name}@example.com")
@app.route('/user/<name>')
def user_profile(name):
    return render_template('profile.html', 
                         username=name, 
                         email=f"{name}@example.com")


if __name__ == '__main__':
    app.run(debug=True)
