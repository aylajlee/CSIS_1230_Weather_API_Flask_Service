-- Exercise 1: Create Tables
-- Users 
DROP TABLE IF EXISTS task_categories CASCADE;
DROP TABLE IF EXISTS tasks CASCADE;
DROP TABLE IF EXISTS categories CASCADE;
DROP TABLE IF EXISTS users CASCADE;

CREATE TABLE users(
	user_id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE tasks (
    task_id SERIAL PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
	description TEXT,  
	completed BOOLEAN DEFAULT false, -- False -> false 
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	due_date  TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    user_id INTEGER REFERENCES users(user_id)
);

CREATE TABLE categories(
	category_id SERIAL PRIMARY KEY,
	name VARCHAR(50) UNIQUE NOT NULL
);

CREATE TABLE task_categories(
	-- task_id INTEGER REFERENCES tasks(task_id),
    -- category_id INTEGER REFERENCES categories(category_id)
	----- the linked category information is also automatically deleted
	task_id INTEGER REFERENCES tasks(task_id) ON DELETE CASCADE,
    category_id INTEGER REFERENCES categories(category_id) ON DELETE CASCADE
);

-- Exercise 2: Insert the tables the following values
--1 alice_dev alice@college.edu 
--2 bob_coder bob@college.edu 
--3 carol_student carol@college.edu
INSERT INTO users(username, email) VALUES
('alice_dev', 'alice@college.edu'),
('bob_coder', 'bob@college.edu'),
('carol_student', 'carol@college.edu');

--task_id title description user_id due_date completed 
INSERT INTO tasks(task_id, title, description, user_id, due_date, completed) VALUES
(1, 'Complete SQL Lab', 'Practice all CRUD operations', 1, '2024-03-15', false),
(2, 'Study For Midterm', 'Review chapters 1-8', 2, '2024-03-20', false),
(3, 'Build Flask App', 'Connect database to web application', 1, '2024-03-25', false),
(4, 'Team Meeting', 'Discuss project requirements', 3, '2024-03-12', false),
(5, 'Grocery Shopping', 'Buy milk and eggs', 2, '2024-03-10', false),
(6, 'Read Chapter 1', 'Database fundamentals', 3, NULL, true); -- '-' is error when there's no data, NULL is correct 

INSERT INTO categories(name) VALUES
-- (1, "School"), 
-- we have to user small quote ' for strings in SQL
('School'), 
('Work'),
('Personal'), 
('Urgent'),
('Project');

INSERT INTO task_categories(task_id, category_id) VALUES
(1, 1),
(1, 4),
(2, 1),
(3, 5),
(4, 3),
(5, 3);

--Exercise 2: Basic selects 
--a. Get all tasks 
--b. Get only task title and due_date 
--c. Get tasks for user_id 1 only 
--d. Retrieve all completed tasks 
--e. Retrieve all tasks completed before March 20th 
SELECT * FROM tasks;
SELECT title, due_date FROM tasks;
SELECT * FROM tasks WHERE user_id = 1; -- user1's task
-- d
SELECT * FROM tasks 
WHERE completed = true;
-- e
SELECT * FROM tasks
WHERE due_date < '2024-03-20'; --before this date

--Exercise 3: Basic updates on tasks table  
--a. Mark grocery shopping tasks as complete 
--b. Update the description where due_date is 2024-03-17 and title is ‘Complete 
--SQL Lab’. Set it to ‘SQL Practice’ 

-- a 
UPDATE tasks 
SET completed = true 
WHERE title = 'Grocery Shopping';

-- b
UPDATE tasks
SET due_date = '2024-03-17'
WHERE task_id = 1;

UPDATE tasks
SET description = 'SQL Practice'
WHERE due_date = '2024-03-17' AND title = 'Complete SQL Lab';


--Exercise 4: Deletions: 
--a. Delete the record from tasks table where the task_id = 5.
DELETE FROM tasks WHERE task_id = 5;


-- FINAL RESULTS CHECK
SELECT * FROM tasks ORDER BY task_id;