CREATE TABLE jobs(
	id INT AUTO_INCREMENT PRIMARY KEY,
    job_name VARCHAR(100) NOT NULL UNIQUE,
    salary INT NOT NULL
);

CREATE TABLE users(
	id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    age INT NOT NULL,
    job_id INT,
    FOREIGN KEY(job_id) REFERENCES jobs(id)
);

INSERT INTO jobs(job_name, salary)
values('Student', 0);

INSERT INTO jobs(job_name, salary)
values('Teacher', 10000);

INSERT INTO jobs(job_name, salary)
values('Scientist', 15000);

INSERT INTO jobs(job_name, salary)
values('Assistant', 9000);

INSERT INTO jobs(job_name, salary)
values('Ship', 23333);

SELECT * FROM jobs;

INSERT INTO users(first_name, last_name, age, job_id)
VALUES('Jeff', 'Fu', 20, 4);

INSERT INTO users(first_name, last_name, age, job_id)
VALUES('Jack', 'Yin', 20, 4);

INSERT INTO users(first_name, last_name, age, job_id)
VALUES('Ray', 'Kurzweil', 65, 6);

INSERT INTO users(first_name, last_name, age, job_id)
VALUES('Gasai', 'Yuno', 16, 4);

INSERT INTO users(first_name, last_name, age, job_id)
VALUES('Yuki', 'Kaze', 14, 8);

SELECT * FROM users;

SELECT first_name, last_name, age, job_name, salary FROM users
JOIN jobs ON users.job_id = jobs.id;

SELECT * FROM users
WHERE first_name = 'Jeff'
UNION
SELECT * FROM users
WHERE first_name = 'Gasai';

SELECT * FROM users
WHERE id > (SELECT avg(id) FROM users);

UPDATE users NATURAL JOIN jobs
SET age = age + 1
WHERE age > 100;
