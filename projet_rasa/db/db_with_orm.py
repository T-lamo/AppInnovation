from sqlalchemy import Column, Integer, String, MetaData, Table, TIME, select
from sqlalchemy.orm import declarative_base, Session
from sqlalchemy import create_engine
from sqlalchemy import func

import sqlite3
from db.models.my_classes import Cours
from datetime import datetime

Base = declarative_base()

class Course(Base):
    __tablename__ = "course"

    id = Column(Integer, primary_key=True)
    section = Column(String(100))
    grp = Column(String(100))
    name = Column(String(100))
    room = Column(String(100))
    time = Column(String(100))

# create a database sqlite
conn = sqlite3.connect('schedule.db') 
cursor = conn.cursor()
conn.close()

# the factory engine will create new database connection
engine = create_engine("sqlite:///db/schedule.db", echo=True, future=True)
conn = engine.connect()
metadata_obj = MetaData()

# create a table in database
# course = Table(
#     "course",
#     metadata_obj,
#     Column("id", Integer, primary_key=True),
#     Column("section", String),
#     Column("grp", String),
#     Column("name", String),
#     Column("room", String),
#     Column("time", TIME),
# )

# # create all tables 
metadata_obj.create_all(engine)

# create objects and persist: insert data in the database
# with Session(engine) as session:
    # course_1 = Course(
    #     section="M2",
    #     grp="classique",
    #     name="Innovation",
    #     room="S2",
    #     time="11:45"
    # )
    # course_2 = Course(
    #     section="L2",
    #     grp="3",
    #     name="sysembarque",
    #     room="S6",
    #     time="16:30"
    # )
    # course_3 = Course(
    #     section="M2",
    #     grp="classique",
    #     name="ecom",
    #     room="S6",
    #     time="8:30"
    # )
    # course_4 = Course(
    #     section="M2",
    #     grp="classique",
    #     name="dataWarehouse",
    #     room="S6",
    #     time="10:00"
    # )
    # course_5 = Course(
    #     section="M2",
    #     grp="classique",
    #     name="e-reputation",
    #     room="S6",
    #     time="14:30"
    # )
    # insert values to database
    # session.add_all([course_1])
    # session.commit()

class Query_Db:
    '''
        This class is intended to query the database
    '''
    def __init__(self) -> None:
        self.session = Session(engine)
    
    def insert_new_course(self,cours:Cours):
        new_course = Course(
            section = cours.section,
            grp = cours.grp,
            name = cours.name,
            room = cours.room,
            time = cours.time
        )
        self.session.add(new_course)
        self.session.close()

    # query database
    def retrieve_name_room(self,section_,grp_,time_) -> String:
        try:
            stmt = self.session.execute(select(Course)
            .where(Course.section == section_)
            .where(Course.grp == grp_)
            .where(Course.time == time_)).scalar_one()

            return "You have '"+str(stmt.name)+"' class in '"+str(stmt.room)+" room"
        
        except Exception:
            return "Hopefully you don't have course at this hour"
    
    def create_html(stmts):
        # Creating the HTML file
        file_html = open("demo.html", "w")
        # Adding the input data to the HTML file
        file_html.write('''<html>
        <head>
        <title>schedule</title>
        <style>
        table,th,td{border:1px solid #cccccc}
        .centered {
            position: fixed;
            top: 50%;
            left: 50%;
            margin-top: -50px;
            margin-left: -100px;
            background-color: white;
            }
        </style>
        </head> 
        <body style="background-color:aquamarine;">
            <table class="centered">
                <tr>
                    <th>Nom</th>
                    <th>Salle</th>
                    <th>Heure</th>
                </tr>''')
        for stmt in stmts:
            file_html.write('''
                <tr>
                    <td>'''+stmt[0].name+'''</td>
                    <td>'''+stmt[0].room+'''</td>
                    <td>'''+stmt[0].time+'''</td>
                </tr>''')
        
        file_html.write('''    </table>
        </body>
        </html>''')
        # Saving the data into the HTML file
        file_html.close()

    def retrieve_schedule_halfday(self,section_,grp_,time_) -> String:
        if("cla" in grp_):
            grp_ = "classique"
        if("alt" in grp_):
            grp_ = "alternant"

        print(datetime.strptime(time_, "%H:%M"))
        # try:
        halfday = datetime.strptime("12:00", "%H:%M").time()
        if(datetime.strptime(time_, "%H:%M").time() > datetime.strptime("12:00", "%H:%M").time()):
            halfday = datetime.strptime("20:00", "%H:%M").time()
        stmts = Session(engine).execute(select(Course)
        .where(Course.section == section_)
        .where(Course.grp == grp_)
        .where(Course.time > datetime.strptime(time_, "%H:%M").time())
        .where(Course.time < halfday)).fetchall()
        print(len(stmts))

        Query_Db.create_html(stmts)

        res = ""
        for stmt in stmts:
            res += "Tu as cours de " + stmt[0].name + " en salle " + stmt[0].room + " à " + stmt[0].time + " heure. \n"

        # print(stmt.)


        return res
    
        # except Exception:
        #     return section_ + " " + grp_ + " " + time_

    
    

    
# retrieve a course in the database
# one_instance = Query_Db()
# res = one_instance.retrieve_schedule_halfday('M2','classique','13:00')
# print(res) 

