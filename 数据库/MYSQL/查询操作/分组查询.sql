-- 分组查询
-- group by 字句
-- 使用group by 字句时，select 列表中的列（除了聚合函数）必须出现在group by 子句中
-- 查询每个部门的员工数量
select department,count(*) as num_employees
from employees group by department;

-- 查询每个部门平均薪资
select department, avg(salary) 
from employees
group by department;

-- having 语句，对分组后的结果进行过滤
-- having 在数据分组后进行过滤，where在数据分组前进行过滤
-- 因此having语句中可以包含聚合函数，而where子句中不能

-- 查询员工数量大于1的部门及其员工数量
select department,count(*)
from employees
group by department
having count(*)>1;

-- 查询平均薪资高于70000的部门及其平均薪资

select department,avg(salary) 
from employees
group by department
having avg(salary)>70000;


-- where 和having 的区别
-- 查询IT部门中，平均薪资高于80000的员工的平均薪资
select department,name,avg(salary) 
from employees
where department='IT'
group by department
having avg(salary)>80000;
