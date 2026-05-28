-- 唯一约束 unique
-- 也可以在表尾进行唯一约束
-- constaitnt xx unique (.. , ..);

-- 非空约束 not null

-- 默认约束 default 
-- update_at timestamp default current_timestamp on update current_timestamp


-- 检查约束 
-- 既能在列尾 如： price decimal(10,2) check(price>0)
-- 也能在列表尾通过constraitnt来设置别名定义
