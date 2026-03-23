-- Exercise 1: Create Tables
-- Users 

CREATE TABLE  users(
	user_id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT current_time
);

CREATE TABLE tasks (
    task_id SERIAL PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
	desription TEXT,  
	completed BOOLEAN DEFAULT False,
	created_at TIMESTAMP DEFAULT current_time,
	due_date DATE, -- DEFAULT due_date, 
    user_id INTEGER 
);

CREATE TABLE categories(
	category_id SERIAL PRIMARY KEY,
	name VARCHAR(50) UNIQUE NOT NULL
);

CREATE TABLE task_categories(
	task_id INTEGER REFERENCES users(user_id),
	category_id INTEGER REFERENCES users(user_id)
);

-- Exercise 2: Insert the tables the following values
--1 alice_dev alice@college.edu 
--2 bob_coder bob@college.edu 
--3 carol_student carol@college.edu
INSERT INTO users(user_id, username, email) VALUES
(1, 'alice_dev', 'alice@college.edu'),
(2, 'bob_coder', 'bob@college.edu' ),
(3, 'carol_student', 'carol@college.edu');

--task_id title description user_id due_date completed 
INSERT INTO tasks(task_id, title, description, user_id, due_date, completed) VALUES
(1, 'Complete SQL Lab', 'Practice all CRUD operations', 1, '2024-03-15', false),
(2, 'Study For Midterm', 'Review chapters 1-8', 2, '2024-03-20', false),
(3, 'Build Flask App', 'Connect database to web application', 1, '2024-03-25', false),
(4, 'Team Meeting Discuss project requirements', 3, '2024-03-12', false),
(5, 'Grocery Shopping', 'Buy milk and eggs', 2, '2024-03-10', false),
(6, 'Read Chapter 1', 'Database fundamentals', 3, '-', true); 

INSERT INTO categories(category_id, name) VALUES
(1, "School"), 
(2, "Work"),
(3, "Personal"), 
(4, "Urgent"),
(5, "Project");

INSERT INTO task_categories(task_id, category_id) VALUES
(1, 1),
(1 , 4),
(2 , 1),
(3 , 5),
(4 , 3),
(5 , 3);

--Exercise 2: Basic selects 
--a. Get all tasks 
--b. Get only task title and due_date 
--c. Get tasks for user_id 1 only 
--d. Retrieve all completed tasks 
--e. Retrieve all tasks completed before March 20th 
SELECT title, description FROM tasks WHERE completed = true;
SELECT title, due_date FROM tasks
WHERE due_date BETWEEN '2024-03-01' AND '2024-03-20';
SELECT * FROM tasks WHERE user_id = 1;

--Exercise 3: Basic updates on tasks table  
--a. Mark grocery shopping tasks as complete 
--b. Update the description where due_date is 2024-03-17 and title is ‘Complete 
--SQL Lab’. Set it to ‘SQL Practice’ 
--UPDATE tasks
--SET completed = true
-- grocery_shopping 5
--WHERE task_id = 5; 

UPDATE tasks 
SET title = 'SQL Practice',
	due_date = '2024-03-17',
	title = 'Complete SQL Lab'
WHERE task_id = 5;


--Exercise 4: Basic deletions: 
--a. Delete the record from tasks table where the task_id = 5.
DELETE FROM tasks WHERE task_id = 5;

