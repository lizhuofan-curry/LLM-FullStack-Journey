use student_course_system;
-- 练习事务控制
-- 默认情况下，每条sql语句都被视为一个单独的事务并自动提交
-- autocommit=1
-- 要执行多语句事务，需要禁用自动提交或使用start transaction
-- 用start transaction 或者 begin
-- 在执行了上面两个语句之一后，auto commit会在当前会话中被临时禁用，直到执行commit或rollback

-- commit 用于提交当前事务，所作的数据修改被永久保存在数据库中

-- rollback 用于回滚和撤销当前事务，将事务期间所做的所有数据修改恢复到事务开始前的状态

-- 保存点 ，允许在事务内部创建标记，以便后续可以将事务回滚到该标记点，而不是回滚整个事务

-- 创建保存点 savepoint ..name..
-- 回滚到保存点 rollback to savepoint name...
-- 保存点不需要显式释放，commit或者rollback会清理所有保存点

-- 模拟银行转账

create table if not exists accounts(
  account_id varchar(50)primary key,
  balance int
); 
insert into accounts(account_id,balance)VALUES
('A',1000),
('B',500);
select * from accounts;
-- 模拟a向b转账200
start transaction;
-- 1,从账户扣款
update accounts set balance=balance-200 where account_id='A';
-- 在这里设置一个保存点，如果后续操作失败，可以回滚到这里
savepoint sp1;
-- 向账户B存款
update accounts set balance=balance+200 where account_id='B';
-- 后续还需判断操作是否合理，如balance>0;不合理就选择回滚

-- 这里我们创建一个存储过程 create procedure
drop procedure if exists transfer_money;
delimiter $$

create procedure transfer_money()
BEGIN
    declare balance_A int;
    start transaction;
    -- 扣除A账户余额
    update accounts set balance=balance-200 where account_id='A';
    -- 增加B账户余额
    update accounts set balance=balance+200 where account_id='B';
    -- 查询A账户余额
    select balance into balance_A from accounts where account_id='A';
    -- 判断余额
    if balance_A<0 then rollback;
    select '事务已回滚：账户A余额为负'AS result;
    else commit;
    select '事务已提交：账户更新成功'AS result;
    end if;
end$$

delimiter ;
call transfer_money();    
select * from accounts;
 
