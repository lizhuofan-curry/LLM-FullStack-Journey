use student_course_system;
create table if not exists users(
  user_id int primary key,
  user_name varchar(50)
);

insert into users(user_id,user_name)VALUES
(1,'Alice'),
(2,'Bob'),
(3,'Charlie');
select * from users;

create table if not exists orders(
  order_id int primary key,
  user_id int ,
  order_amount int
);

insert into orders(order_id,user_id,order_amount)VALUES
(101,1,100),
(102,1,150),
(103,2,200);
select * from orders;
-- 查询所有用户及订单信息
select users.user_id,users.user_name,orders.order_amount
from users
left join orders 
on users.user_id=orders.user_id;
-- 左连接把左边表格的内容全部保存下来
-- 如果右边表格没有的就填上null

-- 右连接 
-- 保留右表中全部信息
select b.order_id ,a.user_name,b.order_amount
from users a
right join orders b
on a.user_id=b.user_id;

-- 全外连接 full join 
-- mysql 中不支持full join关键字，但我们可以通过left join和 right join 的结果使用union 来模拟
-- union方式会去除重复行
insert into orders values (104,4,50);
select * from orders;
-- 实现全连接
select a.user_name,a.user_id,b.order_id,b.user_id
from users a
left join orders b
on a.user_id=b.user_id
union
select a.user_name,a.user_id,b.order_id,b.user_id
from users a
right join orders b
on a.user_id=b.user_id;

-- 自连接
-- 自连接是指一个表与其自身连接，这常用语查询表中行与行之间存在某种层次关系或比较关系
-- 在自连接中，必须使用别名，以区分同一个表的两个不同实例

create table if not exists employees(
  emp_id int primary key,
  emp_name varchar(100),
  manager_id int
);
insert into employees values
(1,'Alice',null),
(2,'Bob',1),
(3,'Charlie',1),
(4,'David',2);
select * from employees;

-- 通过自连接查找每个员工对应的经理是谁
select a.emp_id,a.emp_name,b.emp_name
from employees a
left join employees b
on a.manager_id=b.emp_id;
