-- 1. 确保在 my_first_db 数据库下操作
USE my_first_db;

-- 2. 使用 IGNORE，如果 id 冲突了会自动跳过，不冲突就正常插入
INSERT IGNORE INTO employees (id, name, age, department, salary) VALUES
(1, 'Alice', 30, 'HR', 60000),
(2, 'Bob', 24, 'IT', 75000),
(3, 'Charlie', 35, 'IT', 90000),
(4, 'David', 28, 'Sales', 65000),
(5, 'Eve', 30, 'HR', 62000);

-- 3. 最后一睹风采
SELECT * FROM employees;
