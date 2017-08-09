CREATE DATABASE store;
USE store;
DROP DATABASE IF EXISTS store;

DROP TABLE category;
DROP TABLE product;
unlock tables;
SET SQL_SAFE_UPDATES=0;

CREATE TABLE category(
id INT auto_increment PRIMARY KEY, 
name VARCHAR(30) unique
);

CREATE TABLE product(
category INT,
description VARCHAR(50),
price DOUBLE,
title VARCHAR (50),
favorite boolean default false,
img_url VARCHAR(500),
id INT auto_increment PRIMARY KEY
);
SET FOREIGN_KEY_CHECKS=0;
-- describe product;

INSERT INTO category (name) VALUES 
('Fruits'),('Vegetables'),('Meats'); -- TO ADD: (4,'Poultry'),(5,'Nuts'),(6,'Fish'),(7,'Dairy'),(8,'Health');

INSERT INTO product (category, description, price, title, favorite, img_url) VALUES 
(1, 'Fresh bananas from Northern Israel',10.50,'Bananas',false,'./images/bananas.png'),
(1, 'Fresh strawberries locally grown',14.0,'Strawberries',false,'./images/strawberries.png'),
(1, 'Fresh apples from Central Israel',9.0,'Apples',false,'./images/apples.png'),
(2, 'Fresh carrots from the Golan Heights',7.5,'Carrots',false,'./images/carrots.png'),
(2, 'Fresh tomatoes imported from Italy ',9.0,'Tomatoes',false,'./images/tomatoes.png'),
(2, 'Fresh cucumbers from Central Israel ',6.0,'Cucumbers',false,'./images/cucumbers.png'),
(3, 'Organic chicken',15.0,'Chicken',false,'./images/chicken.png'),
(3, 'Farm fresh beef',19.5,'Beef',false,'./images/beef.png'),
(3, 'Free range turkey',22.75,'Turkey',false,'./images/turkey.png');

SELECT category.name, product.title
FROM product 
INNER JOIN category ON category.id = product.category
GROUP BY category.id ORDER BY category.id;

SELECT product.id FROM product;
SELECT * FROM product WHERE id = 2
unlock tables
delete from product where category = 1
select * from category