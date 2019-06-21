import sqlite3
from customer_check import Customer_check



def newone():
        found = 0
        while found == 0:
            Name = input("Please enter your Name: ")
            Password = input("Please enter your Password: ")
            with sqlite3.connect("test.db") as db:
                cusror = db.cursor()
                finduser = ("select * FROM Customer WHERE Name = ? AND Password = ?")
                cusror.execute(finduser, [(Name),(Password)])
            if cusror.fetchall():
                print("Welcome to our System", Name)
                choice = input("enter 1 to show the available units: ")
                Customer_check1 = Customer_check()
                Customer_check1.Main(choice)
            else:
                print("error!!!!")
                break
        break 
            






if __name__ == '__main__':
    newone()

