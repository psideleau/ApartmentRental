import sqlite3
from customer_check import Customer_check



def new():
        found = 0
        while found == 0:
            Name = input("Please enter Employee Name: ")
            Password = input("Please enter your Password: ")
            with sqlite3.connect("test.db") as db:
                cusror = db.cursor()
                finduser = ("select * FROM Employee WHERE Name = ? AND Password = ?")
                cusror.execute(finduser, [(Name),(Password)])
                if cusror.fetchall():
                 print("Welcome ", Name)
                 just = 1
                 Customer_check2 = Customer_check()
                 Customer_check2.look(just)
                else:
                    print("you can not access the system!!!")
                    break
                break
            break











if __name__ == '__main__':
    new()
