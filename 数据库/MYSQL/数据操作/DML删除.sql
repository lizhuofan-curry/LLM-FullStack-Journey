use my_first_db;
-- 更新 update...set...where...
update student
set email='zhangsan_new@example.com'
where id=1;

-- 将所以年龄小于20岁的同学的年龄加一岁
update student
set age=age+1
where age<20;

-- 练习删除操作
-- delete from ...where
delete from student where id=3;
insert into student (id,name,email,age) 
values(3,'张三','zhangsan@example.com',20);

-- 删除student表中所有年龄大于22岁的学生记录
delete from student where age>22;

-- 清空student 表并重新计数
truncate table student;
