use my_first_db;
select distinct department from employees ;
select name,salary*12 as annual_salary,department from employees;
-- 按薪资降序排列所有员工
select name,salary from employees order by salary desc;
-- 先按部门升序排列，在按薪资降序排列
select name,department,salary
from employees
order by department desc ,salary desc;
-- 查询前三名员工
select * from employees limit 2,2;
-- 每页显示2条记录，查询前三页
select * from employees limit 0,2;
select * from employees limit 2,2;
select * from employees limit 3,2;
-- 查询员工总数
select count(*) as total_employees
from employees
where department='IT';
-- 查询所有员工工资总和
select sum(salary) as total_salary
from employees;
-- 查询IT部的平均薪资
select avg(salary) as IT_avg_salary
from employees
where department='IT';
-- 查询最高薪资
select max(salary) as max_salary
from employees;
-- 查询年龄最小的员工‘
select min(age) as min_age
from employees;
