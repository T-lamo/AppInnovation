from operator import or_
from sqlalchemy import Column, Integer, String, MetaData, Table, TIME, select
from sqlalchemy.orm import declarative_base, Session
from sqlalchemy import create_engine
from sqlalchemy.orm import mapper

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

class Disponibilite(Base):
    __tablename__ = "disponibilite"

    id = Column(Integer, primary_key=True)
    label_salle = Column(String(100))
    start_time = Column(String(100))
    end_time = Column(String(100))
    date = Column(String(100))

class Prof(Base):
    __tablename__ = "prof"
    id = Column(Integer, primary_key=True)
    name =Column(String(100))
    phone = Column(String(100))
    cours= Column(String(100))

# create a database sqlite
conn = sqlite3.connect('db/schedule.db') 
cursor = conn.cursor()
conn.close()

# the factory engine will create new database connection
engine = create_engine("sqlite:///db/schedule.db", echo=True, future=True)
conn = engine.connect()
metadata_obj = MetaData()

# create a table "course" in database
course = Table(
    "course",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("section", String),
    Column("grp", String),
    Column("name", String),
    Column("room", String),
    Column("time", TIME),
)

# create a table "disponibilite" in database
course = Table(
    "disponibilite",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("label_salle", String),
    Column("start_time", String),
    Column("end_time", String),
    Column("date", String),
)  

course = Table(
    "prof",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("name", String),
    Column("phone", String),
    Column("cours", String)
)  
# )
# # create all tables 
metadata_obj.create_all(engine)

# create objects and persist: insert data course in the database
def create_some_courses():
    with Session(engine) as session:
        course_1 = Course(
            section="m2",
            grp="classique",
            name="Innovation",
            room="S2",
            time="11:45"
        )
        course_2 = Course(
            section="l2",
            grp="classique",
            name="sysembarque",
            room="S6",
            time="16:30"
        )
        course_3 = Course(
            section="m2",
            grp="alternant",
            name="ecom",
            room="S6",
            time="8:30"
        )
        course_4 = Course(
            section="m2",
            grp="classique",
            name="dataWarehouse",
            room="S6",
            time="10:00"
        )
        course_5 = Course(
            section="m2",
            grp="alternant",
            name="e-reputation",
            room="S6",
            time="14:30"
        )

    
        # insert values to database
        session.add_all([course_1,course_2,course_3,course_4,course_5])
        session.commit()

# create objects and persist: insert data disponibilite in the database
def create_some_dispos():
    with Session(engine) as session:
            dispo_1 = Disponibilite(
                label_salle ="C025",
                start_time="14:00",
                end_time="22:00",
                date="2023-01-16"
            )
            dispo_2 = Disponibilite(
                label_salle="C058",
                start_time="11:00",
                end_time="13:00",
                date="2022-12-16"
            )
            dispo_3 = Disponibilite(
                label_salle="Amphi Ada",
                start_time="11:00",
                end_time="13:00",
                date="2022-12-16"
            )
            dispo_4 = Disponibilite(
                label_salle="Amphi Blaise",
                start_time="9:00",
                end_time="10:00",
                date="2022-12-22"
            )
            dispo_5 = Disponibilite(
                label_salle="C137",
                start_time="11:00",
                end_time="13:00",
                date="2023-01-13"
            )
            #insert values to database
            session.add_all([dispo_1, dispo_2,dispo_3,dispo_4,dispo_5])
            session.commit()

def create_some_profs():
    with Session(engine) as session:
            prof1 = Prof(
                name ="amos",
                phone = "+33680596882",
                cours= "math"
            )
            prof2 = Prof(
                name ="bastien",
                phone = "+33680596882",
                cours= "reseau"
            )
            prof3 = Prof(
                name ="fara",
                phone = "+33680596882",
                cours= "securite"
            )
           
            #insert values to database
            session.add_all([prof1,prof2,prof3])
            session.commit()


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

    def create_html(stmts):
        # Creating the HTML file
        file_html = open("../../../NaoRasaASRProject/html/index.html", "w")
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
            halfday = datetime.strptime("23:00", "%H:%M").time()

        stmts = Session(engine).execute(select(Course)
        .where(Course.section == section_)
        .where(Course.grp == grp_)
        .where(Course.time > datetime.strptime(time_, "%H:%M").time())
        .where(Course.time < halfday)
        ).fetchall()
        print(len(stmts))
        res = ""
        # if response from db is not empty
        if (len(stmts) != 0):
            Query_Db.create_html(stmts)
            for stmt in stmts:
                res += "Tu as cours de " + stmt[0].name + " en salle " + stmt[0].room + " à " + stmt[0].time + " heure. \n"
        else:
            res += "Malheureusement tu n'as pas de cours. Va à la bibliothèque mon petit fénéant "
        
        return res

    def retrieve_salle_disponible(self,time_,date_):
        stmts = Session(engine).execute(select(Disponibilite)
        .where(Disponibilite.date == datetime.strptime(date_, "%Y-%m-%d").date())
        .where(or_(Disponibilite.start_time >= datetime.strptime(time_, "%H:%M").time(),
        (Disponibilite.end_time <= datetime.strptime(time_, "%H:%M").time())))
        
        ).fetchall()

        print(len(stmts))
        res = ""
        # if response from db is empty
        if (len(stmts) != 0):
            for stmt in stmts:
                res += "La salle " + stmt[0].label_salle + " est disponible " + stmt[0].date +" à "+str(time_)+" heure. \n"
        else:
            res += "Malheureusement aucune salle n'est disponible le "+str(date_)+" à "+str(time_)


        return res

    def retrieve_prof_phone_by_name(self,name_):
        print("name",name_)
        stmt = Session(engine).execute(select(Prof)
            .where(Prof.name == name_)).scalar_one()

        print("stmt value",stmt)
        
        # if response from db is empty
        res =str(stmt.phone)
        print("message",res)


        return res

    def retrieve_prof_name_by_course(self,cours_):
        stmt = Session(engine).execute(select(Prof)
        .where(Prof.cours == cours_)).fetchone()

        print(len(stmt))
        res = ""
       
        # if response from db is empty
        if (len(stmt) != 0):
            # Query_Db.create_html(stmts)
            res =str(stmt.name_)
        else:
            res = "erreur"

# create courses in db
#create_some_courses()
#create dispos in db   
#create_some_dispos()
# retrieve a course in the database
# one_instance = Query_Db()
#create_some_profs()
# res = one_instance.retrieve_schedule_halfday('M2','classique','13:00')
# print(res) 

