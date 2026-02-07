SmartJoin – Data Utility Tool for Auto Join Discovery & Performance Improvement

Project Overview
SmartJoin is a lightweight Python-based data utility tool designed to automatically discover optimized join relationships between database tables and provide performance improvement suggestions.
The tool scans database schemas, identifies common ID-based relationships, removes duplicate joins, and recommends indexing and efficient join strategies to improve query performance.
This project was developed as part of a Campus Innovation Case Study focusing on improving database performance through automated join discovery.


 Objectives
 Automate database schema analysis
 Discover optimized join relationships
 Reduce manual database exploration
 Improve query performance using optimized join logic
 Provide performance suggestions such as indexing and INNER JOIN usage

 Technologies Used
 Python
 SQLite
 SQL Queries (for schema extraction)
 VS Code

 Project Structure
 SmartJoin_Project/
│
├── create_db.py # Script to create sample database
├── auto_join_tool.py # Main SmartJoin automation script
├── company.db # SQLite sample database
└── README.md # Project documentation


 Database Schema
 Tables Used:
 customers
 orders
 payments
 products

Relationships:
customers.customer_id → orders.customer_id
orders.order_id → payments.order_id

 Workflow
1. Connect to SQLite database
2. Extract table and column metadata
3. Compare column names across tables
4. Identify optimized ID-based joins
5. Remove duplicate join suggestions
6. Generate performance optimization recommendations

 How to Run the Project
 Step 1 – Create Database
 Step 2 – Run Auto Join Discovery Tool

 Sample Output
 Smart Join Suggestions
 customers.customer_id = orders.customer_id
 orders.order_id = payments.order_id

 Performance Suggestions
 Add index on join columns
 Use INNER JOIN for optimized query performance

 Key Features
 Automatic schema scanning
 Optimized ID-based join detection
 Duplicate join removal
 Performance improvement recommendations
 Lightweight automation script

 Future Enhancements
 Web-based dashboard
 AI-powered relationship prediction
 ER diagram auto-generation
 Advanced query optimization engine

 Author
Shibilasri G
Campus Innovation Case Study Project


