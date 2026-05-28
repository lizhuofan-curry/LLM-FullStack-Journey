use my_school;
-- modify 修改列定义（但是不能修改名字）
-- change 都能修改
alter table products 
modify column stock_quantity int unsigned default 0;
alter table products
add constraint chk_stock_positive check(stock_quantity>=0);
-- 将product中的product_name重命名为item_name,并将最大长度改为200
alter table products
change product_name item_name varchar(200) not null;

-- 重命名表
-- 将product表重命名为item
alter table products
rename to item;

-- 删除表
drop table if exists old_items;
