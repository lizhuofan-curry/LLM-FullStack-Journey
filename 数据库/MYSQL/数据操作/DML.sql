-- 练习数据插入操作（DML)

-- 先来创建一个student表
create table student (
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(50) NOT NULL,
  email VARCHAR(100) UNIQUE,
  age INT
);
insert into student(name,email,age)
values('张三','zhangsan@example.com',20);
-- 插入多行数据
insert into student (name,email,age) VALUES
('赵六','zhaoliu@example.com',23),
('孙七','sunqi@example.com',19),
('周八','zhouba@example.com',20);

-- 插入查询结果

-- 先来创建old_student
create table old_students(
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(100) not null,
  email varchar(100) unique,
  age int,
  registration_year int
);
-- 向old_students表插入数据
insert into old_students(name,email,age,registration_year) VALUES
('Alice','alice@example.com',20,2019),
('Bob','bob@example.com',22,2020),
('Charlie','charlie@example.com',19,2018),
('David','david@example.com',21,2021);

-- 将old_students表中的部分学完数据迁移到students表中
insert into student (name,email,age)
select name,email,age
from old_students
