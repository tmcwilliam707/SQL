CREATE DATABASE test_db;

-- Connect to the database
\c test_db

-- Create the table
CREATE TABLE user_fundraiser_summary (
    user_id INT,
    donation_date TIMESTAMP,
    total_amount DECIMAL
);

-- Insert sample data
INSERT INTO user_fundraiser_summary (user_id, donation_date, total_amount) VALUES
(1, now() - INTERVAL '10 days', 50),
(1, now() - INTERVAL '20 days', 60),
(2, now() - INTERVAL '5 days', 30),
(2, now() - INTERVAL '15 days', 80),
(3, now() - INTERVAL '25 days', 40),
(3, now() - INTERVAL '35 days', 70),
(4, now() - INTERVAL '2 days', 120);

-- Test the query
SELECT user_id
FROM user_fundraiser_summary
WHERE donation_date BETWEEN now() - '30 DAYS'::interval
GROUP BY user_id
HAVING SUM(total_amount) > 100
ORDER BY user_id;