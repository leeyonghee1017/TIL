*-- 1. data Type
use sqldb;

*-- 변수 선언 및 출력
set @a = 10;
set @b = 20;
set @stra = "mariadb";

select @a, @b, @stra;

*-- 테이블과 변수 출력
select @stra, u.*
from usertbl u;

-- 2. Data 형변환
select 	cast(avg(amount) as integer),
		convert(avg(amount),integer), 
		count(*),
		sum(amount) 
	from buytbl b;

select '3000 * 5 = 15000';

select price, amount, price*amount from buytbl b ;

-- "단가 * 수량 = 금액" 조회
-- 숫자를 문자형으로 바꾸기
-- 문자를 연결해야 함 : concat() 활용
select concat(price, '*', amount, '=', price * amount) from buytbl b ;

select 	price, amount, price*amount,
		concat(cast(price as varchar(10)),
		' * ',
		cast(amount as varchar(10)),
		' = ',
		cast(price * amount as varchar(10)))
	from buytbl b ;


-- 2. 내장 / 윈도우 함수
-- 1) 제어흐름 함수
-- if(수식, 값1, 갑2)
-- usertbl의 birthyear가 50세 이상인 경우는 '50세 이상', 그 외에는 '50세 미만'으로 조회
select name, birthYear, if (birthyear <= '1972', '50세 이상', '50세 미만') from usertbl u ;

-- ifnull(수식1, 수식2)
-- usertbl에서 mobile1에 값이 있는 경우는 해당 값을, 없는 경우는 '연락처 없음'을 조회
select name, mobile1, ifnull(mobile1,'연락처없음') from usertbl u ;

-- nullif(수식1,수식2)
select name,mobile1,nullif(mobile1,'010') from usertbl u ;

-- case when else end
-- addr이 '서울'이거나 '경기'이면 '수도권'으로 조회하고, 나머지는 그대로 조회
select 	name, 
		addr,
		case addr 
			when '서울' then '수도권' 
			when '경기' then '수도권'
			else addr 
		end
from usertbl u ;

-- 2) 문자열 함수
-- BIT_LENGTH, CHAR_LENGTH, LENGTH
-- 'abc', '가나다'
select 	bit_length('abc'),
		CHAR_LENGTH('abc'),
		LENGTH('abc');
	
select 	bit_length('가나다'),
		CHAR_LENGTH('가나다'),
		LENGTH('가나다');

-- instr
select instr('apple banana orage', 'ppl');
select instr('apple banana orage', 'or');

-- format
select format(1234.578,2);

-- left, right
select left('apple banana orage', 5), right('apple banana orage', 5);

-- replace
select replace ('이것이 MariaDb이다','이것이','This is');

-- substring
select 	substring(name, 2, char_length(name)-1),
		name,
		char_length(name)
	from usertbl u ;

-- 3) 수학 함수
-- ceil, floor, round, truncate 
select ceil (4.7),floor (4.7),round (4.7),truncate (4.739,2);

-- rand
select rand();

-- 4) 날짜 / 시간 함수
-- adddate, subdate
select 	name, mdate,
		adddate(mdate, interval 1 month),
		adddate(mdate, interval 1 year)
	from usertbl u ;

select 	name, mdate,
		subdate(mdate, interval 1 month),
		subdate(mdate, interval 1 year)
	from usertbl u ;

-- now(), sysdate(), year(), month(), day()
select now(), sysdate();

select year (now()), month (now()),day (now()),date(now()),time(now())

-- period_add(), period_diff()
select period_add(202301, 3), period_diff(202301, 202111);  

-- 5) 시스템 정보 함수
-- user, database
select user(),database();

-- found_rows
select * from buytbl b ;
select found_rows(); 

-- row_count
update buytbl set amount=3 where userID = 'KBS';
select row_count();

select * from buytbl b where userID ='KBS';


create table emptbl(
	empid char(3) primary key,
	empname char(10),
	emptel char(10),
	managerid char(10)
);

INSERT INTO emptbl VALUES('101', '나사장', '101', '0000');
INSERT INTO emptbl VALUES('201', '김재무', '101', '2222');
INSERT INTO emptbl VALUES('202', '김부장', '201', '2222-1');
INSERT INTO emptbl VALUES('203', '이부장', '201', '2222-2');
INSERT INTO emptbl VALUES('204', '우대리', '203', '2222-2-1');
INSERT INTO emptbl VALUES('205', '지사원', '203', '2222-2-2');
INSERT INTO emptbl VALUES('206', '이영업', '101', '1111');
INSERT INTO emptbl VALUES('207', '한과장', '206', '1111-1');
INSERT INTO emptbl VALUES('208', '최정보', '101', '3333');
INSERT INTO emptbl VALUES('209', '윤차장', '208', '3333-1');
INSERT INTO emptbl VALUES('210', '이주임', '209', '3333-1-1');

