-- 数据库操作

-- 创建一个新的数据库
-- if not exists :可选，如果已经存在则不执行操作
-- character ： 可选，指定数据库的默认字符集，如utf8mb4
-- collate : 可选，指定数据库默认排序规则 如：utf8mb4_unicode_ci

create database if not exists my_school character set utf8mb4 COLLATE utf8mb4_unicode_ci;

-- 删除数据库
drop database if exists my;

-- 修改数据库（全局特性）
alter database my_school CHARACTER set utf8mb4 COLLATE utf8mb4_general_ci;

show databases;
