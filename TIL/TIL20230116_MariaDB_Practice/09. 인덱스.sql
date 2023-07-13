create database indexdb;
use indexdb;

*-- 클러스터형 인덱스
select * from usertbl;

create table usertbl
(
	userid varchar(8) primary key,
	name varchar(10) not null,
	birthyear int not null,
	addr varchar(10) not null
);

INSERT INTO usertbl VALUES('LSG', '이승기', 1987, '서울');
INSERT INTO usertbl VALUES('KBS', '김범수', 1979, '경남');
INSERT INTO usertbl VALUES('KKH', '김경호', 1971, '전남');
INSERT INTO usertbl VALUES('JYP', '조용필', 1950, '경기');
INSERT INTO usertbl VALUES('SSK', '성시경', 1979, '서울');

select * from usertbl;

alter table usertbl
drop primary key;

delete from usertbl;

INSERT INTO usertbl VALUES('LSG', '이승기', 1987, '서울');
INSERT INTO usertbl VALUES('KBS', '김범수', 1979, '경남');
INSERT INTO usertbl VALUES('KKH', '김경호', 1971, '전남');
INSERT INTO usertbl VALUES('JYP', '조용필', 1950, '경기');
INSERT INTO usertbl VALUES('SSK', '성시경', 1979, '서울');

select * from usertbl;

alter table usertbl
add primary key (userid);

select * from usertbl;

-- 보조 인덱스
create index idx_usertbl_addr
	on usertbl (addr);

show table status;
show index from usertbl;


create unique index idx_usertbl_name
	on usertbl(name);

show index from usertbl;

insert into usertbl values('AAA', '성시경', 1990, '인천');

-- 조합인덱스
create index idx_usertbl_02 
	on usertbl (name, birthyear);
	
explain select * from usertbl where name='성시경';

drop index idx_usertbl_name
	on usertbl;
	
show table status;

show index from usertbl;

-- 인덱스 성능 비교
select count(*)
	from employees.employees e ;
	
create table emp 
select * from employees.employees e ;
create table emp_c
select * from employees.employees e ;
create table emp_se
select * from employees.employees e ;

select * from emp;
select * from emp_c;
select * from emp_se;

select count(*)
	 from emp ;
select count(*)
	 from emp_c ;
select count(*)
	 from emp_se ;
	 
show table status;

analyze table emp;
analyze table emp_c;
analyze table emp_se;

show table status;



alter table emp_c 
add primary key (emp_no);

explain select * from emp where emp_no between 10000 and 10020;
explain select * from emp_c where emp_no between 10000 and 10020;
explain select * from emp_se where emp_no = 10020;

-- 강제로 인덱스 제외
explain select * from emp_c ignore index (primary) where emp_no=10020;

-- 강제로 인덱스 적용
explain select * from emp_se where emp_no*1=10020;
explain select * from emp_se use index (idx_emp_se) where emp_no=10020;

create index idx_emp_se_01
on emp_se(first_name);

show index from emp_se;

explain select * from emp_se where first_name = 'Remzi' and emp_no=10097 ;
explain select * from emp_se use index (idx_emp_se_01) where first_name = 'Remzi' and emp_no=10097 ;