use student_course_system;
select * from employees;
select * from department;
-- 查询工资高于平均工资的员工信息
select a.emp_name,a.salary,b.dept_name 
from employees a
left join department b on a.dept_id=b.dept_id
where salary>(select avg(salary) from employees);

-- 查询已下单用户的详细信息
select * from orders;
select * from users;
select user_id,User_name
from users
where user_id in (select distinct user_id from orders);

-- 查询至少在一个部门中有员工的部门信息
select * from employees;
select * from department;
select dept_name
from department d
where exists(select 1 from employees e where d.dept_id=e.dept_id);

-- 查询每一个用户及其订单总数
select user_name,
(select count(*)
 from orders b 
 where a.user_id=b.user_id
)
from users a;

-- 在from子句中使用子查询
-- 创建临时表
-- 查询每个部门的平均工资，并且只显示平均工资大于6000的部门
select dept_name,avg_salary
from (
  select b.dept_name,avg(a.salary)as avg_salary
  from employees a
  inner join department b on a.dept_id = b.dept_id
  group by b.dept_name
)as avg_dep_salary
 where avg_salary>60000;