select * from emptbl;


*-- 4. SQL프로그래밍
drop procedure if exists ifproc;

delimiter $$
create procedure ifproc()
begin
	declare var1 int;
	set var1 = 100;
	
	if var1 = 100 then
		select '100과 일치합니다.';
	else
		select '100이 아닙니다.';
	end if;
end $$

delimiter ;

call ifproc();

-- 2) case 구문 예제
drop procedure if exists caseproc;

delimiter $$
create procedure caseproc()
begin
	declare point int;
	declare grade char(1);
	set point = 75;
	
	case
		when point >= 90 then set grade = 'A';
		when point >= 80 then set grade = 'B';
		when point >= 70 then set grade = 'C';
		when point >= 60 then set grade = 'D';
		else set grade = 'F';
	end case;

	select point, grade;
end $$

delimiter ;

call caseproc();

*-- 3) 반복문(while)
-- 기본구문
drop procedure if exists whileproc;

delimiter $$
create procedure whileproc()
begin
	declare i int;
	declare total int;
	
	set i = 0;
	set total = 0;
	while i < 100 do
		set i = i +1;
		set total = total + i;
	end while;

	select i, total;
end $$

delimiter ;

call whileproc();

*-- iterate, leave 구문
drop procedure if exists whileproc2;

delimiter $$
create procedure whileproc2()
begin
	declare i int;
	declare total int;
	
	set i = 0;
	set total = 0;

	mywhile : while i < 100 do
		set i = i +1;
		
		if (i%2 = 0) then
			iterate mywhile;
		end if;
	
		set total = total + i;
	
		if total > 1000 then
			leave mywhile;
		end if;
	end while;

	select i, total;
end $$

delimiter ;

call whileproc2();


*-- 4) 오류 처리
drop procedure if exists errproc;

delimiter $$
create procedure errproc()
begin
	declare continue handler for sqlexception
	begin
		show errors;
		rollback;
	end;
	
	-- insert into usertbl(userID,name,birthYear,addr) values('BBK','LEE',1990,'서울');
	insert into usertbl values('BBK');
end $$

delimiter ;

call errproc();


*-- 5) 동적 sql문
-- 기본문
prepare myQuery from 'select * from usertbl where userid="BBK"';

execute myQuery;

deallocate prepare myQuery;


-- userid, mobile1의 조건값을 변수로 대입
set @userid = 'BBK';
set @mobile1 = '010';
prepare myQuery from 'select * from usertbl where userid= ? and mobile1 = ?';
execute myQuery using @userid, @mobile1;

deallocate prepare myQuery;


-- 3개 테이블 join
CREATE TABLE stdtbl(
	id 	varchar(10) not null primary key,
	name	varchar(20) not null,
	addr	varchar(10)
	);

CREATE TABLE clubtbl(
	clubcode varchar(10) not null primary key,
	clubname varchar(20) not null,
	roomno varchar(10)
	);

CREATE TABLE stdclubtbl(
	num	int	AUTO_INCREMENT not null primary key,
	id	varchar(10) not null,
	clubcode varchar(10) not null,
	FOREIGN KEY(id) REFERENCES stdtbl(id),
	FOREIGN KEY(clubcode) REFERENCES clubtbl(clubcode)
	);


-- 데이타 입력	
INSERT INTO stdtbl VALUES ('K001', '김범수', '경남'), ('S001','성시경', '서울'), ('J001','조용필', '경기'), ('E001','은지원', '경북'), ('B001','바비킴', '서울');
INSERT INTO clubtbl VALUES ('SWIM', '수영', '101호'), ('BADK','바둑', '102호'), ('SOCC','축구', '103호'), ('BONS','봉사', '104호');
INSERT INTO stdclubtbl VALUES (NULL, 'K001', 'BADK'), (NULL, 'K001', 'SOCC'), (NULL, 'J001', 'SOCC'), (NULL, 'E001', 'SOCC'), (NULL, 'E001', 'BONS'), (NULL, 'B001', 'BONS');

-- 학생의 이름, 지역, 가입한 동아리코드, 가입한 동아리명 출력
select name, addr, clubcode from stdtbl a inner join stdclubtbl b on a.id = b.id;

select a.name, a.addr, b.clubcode, c.clubname 
from stdtbl a 
inner join stdclubtbl b on a.id = b.id
inner join clubtbl c on b.clubcode  = c.clubcode ;

select c.*, d.clubname 
from (select name, addr, clubcode from stdtbl a inner join stdclubtbl b on a.id = b.id) c
inner join clubtbl d on c.clubcode = d.clubcode ; 