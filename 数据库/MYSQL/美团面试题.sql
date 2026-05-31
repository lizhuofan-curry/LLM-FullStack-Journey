-- sql作业1

-- 创建学生表
create table if not  exists students(
  student_id int primary key,
  student_name varchar(50),
  class varchar(50)
);

-- 创建课程表
create table if not  exists courses(
  course_id int primary key,
  course_name varchar(50)
);

-- 成绩表
create table if not  exists scores(
  id int primary key AUTO_INCREMENT,
  student_id int ,
  course_id int,
  score decimal(5,2),
  foreign key (student_id) references students(student_id),
  foreign key (course_id) references courses(course_id)
);

-- 学生
INSERT INTO students (student_id, student_name, class) VALUES
(1, '张伟', '高一(1)班'),
(2, '李娜', '高一(1)班'),
(3, '王强', '高一(1)班'),
(4, '赵敏', '高一(2)班'),
(5, '孙磊', '高一(2)班'),
(6, '刘洋', '高一(2)班'),
(7, '杨静', '高一(3)班'),
(8, '董鹏', '高一(3)班'),
(9, '周婷', '高一(3)班'),
(10, '吴昊', '高一(3)班');

-- 课程
INSERT INTO courses (course_id, course_name) VALUES
(1, '语文'),
(2, '数学'),
(3, '英语'),
(4, '物理'),
(5, '化学'),
(6, '历史');

-- 成绩（AUTO_INCREMENT 的 id 可省略）
INSERT INTO scores (student_id, course_id, score) VALUES
(1, 1, 92.50), (1, 2, 88.00), (1, 3, 85.75), (1, 4, 91.00), (1, 5, 86.50), (1, 6, 78.25),
(2, 1, 78.00), (2, 2, 81.25), (2, 3, 79.50), (2, 4, 75.00), (2, 5, 80.00), (2, 6, 83.75),
(3, 1, 88.75), (3, 2, 90.50), (3, 3, 84.00), (3, 4, 87.25), (3, 5, 82.00), (3, 6, 76.50),
(4, 1, 69.50), (4, 2, 72.00), (4, 3, 74.25), (4, 4, 70.00), (4, 5, 68.00), (4, 6, 71.75),
(5, 1, 95.00), (5, 2, 93.50), (5, 3, 90.25), (5, 4, 92.75), (5, 5, 89.50), (5, 6, 85.00),
(6, 1, 82.25), (6, 2, 78.50), (6, 3, 80.75), (6, 4, 79.00), (6, 5, 77.25), (6, 6, 81.50),
(7, 1, 60.00), (7, 2, 65.50), (7, 3, 70.25), (7, 4, 62.75), (7, 5, 68.50), (7, 6, 73.00),
(8, 1, 85.00), (8, 2, 88.75), (8, 3, 86.00), (8, 4, 84.50), (8, 5, 83.25), (8, 6, 79.75),
(9, 1, 91.25), (9, 2, 89.00), (9, 3, 93.50), (9, 4, 90.75), (9, 5, 92.00), (9, 6, 88.25),
(10, 1, 74.50), (10, 2, 71.25), (10, 3, 69.00), (10, 4, 72.75), (10, 5, 75.50), (10, 6, 70.00);

select * from students;
select * from courses;
select * from scores;

-- 题目1 如何查到数学成绩排名第二的学生
-- 法一用窗口函数
select 
student_id,
student_name,
class,
course_name,
score,
ranking
from (
  select 
  s.student_id,
  s.student_name,
  s.class,
  c.course_name,
  sc.score,
  rank() over(order by sc.score desc) as ranking
  from scores sc
  join students s on sc.student_id=s.student_id
  join courses c on c.course_id=sc.course_id
  where c.course_name='数学'
)as A
where ranking =2;

-- 法二 用limit 和 offset
select s.class,s.student_id,s.student_name,c.course_name,sc.score
from students s
join scores sc on sc.student_id = s.student_id
join courses c on c.course_id = sc.course_id
where c.course_name='数学'
order by sc.score desc
limit 1 offset 1;

-- 题目二：从学生表和成绩表中，查询学生学号，姓名，平均成绩
-- 法一 group
select 
s.student_id,
s.student_name,
ifnull(avg(sc.score),0) as avg_score,
count(sc.score) as count
from students s 
join scores sc on sc.student_id=s.student_id
group by s.student_id,s.student_name
order by avg_score desc;
-- 法二 窗口函数
select DISTINCT
s.student_id,
s.student_name,
avg(sc.score) over(partition by sc.student_id) as avg_score
from students s 
join scores sc on sc.student_id=s.student_id
order by avg_score desc;

-- 题目三 有一个储存学生各课程成绩的表，要求用mysql查询出每个学生的总成绩
select 
s.student_id,
s.student_name,
sum(sc.score) as sum_score
from students s 
join scores sc on sc.student_id=s.student_id
group by s.student_id,s.student_name
order by sum_score desc;
