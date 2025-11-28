# -*- coding: utf-8 -*-
"""
Created on Thu Nov 27 17:09:09 2025

@author: odoheb
"""

import time
import json

class BudgetTracker(object):
    def __init__(self):
        self.income = list()
        self.expense = list()
    
    def add_income(self):
        category = ''
        while True:
            i = input("Income-Type, Value ==> ").strip().split(',', 1)
            category = i[0].strip().lower()
            if category == 'stop' or category == 'end':
                break 
            formatted = dict(Type='income', amount= float(i[1]), category= category, time= time.ctime())
            self.income.append(formatted)
        return self.income
    def add_expense(self):
       category = ''
       while True:
           i = input("Expense-Type, Value ==> ").strip().split(',', 1)
           category = i[0].strip().lower()
           if category == 'stop' or category == 'end':
               break 
           formatted = dict(Type='expense', amount= float(i[1]), category= category, time= time.ctime())
           self.expense.append(formatted)
       return self.expense
   
    def total_income(self):
        total_income = 0
        for i in self.income:
            total_income += float(i['amount'])
        return total_income
    def total_expense(self):
        total_expense = 0
        for i in self.expense:
            total_expense += float(i['amount'])
        return total_expense
    
    def net_balance(self):
        return self.total_income() - self.total_expense()
    
    def produce_summary(self):
        income = self.total_income()
        expenses = self.total_expense()
        net = income - expenses
    
        print("\n==== Budget Summary ====\n")
        print(f"Total Income:     ${income:8.2f}")
        print(f"Total Expenses:   ${expenses:8.2f}")
        print("--------------------------------")
        print(f"Net Balance:      ${net:8.2f}\n")
    
    def category_spending(self):
        combined = self.income + self.expense
        while True:
            pick = input("Enter a category ==> ").strip().lower()
            if pick.lower() == 'stop' or pick.lower() == 'end':
                break
            print("\n==== Category Spending: {} ====\n".format(pick))
            for i in combined:
                if i['category'] == pick:
                    print("Amount: ${}     {}".format(i['amount'], i['time']))
                    
    def save(self):
        with open("data.txt", "w") as f:
            for i in self.income:
                f.write(json.dumps(i) + '\n')
            for i in self.expense:
                f.write(json.dumps(i) + '\n')
                
                
    def load(self):
        try:
            with open("data.txt", "r") as f:
                for item in f:
                    entry = json.loads(item.strip())
                    
                    if entry['Type'] == 'income':
                        self.income.append(entry)
                    else:
                        self.expense.append(entry)
        except FileNotFoundError:
            pass
            
                    
        
        
        
        
if __name__ == "__main__":
    tracker = BudgetTracker()
    tracker.load()
    while True:
        choice = input("1. Add income \
                       \n2. Add expense \
                       \n3. View summary \
                       \n4. View category spending \
                       \n5. Save and quit \
                       \nEnter here ==>\
                       ").strip()
        if choice == '1':
            tracker.add_income()
        elif choice == '2':
            tracker.add_expense()
        elif choice == '3':
            tracker.produce_summary()
        elif choice == '4':
            tracker.category_spending()
        elif choice =='5':
            tracker.save()
            break

        
    
            
        
            
            
            
            
            
            
            
            
            
            