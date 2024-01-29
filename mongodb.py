from pymongo import MongoClient
import os

client = MongoClient("")
# database and collection code goes here
db = client.account
#coll_incomes = db.incomes
#coll_expenses = db.expenses
coll_periods = db.periods
# find code goes here
# iterate code goes here
# Close the connection to MongoDB when you're done.
#client.close()

def insert_period(period, incomes, expenses, comment):
    data = {"period": period, "incomes": incomes, "expenses": expenses, "comment": comment}
    print(data)
    result = coll_periods.insert_many([data])
    if result:
        return {"result": result}


def fetch_all_periods():
    """Returns a dict of all periods"""
    cursor = coll_periods.find()
    periods = []
    for doc in cursor:
       periods.append(doc['period'])
    return periods
   


def get_period(period):
    result = coll_periods.find_one({"period": period})
    return result
