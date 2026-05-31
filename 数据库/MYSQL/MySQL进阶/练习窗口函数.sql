-- 练习窗口函数

-- 聚合函数vs 窗口函数
-- group by 本质是分组聚合，只保留分组字段和集合计算结果，原始的每一行细节被丢弃
-- 而窗口函数本质是开窗计算，计算结果作为新列附加到每一行，原始行的所有信息都保留

use student_course_system;
drop table if exists employees;
create table if not exists employees(
  id int primary key,
  name varchar(50) not null,
  department VARCHAR(50) not null,
  salary int not null
);
insert into employees values
(1,'Allen','IT',8000),
(2,'Charlie','IT',9000),
(3,'David','Marketing',7000),
(4,'Jason','Marketing',6000);

select * from employees;
-- group 合并行的过程
select id,name,salary, department,avg(salary) as avg_salary
from employees
group by department;
-- 用窗口函数保留原始行的过程
select 
  id,
  name,
  department,
  salary,
  -- 窗口函数：计算当前行所在部门的平均工资，附加为新列
  avg(salary) over (partition by department) as dept_avg_salary
  from employees;
  
-- 语法 over 定义窗口的关键字，partition可选，order by 可选，  

-- 常见的窗口函数分类

-- 排名窗口函数
-- row_number()
-- rank()
-- dense_rank()
-- ntile()
drop table if exists employees;
create table employees(
  id int primary key,
  name varchar(50) not null,
  department varchar(50) not null,
  salary int not null
);
insert into employees VALUES
(1,'Allen','IT','8000'),
(2,'Charlie','IT',9000),
(3,'David','Marketing',7000),
(4,'Jason','Marketing',6000),
(5,'Kevin','IT',8000),
(6,'James','IT',7000);
select * from employees;

-- 查询每个部门员工的工资排名
select name,department,salary,id,
ROW_NUMBER() over(partition order  by department order by salary desc) as row_num_rank,
RANK() over(partition by department order by salary desc) as ranking,
DENSE_RANK() over(partition by department order by salary desc) as dense_ranking
from employees;

-- 值窗口函数
-- lag(expression,n,default) :获取当前行向上n行的expression
-- lead(expression,n,default):获取当前行向下n行的expression值
-- first_value(expression) :获取窗口中第一行的expression值
-- last_value(expression) :获取窗口中最后一行的expression值

-- 查询每一个员工的工资，以及他所在部门工资排他前一名的员工的工资
select 
department,name,salary,lag(salary,1,0) over(partition by department order by salary desc)
from employees;

-- 聚合窗口函数
select name,salary,department,
avg(salary) over(partition by department) as dept_avg_salary
from employees;
