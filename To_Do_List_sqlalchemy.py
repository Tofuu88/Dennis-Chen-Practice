from sqlalchemy import create_engine, and_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from datetime import datetime, date, timedelta
from sqlalchemy.orm import sessionmaker
engine = create_engine('sqlite:///todo.db?check_same_thread=False')  # this creates a database file
Base = declarative_base()  # All model classes should inherit from the DeclarativeMeta class that is returned by declarative_base():
# Base inherit from the declarativeMeta class

class Table(Base):  # Table is the name of the model class
    __tablename__ = "task"  # __Tablename__ specifies the table name in the database
    id = Column(Integer, primary_key=True)  #id is the primary key
    task = Column(String, default="default_value")  
    deadline = Column(Date, default=datetime.today())  #default is a datetime object

    def __repr__(self):
        return self.task + "."  # repr returns a string field, each row in ORM is an object of the class

Base.metadata.create_all(engine)  # this creates a table in the database by generating SQL queries based upon the model description (__Tablename__)\

def main():
    while True:
        inp = input("1) Today's tasks\n2) Week's tasks\n3) All tasks\n4) Missed tasks\n5) Add task\n6) Delete task\n0) Exit\n", )
        print(" ")
        if inp == "1":  # query the database
            Session = sessionmaker(bind=engine)
            session = Session()  # session object
            info = session.query(Table).all()
            session.commit()
            today = datetime.today().date()
            if len(info) == 0:       
                print("Today", today.strftime("%d %b") + ":")
                print("Nothing to do!")
            else:
                print("Today", today.strftime("%d %b") + ":")
                for item in info:
                    print(str(item.id) + ".", item)
            print(" ")

        elif inp == "2":
            today = datetime.today().date()
            Session = sessionmaker(bind=engine)
            session = Session()  # session object
            for i in range(9):
                next_day = today + timedelta(days=i)
                info = session.query(Table).filter(Table.deadline == next_day).all()
                print(next_day.strftime("%A %d %b"), ":", sep="")
                if not info:
                    print("Nothing to do!")
                    print(" ")
                else:
                    counter = 1
                    for item in info:
                        print(str(counter) + ".", item)
                        counter += 1
            session.commit()
            
        elif inp == "3":
            Session = sessionmaker(bind=engine)
            session = Session()  # session object
            info = session.query(Table).order_by(Table.deadline).all()
            session.commit()
            counter = 1
            for item in info:
                print(str(counter) + ".", item.task + ".", item.deadline.strftime("%d %b"))
                counter += 1
            print(" ")
        
        elif inp == "4":
            Session = sessionmaker(bind=engine)
            session = Session()  # session object
            today = datetime.today().date()
            missed_tasks = session.query(Table).filter(Table.deadline < today).all()
            counter = 1
            print("Missed tasks:")
            if len(missed_tasks) == 0:
                print("Nothing is missed")
            else:
                for item in missed_tasks:
                    print(str(counter) + ".", item, item.deadline.strftime("%d %b"))
                    counter += 1
                print(" ")
            session.commit()

        elif inp == "5":
            string_inp = input("Enter Task\n", )
            deadline_inp = input("Enter deadline\n", )
            Session = sessionmaker(bind=engine)
            session = Session()  # session object
            new_row = Table()
            new_row.task = string_inp
            new_row.deadline = datetime.strptime(deadline_inp, "%Y-%m-%d")
            session.add(new_row)
            session.commit()
        
            print("The task has been added!")
            print(" ")

        elif inp == "6":
            Session = sessionmaker(bind=engine)
            session = Session()  # session object
            today = datetime.today().date()
            missed_tasks = session.query(Table).order_by(Table.deadline).all()
            del_num = int(input("Choose the number of the task you want to delete:", ))
            counter = 1
            print("Missed tasks:")
            if len(list(missed_tasks)) != 0:
                for item in missed_tasks:
                    print(str(item.id) + ".", item)
                    counter += 1
                session.delete(missed_tasks[del_num - 1])
                session.commit()
            else:
                print("Nothing to delete!")
            print("The task has been deleted!")
        elif inp == "0":
            print("Bye!")
            break

if __name__ == "__main__":
    main()