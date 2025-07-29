-- Create Categories table
CREATE TABLE Categories (
    category_id INT PRIMARY KEY,
    category_name VARCHAR(100)
);

INSERT INTO Categories (category_id, category_name)
VALUES
(1, 'Electric Guitars'),
(2, 'Acoustic Guitars'),
(3, 'Basses'),
(4, 'Accessories');

-- Create Products table
CREATE TABLE Products (
    product_id INT PRIMARY KEY,
    product_code VARCHAR(50),
    product_name VARCHAR(100),
    list_price DECIMAL(10,2),
    discount_percent DECIMAL(5,2),
    date_added DATE,
    category_id INT,
    FOREIGN KEY (category_id) REFERENCES Categories(category_id)
);

INSERT INTO Products (product_id, product_code, product_name, list_price, discount_percent, date_added, category_id)
VALUES
(1, 'STRAT1', 'Fender Stratocaster', 999.99, 10.00, '2022-06-15', 1),
(2, 'TELE2', 'Fender Telecaster', 1099.00, 15.00, '2022-08-22', 1),
(3, 'GIBSON3', 'Gibson Les Paul', 1999.99, 20.00, '2023-01-10', 1),
(4, 'ACOUST1', 'Taylor Acoustic 214ce', 799.00, 8.00, '2022-03-12', 2),
(5, 'BASS1', 'Ibanez Bass', 659.00, 5.00, '2021-11-20', 3);

-- Create Customers table
CREATE TABLE Customers (
    customer_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email_address VARCHAR(100)
);

INSERT INTO Customers (customer_id, first_name, last_name, email_address)
VALUES
(1, 'John', 'Doe', 'john.doe@gmail.com'),
(2, 'Jane', 'Murach', 'jane.murach@yahoo.com'),
(3, 'Allan', 'Sherwood', 'allan.sherwood@yahoo.com');

-- Create Addresses table
CREATE TABLE Addresses (
    address_id INT PRIMARY KEY,
    customer_id INT,
    line1 VARCHAR(100),
    city VARCHAR(50),
    state VARCHAR(50),
    zip_code VARCHAR(10),
    address_type VARCHAR(50),
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
);

INSERT INTO Addresses (address_id, customer_id, line1, city, state, zip_code, address_type)
VALUES
(1, 1, '123 Main St', 'Boston', 'MA', '02118', 'shipping'),
(2, 2, '456 Park Ave', 'New York', 'NY', '10001', 'billing'),
(3, 3, '789 Sunset Blvd', 'Los Angeles', 'CA', '90028', 'shipping');

-- Create Order_Items table
CREATE TABLE Order_Items (
    item_id INT PRIMARY KEY,
    product_id INT,
    item_price DECIMAL(10,2),
    discount_amount DECIMAL(10,2),
    quantity INT,
    FOREIGN KEY (product_id) REFERENCES Products(product_id)
);

INSERT INTO Order_Items (item_id, product_id, item_price, discount_amount, quantity)
VALUES
(1, 1, 999.99, 100.00, 1),
(2, 2, 1099.00, 164.85, 2),
(3, 3, 1999.99, 399.99, 1),
(4, 5, 659.00, 65.90, 2);
