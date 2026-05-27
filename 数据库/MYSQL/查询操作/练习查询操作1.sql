use my_first_db;
-- 查询IT部门的员工;
select name,department from employees where department='IT';
-- 查询薪资大于700000的员工
select name,salary from employees where salary>70000;
-- 查询IT部门且薪资大于80000的员工
select name,department,salary from employees where department='IT' and salary>80000;
-- 查询HR部门或Sales部门的员工
select name,department,salary from employees where department='IT' or department='Sales';
-- 查询薪资在60000到70000之间的员工（包含边界）
select name,department,salary from employees where salary between 60000 and 70000;
-- 查询部门为HR 或IT的员工
select name,department from employees where department in('IT','HR');
-- 查询姓名以‘A’开头的员工
select name from employees where name like 'A%';
-- 查询姓名以‘e’结尾的员工
select name from employees where name like '%e';
-- 查询姓名中包含‘li’的员工
select name from employees where name like '%li%';
-- 查询姓名第二个字符是o的员工
select name from employees where name like '_o%';
