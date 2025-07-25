-- 1. Products Table: Ordered by list price descending
SELECT product_code, product_name, list_price, discount_percent
FROM Products
ORDER BY list_price DESC;

-- 2. Customers Table: Full name + filtering last names M–Z
SELECT first_name, last_name,
       CONCAT(last_name, ', ', first_name) AS full_name
FROM Customers
WHERE last_name >= 'M'
ORDER BY last_name ASC;

-- 3. Products Table: Price between 500 and 2000, ordered by date_added descending
SELECT product_name, list_price, date_added
FROM Products
WHERE list_price > 500 AND list_price < 2000
ORDER BY date_added DESC;

-- 4. Order_Items Table: Calculated totals
SELECT item_id,
       item_price,
       discount_amount,
       quantity,
       item_price * quantity AS price_total,
       discount_amount * quantity AS discount_total,
       (item_price - discount_amount) * quantity AS item_total
FROM Order_Items
WHERE (item_price - discount_amount) * quantity > 500
ORDER BY item_total DESC;

-- 5. Categories + Products Join
SELECT category_name, product_name, list_price
FROM Categories
JOIN Products ON Categories.category_id = Products.category_id
ORDER BY category_name ASC, product_name ASC;

-- 6. Customers + Addresses Join: Email filter
SELECT first_name, last_name, line1, city, state, zip_code
FROM Customers
JOIN Addresses ON Customers.customer_id = Addresses.customer_id
WHERE email_address = 'allan.sherwood@yahoo.com'
ORDER BY zip_code ASC;

-- 7. Customers + Addresses Join: Shipping addresses only
SELECT first_name, last_name, line1, city, state, zip_code
FROM Customers
JOIN Addresses ON Customers.customer_id = Addresses.customer_id
WHERE address_type = 'shipping'
ORDER BY zip_code ASC;
