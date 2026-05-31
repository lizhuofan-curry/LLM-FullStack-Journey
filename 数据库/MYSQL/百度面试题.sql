use baidu;
-- 重置环境（注意外键顺序）
DROP TABLE IF EXISTS scores;
DROP TABLE IF EXISTS students;
DROP TABLE IF EXISTS employee;
DROP TABLE IF EXISTS department;

-- 部门表（题目2用）
CREATE TABLE department (
  id INT PRIMARY KEY,
  name VARCHAR(50) NOT NULL
) ENGINE=InnoDB;

-- 员工表（题目1、2用）
-- 题目1只需(id, salary)，为兼容题目2，这里一并提供 name、departmentId
CREATE TABLE employee (
  id INT PRIMARY KEY,
  name VARCHAR(50),
  salary INT NOT NULL,
  departmentId INT,
  CONSTRAINT fk_emp_dept FOREIGN KEY (departmentId) REFERENCES department(id)
) ENGINE=InnoDB;

-- 学生表（题目3、4、5用）
CREATE TABLE students (
  id INT PRIMARY KEY,
  name VARCHAR(50) NOT NULL,
  enrollment_year INT NOT NULL,
  class_id INT NOT NULL
) ENGINE=InnoDB;

-- 成绩表（题目3、4用）
CREATE TABLE scores (
  id INT AUTO_INCREMENT PRIMARY KEY,
  student_id INT NOT NULL,
  subject VARCHAR(50) NOT NULL,
  score INT NOT NULL,
  CONSTRAINT fk_scores_student FOREIGN KEY (student_id) REFERENCES students(id)
) ENGINE=InnoDB;

-- 插入部门数据
INSERT INTO department (id, name) VALUES
  (1, 'Engineering'),
  (2, 'HR'),
  (3, 'Sales');

-- 插入员工数据（覆盖多种薪资与部门场景）
INSERT INTO employee (id, name, salary, departmentId) VALUES
  (1, 'Alice', 100000, 1),
  (2, 'Bob',    90000, 1),
  (3, 'Carol', 100000, 2),
  (4, 'Dave',   80000, 2),
  (5, 'Eve',    90000, 3),
  (6, 'Frank',  70000, 3);

-- 插入学生数据（包含2023、2024用于过滤；包含班级1的重名）
INSERT INTO students (id, name, enrollment_year, class_id) VALUES
  (1, '张伟', 2022, 1),
  (2, '张伟', 2022, 1),
  (3, '李雷', 2023, 1),
  (4, '韩梅梅', 2025, 2),
  (5, '王芳', 2021, 1),
  (6, '陈强', 2024, 2),
  (7, '赵敏', 2020, 1),
  (8, 'John', 2025, 1);  -- 无成绩学生，用于题目3的LEFT JOIN场景

-- 插入成绩数据（构造不同平均分）
-- 学生1 张伟(2022, 班级1)：平均 > 85
INSERT INTO scores (student_id, subject, score) VALUES
  (1, 'Math', 90),
  (1, 'English', 88);

-- 学生2 张伟(2022, 班级1)：平均 < 85
INSERT INTO scores (student_id, subject, score) VALUES
  (2, 'Math', 70),
  (2, 'English', 75);

-- 学生3 李雷(2023, 班级1)：将被题目3过滤
INSERT INTO scores (student_id, subject, score) VALUES
  (3, 'Math', 95),
  (3, 'English', 90);

-- 学生4 韩梅梅(2025, 班级2)：平均 > 85
INSERT INTO scores (student_id, subject, score) VALUES
  (4, 'Math', 92),
  (4, 'English', 93);

-- 学生5 王芳(2021, 班级1)：平均 > 85
INSERT INTO scores (student_id, subject, score) VALUES
  (5, 'Math', 86),
  (5, 'English', 86);

-- 学生6 陈强(2024, 班级2)：将被题目3过滤
INSERT INTO scores (student_id, subject, score) VALUES
  (6, 'Math', 88),
  (6, 'English', 82);

-- 学生7 赵敏(2020, 班级1)：平均 < 85
INSERT INTO scores (student_id, subject, score) VALUES
  (7, 'Math', 84),
  (7, 'English', 84);

-- 学生8 John(2025, 班级1)：无成绩（不插入scores）


-- 题目1 
with ranktable as(
  select 
  salary,
  dense_rank() over(order by salary desc) as rank_num
  from employee
)
select 
max(CASE 
	WHEN rank_num=2 THEN
		salary
	ELSE
		null
END 
) 
from ranktable;

-- 题目2

with rankemp as(
  select 
  d.name as department,
  e.name as employee,
  e.salary,
  ROW_NUMBER()over(partition by e.departmentID order by e.salary desc)as rank_
  from employee e 
  join department d on e.departmentID=d.id
)
select 
department,
employee,
salary
from  rankemp
where rank_=1;

-- 子查询
select 
d.name as department,
e.name as employee,
e.salary
from employee e 
join department d on d.id=e.departmentID
where (e.departmentid,e.salary)in(
select departmentId,max(salary)
from employee
group by departmentId
);

-- 第三题
select 
s.name,
s.enrollment_year,
sc.subject,
sc.score
from students s 
join scores sc on s.id=sc.student_id
where s.enrollment_year not in(2023,2024);


-- 两个表连接找平均成绩大于85分的学生和平均成绩
select 
    s.name as student_name,
    avg(sc.score) as avg_score
    from students s
    join scores sc on sc.student_id=s.id
    group by s.id
    having avg(sc.score)>85;
    
-- 查询班级为1的相同姓名的学生有多少个
select name,count(*) as student_count
from students
where class_id=1
group by name    
having count(*)>1;

