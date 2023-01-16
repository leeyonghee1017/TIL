*-- primary key
create database tabledb;
use tabledb;

create table usertbl
(
	userid varchar(8) primary key,
	name varchar(10) not null,
	birthyear int not null
);

alter table usertbl 
	drop primary key;
	
show index from usertbl;

alter table usertbl 
	add primary key (userid);
	
show index from usertbl;

create table prodtbl
(
	prodcode char(3) not null,
	prodid char(4) not null,
	proddate datetime not null,
	pordcud char(10) not null,
	primary key (prodcode, prodid)
);

show index from prodtbl;

alter table prodtbl 
	drop primary key;
	
show index from prodtbl;

alter table prodtbl 
	add primary key (prodcode, prodid);
	
show index from prodtbl;


*-- foreign key
create table buytbl
(
	num int auto_increment primary key,
	userid varchar(8) not null,
	prodname varchar(8) not null,
	constraint fk_bustbl_usertbl foreign key (userid)
	references usertbl (userid)
);

alter table buytbl
	drop constraint fk_bustbl_usertbl;
	
alter table buytbl 
	add constraint fk_bustbl_usertbl foreign key (userid)
	references usertbl (userid);
	
show index from buytbl;

insert into usertbl values('LSG', '이승기', 1987);
insert into usertbl values('KBS', '김범수', 1979);
insert into buytbl values(null, 'LSG', '운동화');
insert into buytbl values(null, 'LSG', '노트북');

select * from usertbl;
select * from buytbl;

-- 기준테이블(usertbl) userid에 'ABC' 데이터가 없으므로 에러 발생
insert into buytbl values(null, 'ABC', '노트북');
update buytbl set userid = 'ABC' where num = 1;

-- 기준테이블에 'ABC' insert
insert into usertbl values('ABC', '홍길동', 1990);
select * from usertbl u ;
insert into buytbl values(null, 'ABC', '노트북');
select * from buytbl;
update buytbl set userid = 'ABC' where num = 1;
select * from buytbl;

-- 기준테이블 데이터 변경 / 삭제
update usertbl set userid = 'DEF' where userid = 'ABC';
delete from usertbl where userid = 'ABC';

-- 기준테이블 변경, 삭제 시 외래키테이블 자동적용
alter table buytbl
	drop constraint fk_bustbl_usertbl;

alter table buytbl 
	add constraint fk_bustbl_usertbl foreign key (userid)
		references usertbl(userid)
		on update cascade
		on delete cascade;
		
delete from usertbl where userid = 'ABC';
select * from usertbl u ;
select * from buytbl;

update usertbl set userid ='DEF' where userid = 'LSG';
select * from usertbl u ;
select * from buytbl; 

-- unique key
alter table usertbl 
	add email varchar(50);
	
select * from usertbl u ;

alter table usertbl 
	add constraint uk_usertbl_email
	unique key (email);
	
show index from usertbl;

-- check
alter table usertbl 
	add constraint chk_usertbl_birthyear
	check (birthyear >= 1900);
	
insert into usertbl(userid, name, birthyear, email) values('ABC', '홍길동', 1500, null);

-- default
alter table usertbl 
	alter column birthyear set default 2023;
	
insert into usertbl(userid, name, birthyear, email) values('ABC', '홍길동', default, null);
select * from usertbl u ;

insert into usertbl(userid, name, email) values('XYZ', '테스트', null);
select * from usertbl u ;

-- null
alter table usertbl 
	modify column name varchar(8) null;	
select * from usertbl u ;

insert into usertbl(userid, name, birthyear, email) values('AAA', null, 1990, 'test@gamil.com');
select * from usertbl u ;

-- null 데이터 update 후 not null 변경 가능
select * from usertbl u where name is null;

update usertbl set name = '강감찬' where name is null;

alter table usertbl 
	modify column name varchar(8) not null;
	
desc usertbl ;

*-- view
create view v_usertbl
as
select userid, name, email
	from usertbl u 
	where email is not null;
	
select * from v_usertbl;



use sqldb;

create view sum_buytbl
as
select prodname,groupname,sum(amount),sum(amount*price)
	from buytbl b 
	group by prodname,groupname;
	
select * from sum_buytbl;


drop view sum_buytbl;



create view sum_buytbl
as
select prodname,groupname,sum(amount) sum_amount,sum(amount*price) sum_total
	from buytbl b 
	group by prodname,groupname;
	
select * from sum_buytbl;