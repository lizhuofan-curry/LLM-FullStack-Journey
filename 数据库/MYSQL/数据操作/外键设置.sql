use my_school;
-- 约束
-- 主键约束 primary key 
-- 必须唯一unique，不能为空not null
-- 一个表只能有一个主键
-- 主键可以是单列，也可以是多列组合（复合主键
-- 主键通常搭配auto_increment
-- 复合主键不能设置自动递增



-- 外键约束 foreign key 
-- 用于在一个表中建立与另一个表的主键的连接
create table department(
  dept_id int primary key,
  dept_name varchar(100) not null
);
create table employees(
  employees_id int primary key auto_increment,
  first_name varchar(50) not null,
  dept_id INT,
  constraint fk_employee_dept foreign key(dept_id)
      REFERENCES department(dept_id)
      on delete set null -- 如果部门被删除，员工的部门ID为null
      on update cascade -- 如果部门id更新，员工的部门ID也更新
      
      -- 简洁版外键设置
      -- foreign key(dept_id) references department(dept_id)
);
