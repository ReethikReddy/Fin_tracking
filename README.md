💰 FinTrack Pro — CLI Finance Manager

FinTrack Pro is a Command Line Personal Finance Manager built with Python, SQLite, and SQLAlchemy ORM. It helps users manage expenses, categories, subscriptions, and monthly budgets with analytics support using raw SQL queries.

This project is designed to demonstrate ORM usage, CRUD operations, database design, and reporting queries — making it ideal for learning and interview showcase.

🚀 Features

✅ Add Categories

✅ Add / Update / Delete Expenses

✅ Search Expenses by Date

✅ Category-wise Expense Report

✅ Subscription Tracking

✅ Monthly Budget Limits

✅ Budget Exceed Alerts

✅ Raw SQL Analytics Queries

✅ Persistent SQLite Storage

✅ Menu-driven CLI Interface

🧱 Tech Stack

Python

SQLite

SQLAlchemy ORM

Raw SQL Queries

CLI (Command Line Interface)

🗄️ Database Schema
Tables

categories

id (PK)
name
expenses

id (PK)
title
amount
date
category_id (FK → categories.id)


subscriptions

id (PK)
name
amount
next_date


budgets

id (PK)
month
limit_amount

Relationships
Category (1) ──── (N) Expenses

📦 Installation
1️⃣ Clone Repository
git clone https://github.com/yourusername/fintrack-pro.git
cd fintrack-pro

2️⃣ Install Dependencies
pip install sqlalchemy


(SQLite comes bundled with Python — no extra install needed.)

▶️ Run the Application
python main.py

🖥️ CLI Menu
===== FINTRACK =====
1. Add Category
2. Add Expense
3. Update Expense
4. Delete Expense
5. Search Expense by Date
6. Category Expense Report
7. Add Subscription
8. Show Subscriptions
9. Set Monthly Budget
10. Budget Alert
11. Exit

📊 Example Analytics Query Used

Category-wise expense totals using raw SQL:

SELECT c.name, SUM(e.amount)
FROM categories c
JOIN expenses e
ON c.id = e.category_id
GROUP BY c.name;

🎯 Learning Outcomes

This project demonstrates:

ORM modeling with SQLAlchemy

Database relationships

CRUD operations

Raw SQL joins & aggregation

Modular Python design

CLI application structure

Budget tracking logic

🔮 Future Enhancements

📤 CSV export

🌐 Flask / Web UI

👤 User authentication

📈 Charts & dashboards

📅 Auto recurring subscriptions

🔔 Reminder alerts


