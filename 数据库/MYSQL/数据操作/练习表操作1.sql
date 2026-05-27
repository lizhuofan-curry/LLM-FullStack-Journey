-- 练习表操作
use my_school;

-- 创建表
create table if not exists products(
  product_id int AUTO_INCREMENT PRIMARY key,
  product_name varchar(255) not null,
  category varchar(100),
  price decimal(10,2) not null,
  stock_quantity int default 0,
  create_at timestamp default CURRENT_TIMESTAMP
);
