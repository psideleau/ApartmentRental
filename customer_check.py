import sqlite3

class Customer_check:

    def Main(self, choice):
        db = sqlite3.connect("test.db")
        db.row_factory = sqlite3.Row
        db.execute("create table if not exists Employee(Name text, EmployeeID int, DOB text, Position text, Password int)")
        db.execute(
            "create table if not exists Customer(Name text, NationalID int, DOB text, PhoneNUM int, Password int)")
        db.execute(
            "create table if not exists Unit(UniteID text, RoomNUM int, BathNUM int, Price float, UniState text)")
        db.execute("create table if not exists Reservation(NationalID int, UniteID text) ")
        db.execute("insert into Employee (Name,EmployeeID,DOB,Position,Password) values (? , ? , ? , ?, ?)",
                   ("Salem", 1234, "1/1/1990", "Owner", 999))
        db.execute("insert into Employee (Name,EmployeeID,DOB,Position,Password) values (? , ? , ? , ?, ?)",
                   ("Abdullah", 4321, "1/1/1991", "Supervisor", 888))
        db.execute("insert into Customer (Name,NationalID,DOB,PhoneNUM,Password) values (? , ? , ? , ?, ?)",
                   ("Sara", 123, "1/1/1980", 500500, 111))
        db.execute("insert into Customer (Name,NationalID,DOB,PhoneNUM,Password) values (? , ? , ? , ?, ?)",
                   ("Mathew", 456, "1/1/1985", 503503, 222))
        db.execute("insert into Customer (Name,NationalID,DOB,PhoneNUM,Password) values (? , ? , ? , ?, ?)",
                   ("John", 789, "1/1/1988", 509509, 333))
        db.execute("insert into Customer (Name,NationalID,DOB,PhoneNUM,Password) values (? , ? , ? , ?, ?)",
                   ("Tony", 101, "1/1/1995", 908908, 444))
        db.execute("insert into Customer (Name,NationalID,DOB,PhoneNUM,Password) values (? , ? , ? , ?, ?)",
                   ("Flavia", 199, "1/1/1996", 907907, 555))
        db.execute("insert into Unit (UniteID,RoomNUM,BathNUM,Price,UniState) values (? , ? , ? , ? , ?)",
                   ("1S", 2, 1, 1200, "Reserved"))
        db.execute("insert into Unit (UniteID,RoomNUM,BathNUM,Price,UniState) values (? , ? , ? , ? , ?)",
                   ("2R", 1, 1, 800, "Available"))
        db.execute("insert into Unit (UniteID,RoomNUM,BathNUM,Price,UniState) values (? , ? , ? , ? , ?)",
                   ("3V", 3, 3, 2000, "Reserved"))
        db.execute("insert into Unit (UniteID,RoomNUM,BathNUM,Price,UniState) values (? , ? , ? , ? , ?)",
                   ("4T", 1, 1, 800, "Available"))
        db.execute("insert into Unit (UniteID,RoomNUM,BathNUM,Price,UniState) values (? , ? , ? , ? , ?)",
                   ("5B", 2, 2, 1300, "Reserved"))
        db.execute("insert into Reservation (NationalID,UniteID) values (? , ?)", (123, "1S"))
        db.execute("insert into Reservation (NationalID,UniteID) values (? , ?)", (456, "3V"))
        db.execute("insert into Reservation (NationalID,UniteID) values (? , ?)", (789, "5B"))
        # db.commit()




        if choice == "1":
            cusror = db.execute("select * from Unit where UniState= 'Available' ")
            for row in cusror:
                print(
                        "Unite ID:{}, Rooms:{}, Baths:{}, Price:{}, Unite State:{} ".format(row["UniteID"], row["RoomNUM"],
                                                                                        row["BathNUM"], row["Price"],
                                                                                        row["UniState"]))

        else:
            print("wrong choice")



    def look(self, just):
        while just == 1:
            NationalID = input ("please enter national id:")
            with sqlite3.connect("test.db") as db :
                cusror = db.cursor()
                findit = ("select * from Reservation WHERE NationalID = ?")
                cusror.execute(findit, [(NationalID)])
                print(cusror.fetchall())
                break
                
