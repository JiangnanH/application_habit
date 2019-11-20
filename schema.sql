
drop database if exists awesome;

create database awesome;

use awesome;

grant select, insert, update, delete, create on awesome.* to 'www-data'@'localhost';
