drop database if exists pro2_m6y4;
create database if not exists pro2_m6y4;
use pro2_m6y4;

create table if not exists quiz
(
	id int auto_increment primary key,
    name varchar(100)
);

create table if not exists question
(
	id int auto_increment primary key,
    question varchar(200),
    answer varchar(100),
    wrong1 varchar(100),
    wrong2 varchar(100),
    wrong3 varchar(100)
);

create table if not exists quiz_content
(
	id int auto_increment primary key,
    quiz_id int,
    question_id int,
    
    foreign key (quiz_id) references quiz(id),
    foreign key (question_id) references question(id)
);

-- alter table quiz_content
-- add constraint question_fk
-- foreign key (question_id) references question(id);

INSERT INTO quiz (name)
VALUES 
  ('Своя игра'), 
  ('Кто хочет стать миллионером?'), 
  ('Самый умный');

insert into question (question, answer, wrong1, wrong2, wrong3)
values ('Сколько месяцев в году имеют 28 дней?', 'Все', 'Один', 'Ни одного', 'Два'),
	('Каким станет зеленый утес, если упадет в Красное море?', 'Мокрым', 'Красным', 'Не изменится', 'Фиолетовым'),
	('Какой рукой лучше размешивать чай?', 'Ложкой', 'Правой', 'Левой', 'Любой'),
	('Что не имеет длины, глубины, ширины, высоты, а можно измерить?', 'Время', 'Глупость', 'Море', 'Воздух'),
	('Когда сетью можно вытянуть воду?', 'Когда вода замерзла', 'Когда нет рыбы', 'Когда уплыла золотая рыбка', 'Когда сеть порвалась'),
	('Что больше слона и ничего не весит?', 'Тень слона', 'Воздушный шар', 'Парашют', 'Облако');
    
select *
from quiz;

select *
from question;

select *
from quiz
cross join question
order by name;