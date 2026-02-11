from sqlalchemy import create_engine,Column,Integer,String,ForeignKey,text,Float,func
from sqlalchemy.orm import declarative_base,relationship,sessionmaker

engine = create_engine("sqlite:///fintrack.db")

Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()

class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer,primary_key=True)
    name = Column(String)
    expenses = relationship("Expense",back_populates="category")

class Expense(Base):
    __tablename__ = "expenses"
    id = Column(Integer,primary_key=True)
    title = Column(String)
    amount = Column(Float)
    date = Column(String)
    category_is = Column(Integer,ForeignKey("categories.id"))
    category = relationship("Category",back_populates="expenses")

class Subscriptions(Base):
    __tablename__ = "subscriptions"
    id = Column(Integer,primary_key=True)
    name = Column(String)
    amount = Column(Float)
    next_date = Column(String)

class Budget(Base):
    __tablename__ = "budgets"
    id = Column(Integer,primary_key=True)
    month = Column(String)
    limit_amount = Column(Integer)

Base.metadata.create_all(engine)

def add_category():
    name = input("Category name: ")
    session.add(Category(name=name))
    session.commit()
    print("Catgory Added")


def add_expense():
    title = input("Expense title: ")
    amount = float(input("Amount: "))
    date = input("date: ")
    category_id = int(input("Category ID: "))
    session.add(Expense(title = title, amount = amount, date = date, category_id = category_id))
    session.commit()
    print("Expense Added ")

def update_expense():
    eid = int(input("Expense ID: "))
    exp = session.query(Expense).filter(Expense.id == eid).first()
    if exp :
        exp.title = input("new title: ")
        exp.amount = float(input("New Amount:  "))
        session.commit()
        print("Expense Deleted ")
    else: 
        print("Not Found ")

def delete_expense():
    eid = int(input("Expense ID: "))
    exp = session.query(Expense).filter(Expense.id == eid).first()

    if exp:
        session.delete(exp)
        session.commit()
        print("Expense deleted")
    else:
        print("Not found")

def search_by_date():
    d = input("Enter Date: ")
    rows = session.query(Expense).filter(Expense.date == d).all()
    for r in rows:
        print(r.title, "-", r.amount, "-",r.category.name)

def add_subscription():
    name = input("Subscription name: ")
    amount = float(input("Amount: "))
    next_date = input("Next payment date: ")
    session.add(Subscriptions(name=name, amount=amount, next_date=next_date))
    session.commit()
    print("Subscription added")

def show_subscriptions():
    subs = session.query(Subscriptions).all()
    for s in subs:
        print(s.id, s.name, s.amount, s.next_date)


def category_report():
    sql = """SELECT c.name, SUM(e.amount)
    FROM categories c
    JOIN expenses e
    ON c.id = e.category_id
    GROUP BY c.name;"""

    result = session.execute(text(sql))

    print("Category Expense Report")
    for row in result:
        print(row[0], "-", row[1])


def set_budget():
    month = input("Month (YYYY-MM): ")
    limit_amount = float(input("Budget limit: "))

    session.add(Budget(month=month, limit_amount=limit_amount))
    session.commit()

    print("Budget set")


def budget_alert():
    month = input("Month (YYYY-MM): ")

    total = session.execute(
        text("SELECT SUM(amount) FROM expenses WHERE date LIKE :m"),
        {"m": f"{month}%"}
    ).scalar() or 0

    b = session.query(Budget).filter(Budget.month == month).first()

    if b and total > b.limit_amount:
        print("Budget exceeded")
        print("Spent:", total, "Limit:", b.limit_amount)
    else:
        print("Within budget")
        print("Spent:", total)


while True:
    print("""
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
""")

    choice = input("Choose: ")

    if choice == "1":
        add_category()
    elif choice == "2":
        add_expense()
    elif choice == "3":
        update_expense()
    elif choice == "4":
        delete_expense()
    elif choice == "5":
        search_by_date()
    elif choice == "6":
        category_report()
    elif choice == "7":
        add_subscription()
    elif choice == "8":
        show_subscriptions()
    elif choice == "9":
        set_budget()
    elif choice == "10":
        budget_alert()
    elif choice == "11":
        break
    else:
        print("Invalid choice")
