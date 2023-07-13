use sqldb;
-- in 포함된 프로시져
select * from usertbl u ;

drop procedure if exists userproc1;

delimiter $$
create procedure userproc1(in username varchar(10))
begin
	select * from usertbl where name = username;
end $$
delimiter ;

call userproc1('바비킴');

-- out 포함된 프로시저 생성

drop procedure if exists userproc2;

delimiter $$
create procedure userproc2(in username varchar(10), out v_userid char(8))
begin
	select userid into v_userid from usertbl where name = username;
end $$
delimiter ;

call userproc2('바비킴', @v_userid);
select @v_userid;

-- 스토어드 함수
drop function if exists userfunc;

delimiter $$
create function userfunc(value1 int, value2 int)
	returns int
begin
	return value1 + value2;
end $$
delimiter ;

select userfunc(100,200);

select userfunc(height,100) from usertbl;
select left(name,2) from usertbl u ;

-- 커서
drop procedure if exists cursorproc;

delimiter $$
create procedure cursorproc()
begin
	declare userheight int;
	declare cnt int default 0;
	declare totalheight int default 0;

	declare end0Row boolean default false;
	declare usercursor cursor for
		select height from usertbl;
	declare continue handler
		for not found set end0Row = true;
	open usercursor;
	cursor_loop:loop 
		fetch usercursor into userheight;
		if end0Row then leave cursor_loop;
		end if;
		set cnt = cnt + 1;
		set totalheight = totalheight + userheight;
			
	end loop cursor_loop;
	
	select totalheight / cnt;

	close usercursor;
	
end $$
delimiter ;

call cursorproc();

-- 트리거
-- 백업테이블 생성
CREATE TABLE backup_userTBL
( userID		CHAR(8) not null primary key, 	-- 사용자 아이디(PK)
  name		VARCHAR(10) NOT NULL, 		-- 이름
  birthYear	INT NOT NULL,			-- 출생연도
  addr		CHAR(2) NOT NULL,		-- 지역(서울, 경기, 경남)
  mobile1	CHAR(3),				-- 국번
  mobile2	CHAR(8),				-- 번호2
  height		SMALLINT,			-- 키
  mDate		DATE				-- 회원 가입일
);


-- 트리거 생성 : delete
drop trigger if exists backtbl_deletetrg;

delimiter $$
create trigger backtbl_deletetrg
	after delete 
	on usertbl
	for each row
begin
	insert into backup_userTBL
	values(old.userid, old.name, old.birthyear, old.addr, old.mobile1, old.mobile2, old.height, old.mDate);
end $$
delimiter ;

delete from usertbl where userid='EJW';

select * from backup_userTBL;
