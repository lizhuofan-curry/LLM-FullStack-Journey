-- 实践案例：学生选课系统表结构设计与数据填充

-- 设计并实现一个简化的学生选课系统的数据表结构
-- 先来创建一个student_course_system数据库
create database if not exists student_course_system;
use student_course_system;

-- 创建students表
create table if not exists student(
  student_id int primary key auto_increment,
  student_name varchar(100) not null,
  email varchar(100) unique not null,
  enrollment_year int 
)engine=innodb;

-- 创建course表
create table if not exists course(
  course_id int primary key auto_increment,
  course_name varchar(100) unique not null,
  credits int not null,
  constraint chk_credits check (credits>0)
)engine=innodb;

-- 创建选课表enrollment
create table if not exists enrollment(
  enrollment_id int primary key AUTO_INCREMENT,
  student_id int,
  course_id int,
  enrollment_date DATE default(CURRENT_DATE),
  grade varchar(10),
  constraint fk_enrollment_student 
  foreign key(student_id) 
  references student(student_id) 
  on update cascade,
  constraint fk_enrollment_course
  foreign key(course_id)
  references course(course_id)
  on update cascade,
  -- 一个学生一门课只能选一次
  constraint uni_student_course 
  unique(student_id,course_id)
)engine=innodb;

-- 向表中插入数据
-- 插入学生数据
insert into student(student_name,email,enrollment_year)value
('刘一','liuyi@example.com',2021),
('陈二','chener@example.com',2022),
('张三','zhangsan@example.com',2021),
('李四','lisi@example.com',2023),
('王五','wangwu@example.com',2022);
select * from student;

-- 插入课程数据
insert into course(course_name,credits)VALUES
('数据库原理',3),
('计算机网络',4),
('操作系统',3),
('数据结构',4);
select * from enrollment;
-- 插入选课记录
-- 假设刘一（id=1）选了数据库（id=1）和计算机网络（id=2）
insert into enrollment(student_id,course_id,enrollment_date,grade)VALUES
(1,1,'2023-09-02','A'),
(1,2,'2023-09-02','B+');
-- 张三（id=3）选了数据库原理（id=1）和数据结构（id=4）
insert into enrollment(student_id,course_id,enrollment_date)VALUES
(3,1,'2023-09-02'), 
(3,4,CURDATE()); 
-- 李四（id=4）选了操作系统（id=3）
insert into enrollment(student_id,course_id) VALUES
(4,3);

-- 数据的修改和删除
-- 将张三的邮箱修改为zhangsan_new@examp.com
select * from student;
update student
set email='zhangsan_new@examp.com'
where student_id=3;

-- 更新某个选课记录成绩
-- 更新张三的数据库成绩为‘A-’
select * from enrollment;
update enrollment
set grade='A-'
where student_id=3 and course_id=1;

-- 删除某个选课记录
-- 刘一退选了计算机网络（id=2）
delete from enrollment
where student_id=1 and course_id=2;
select * from student;
-- 删除一名学生，假设陈二退学，所有的选课记录也应该删除
-- 先为陈二插入一条选课记录以便观察联级删除效果
insert into enrollment(student_id,course_id,grade)VALUES
(2,1,'A');
