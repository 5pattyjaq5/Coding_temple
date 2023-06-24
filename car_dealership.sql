-- creating tables 
CREATE TABLE customer (
        customer_id SERIAL,
        first_name VARCHAR(100),
        last_name VARCHAR(100),
        invoice_number INT,
        service_ticket INT
);

CREATE TABLE vehicles (
        vin_number SERIAL,
        vehicle_new BOOLEAN,
        vehicle_miles NUMERIC,
        vehicle_make VARCHAR(100),
        vehicle_model VARCHAR(100),
        vehicle_year INT,
        customer_id INT,
        service_ticket INT,
        invoice_number INT
);

CREATE TABLE salesrep (
        salesRep_id SERIAL,
        invoice_number INT
);

CREATE TABLE parts (
        parts_number SERIAL,
        vin_number INT
);

CREATE TABLE service (
        mechanic_id SERIAL,
        service_ticket INT,
        parts_number INT,
        service_type VARCHAR(100)
);

--inserting info for each table
INSERT INTO customer VALUES
('50001' ,'Jane', 'Doe', '6851-1', '18545'),
('50002', 'Jim', 'Street', '7891-5', '58754'),
('50003', 'Keizer', 'Jacques', '6858-1', '48456');

INSERT INTO vehicles VALUES
('1GNUKCE05AR206294', 'no', '86,968', 'Chevrolet', 'Tahoe', '2010', '50001','18545', '6851-1' ),
('5N1AR2MN8FC625745', 'yes', '10', 'Nissan', 'Pathfinder', '2015', '50002', '58754', '7891-5'),
('5N1DR2MM6JC626082', 'yes', '0', 'Nissan', 'Pathfinder', '2018', '50003','48456', '6858-1');

INSERT INTO salesrep VALUES
('100', '6851-1'),
('100', '7891-5'),
('105', '6858-1');

INSERT INTO parts VALUES
('FG1054','1GNUKCE05AR206294'),
('33500','5N1AR2MN8FC625745'),
('YH477843P','5N1DR2MM6JC626082');

INSERT INTO service VALUES
('A9696','18545','FG1054', 'Fuel Pump'),
('A8696','58754','33500', 'TPMS'),
('A7696','48456','YH477843P', 'Brake Rotors');