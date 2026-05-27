CREATE table if not exists employees(
    id INT PRIMARY KEY,
    name VARCHAR(50),
    age INT,
    department VARCHAR(50),
    salary INT
);
insert into employees if not EXISTS (id,name,age,department,salary) VALUES
(1,'Alice',30,'HR',60000),
(2,'Bob',24,'IT',75000),
(3,'Charlie',35,'IT',90000),
(4,'David',28,'Sales',65000),
(5,'Eve',30,'HR',62000);
select * from employees;
