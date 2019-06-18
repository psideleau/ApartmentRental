import sqlite3

from customer_check import Customer_check



def newone():
        found = 0
        while found == 0:
            Name = input("Please enter your Name: ")
            Password = input("Please enter your Password: ")
            with sqlite3.connect("test.db") as db:
                cusror = db.cursor()
                finduser = ("select * FROM Customer WHERE Name = ?")
                cusror.execute(finduser, [(Name)])
            if cusror.fetchall():
                with sqlite3.connect("test.db") as db:
                    cusror = db.cursor()
                    findpass = ("select * from Customer where Password = ?")
                    cusror.execute(findpass, [(Password)])
                    if cusror.fetchall():
                        print("Welcome to our program")
                        choice = input("enter 1 to show the available units: ")
                        Customer_check1 = Customer_check()
                        Customer_check1.Main(choice)

            else:
                print("Error")
                



if __name__ == '__main__':
    newone()

 
