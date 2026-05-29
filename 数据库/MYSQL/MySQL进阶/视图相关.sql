use student_course_system;
-- 视图
-- 创建视图：保存查询HR部门员工姓名和工资的SQL逻辑
create view hr_emp_salary AS
select emp_name,salary
from employees
where dept_id=101;
-- 后续查询时直接用视图名即可，和表操作一样
select * from hr_emp_salary;

-- 创建，修改，删除视图
-- 创建视图
-- or replace : 如果存在同名视图，则替换它，否则创建新视图
-- 视图的select 语句可以非常复杂，可以包含join，聚合函数，子查询
-- 创建视图 create view as select
-- 修改视图 alter view as select  
-- 删除视图 drop view if exists


-- 视图作用：
-- 简化复杂查询，实现封装
-- 数据安全性，可以创建一个不包含隐私信息的视图
-- 数据独立性，修改视图中的值不改变原来的值
-- 数据重用和一致性
