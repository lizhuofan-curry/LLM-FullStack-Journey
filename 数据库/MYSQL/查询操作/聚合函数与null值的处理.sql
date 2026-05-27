use my_first_db;
-- 查询平均工资
select avg(salary) as total_avg_salary
from employees;
-- 练习聚合函数与null值的处理
-- count(*)会计算所有的行，包括含有null的行
-- count(column_name):只会计算列中非null值的行数
-- sum(),avg(),max(),min(),这些函数在计算时会自动忽略null

-- 现在在表中插入一个bonus的列，其中包含null值
alter table employees add column bonus INT;

-- 插入bonus数据
update employees set bonus=5000 where id=1;
update employees set bonus=null  where id=2;
update employees set bonus=10000 where id=3;
update employees set bonus=5000 where id=4;
update employees set bonus=10000 where id=5;

-- 计算有奖金的人数
select count(bonus) from employees;
-- 计算总人数
select count(*) from employees;
-- 计算平均奖金（只计算有奖金的人）
select avg(bonus) from employees;
-- 如果想把null 当做0来计算平均奖学金，需要用ifnull()函数
select avg(ifnull(bonus,0)) from employees;
