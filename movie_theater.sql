-- creating tables 
CREATE TABLE customer (
        customer_id SERIAL,
        first_name VARCHAR(100),
        last_name VARCHAR(100),
        phone_number INT
);

CREATE TABLE concessions (
        customer_id SERIAL,
        item_number SERIAL,
        item_cost INT,
        item_name VARCHAR(100)
);

CREATE TABLE tickets (
        customer_id SERIAL,
        ticket_number INT
);

CREATE TABLE movies (
        ticket_number INT,
        movie_name VARCHAR(100),
        movie_genre VARCHAR(100),
        movie_length INT
);

--inserting info for each table
INSERT INTO customer VALUES
('Ab1' ,'Shawn', 'Doe', '000-111-2222'),
('Ab2', 'Jim', 'Bennett', '000-222-3333');


INSERT INTO concessions VALUES
('Ab1', '5114'. '10.99', 'popcorn'),
('Ab2', '5874', '4.59', 'sour patches');

INSERT INTO tickets VALUES
('Ab1', '6851-1'),
('Ab2', '7891-5');

INSERT INTO parts VALUES
('6851-1','Big Daddy', 'Comedy/Drama', '94'),
('7891-5','The Litte Mermaid', 'Fantasy', '83');