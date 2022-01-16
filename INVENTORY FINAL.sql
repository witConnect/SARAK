CREATE DATABASE Inventory_Management_Final;
USE Inventory_Management_Final;

-- TABLE CRATION
CREATE TABLE IF NOT EXISTS User (
	user_id INT NOT NULL,
    log_password VARCHAR(20) NOT NULL,
    email VARCHAR(50) NOT NULL,
    PRIMARY KEY(user_id)
    );

CREATE TABLE IF NOT EXISTS Store_Owner (
	user_id INT NOT NULL,
    first_name VARCHAR(20) NOT NULL,
    last_name VARCHAR(20) NOT NULL,
    PRIMARY KEY(user_id),
    FOREIGN KEY(user_id) REFERENCES User(user_id)
    );
    

CREATE TABLE IF NOT EXISTS Store (
	store_id INT NOT NULL,
    user_id INT NOT NULL,
    s_name VARCHAR(20) NOT NULL,
    street VARCHAR(20) NOT NULL,
    city VARCHAR(20) NOT NULL,
    state VARCHAR(20) NOT NULL,
    pin BIGINT NOT NULL,
    PRIMARY KEY(store_id),
    FOREIGN KEY(user_id) REFERENCES Store_Owner(user_id)
    ON DELETE CASCADE
    );

CREATE TABLE IF NOT EXISTS Product (
	product_id INT NOT NULL,
    product_name VARCHAR(20) NOT NULL,
    product_type VARCHAR(20) NOT NULL,
    PRIMARY KEY(product_id)
    );
    
CREATE TABLE IF NOT EXISTS Supplier (
	user_id INT NOT NULL,
    supplier_first_name VARCHAR(20) NOT NULL,
    supplier_last_name VARCHAR(20) NOT NULL,
    product_id INT NOT NULL,
    PRIMARY KEY(user_id,product_id),
    FOREIGN KEY (product_id) REFERENCES Product(product_id)
    );
    
CREATE TABLE IF NOT EXISTS Inventory (
	store_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    reorder_lvl INT NOT NULL,
    FOREIGN KEY (store_id) REFERENCES Store(store_id)
    );

-- INSERTING DATA
INSERT INTO USER VALUES(1,'prakash','prakashr7d@gmail.com'),
(2,'kishore','kishoreteenager@gmail.com'),
(3,'jaya','jayasuriya352002@gmail.com'),
(4,'sanjay','sanjaykrishna2001@gmail.com'),
(5,'jeeva','jeevanandsurya@gmail.com'),
(6,'ananad','cibleartist@gmail.com');

INSERT INTO store_owner VALUES(1,'Prakash','R'),
(2,'Kishore','Kumar R'),
(3,'Jayasuriya','E');

INSERT INTO Product VALUES(1,'Aata','Dough'),
(2,'Juice','Edible'),
(3,'Milk','Essentials'),
(4,'Mask','Essentials');

INSERT INTO supplier VALUES(4,'Sanjay','Krishna',1),
(4,'Sanjay','Krishna',2),
(5,'Jeeva','Surya',3),
(6,'Aanand','A',4);

INSERT INTO Store VALUES(1,1,'Prakash Dept','Bava Streeet','Chidambaram','Tamilnadu',632018),
(2,1,'Metric','LU Street','Tenkasi','Tamilnadu',626203),
(3,2,'Kishore Dept','VKK Menon Street','Coimbatore','Tamilnadu',641044),
(4,3,'ExCo','Ma Street','Singanallur','Tamilnadu',640234);

INSERT INTO Inventory VALUES(1,1,40,80),
(1,2,50,100),
(1,3,50,150),
(2,1,40,90),
(2,2,50,120),
(3,4,50,80),
(4,3,60,120);

-- VIEWS

CREATE OR REPLACE VIEW store_count AS
SELECT user_id,COUNT(user_id) AS `Stores Owned`
FROM Store GROUP  BY user_id;

CREATE OR REPLACE VIEW store_info AS
SELECT store_id,user_id,s_name,
CONCAT(street,' ',city,' ',pin,' ',state) Address FROM Store;

CREATE OR REPLACE VIEW all_products AS
SELECT * FROM Product;

CREATE VIEW Products_Suppliers AS SELECT 
supplier.product_id, product_name, user_id, concat(supplier_first_name,supplier_last_name) 
FROM product INNER JOIN supplier ON product.product_id = supplier.product_id;

-- TRIGGERS

CREATE TABLE IF NOT EXISTS User_logs (
	user_id INT,
    log_password VARCHAR(20),
    email VARCHAR(50),
    changedat DATETIME DEFAULT NULL,
    action VARCHAR(50) DEFAULT NULL,
    PRIMARY KEY(user_id)
    );

CREATE TRIGGER before_password_update
	BEFORE UPDATE ON user
    FOR EACH ROW
    INSERT INTO User_logs
    SET action = 'update',
		user_id = OLD.user_id,
        log_password = OLD.log_password,
        email = OLD.email,
        changedat = NOW();
        
CREATE TABLE IF NOT EXISTS Store_logs(
	store_id INT NOT NULL,
    user_id INT NOT NULL,
    s_name VARCHAR(20) NOT NULL,
    street VARCHAR(20) NOT NULL,
    city VARCHAR(20) NOT NULL,
    state VARCHAR(20) NOT NULL,
    pin BIGINT NOT NULL,
    action VARCHAR(50) DEFAULT NULL,
    changedat DATETIME DEFAULT NULL,
    FOREIGN KEY(user_id) REFERENCES Store_Owner(user_id)
    );

CREATE TRIGGER before_delete_store
	BEFORE DELETE ON Store
    FOR EACH ROW
    INSERT INTO Store_logs
    SET action = 'DELETE',
		store_id = OLD.store_id,
        user_id = OLD.user_id,
        s_name = old.s_name,
        street = old.street,
        city = old.city,
        state = old.state,
        pin = old.pin,
        changedat = NOW();
        

-- PROCEDURES
DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `insert_store`(IN sid INT,IN uid INT,IN s_name VARCHAR(20),
IN street VARCHAR(20),IN city VARCHAR(20),IN state VARCHAR(20),IN pin BIGINT)
BEGIN
	INSERT INTO store VALUES(sid,uid,s_name,street,city,state,pin);

END$$
DELIMITER ;


DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `remove_store`(sid INT)
    READS SQL DATA
BEGIN

	DELETE FROM Store WHERE store_id = sid;

END$$
DELIMITER ;


DELIMITER $$
CREATE DEFINER= `root`@`localhost` PROCEDURE `add_item`(IN store_id INT,IN product_id INT,IN  quantity INT,
IN reorder_lvl  INT)
READS SQL DATA
BEGIN
	INSERT INTO inventory VALUES(store_id,product_id,quantity,reorder_lvl);
END$$
DELIMITER ;
