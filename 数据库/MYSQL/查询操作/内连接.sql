use my_first_db;
show databases;
-- 练习内连接
create table employees_test(
  id INT PRIMARY KEY,
  name VARCHAR(50),
  dept_id INT
);
-- 向employees_test表插入数据
insert into employees_test(id,name,dept_id) VALUES
(1,'Alice',101),
(2,'Bob',102),
(3,'Charlie',101),
(4,'Diana',103);
-- 创建departments表
create table department (
  dept_id INT PRIMARY KEY,
  dept_name varchar(50)
);
-- 向department表中插入数据
insert into department (dept_id,dept_name) VALUES
(101,'HR'),
(102,'IT'),
(104,'Finance');
-- 内连接查询员工及其部门名称
select e.name ,d.dept_name
from employees_test as e
inner join department as d on e.dept_id=d.dept_id;

