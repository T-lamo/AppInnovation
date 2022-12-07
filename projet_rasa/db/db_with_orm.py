from sqlalchemy import Column, Integer, String, MetaData, Table, select
from sqlalchemy.orm import declarative_base, Session
from sqlalchemy import create_engine
import sqlite3
from models.my_classes import Cours

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
engine = create_engine("sqlite:///schedule.db", echo=True, future=True)
conn = engine.connect()
metadata_obj = MetaData()

# create a table in database
course = Table(
    "course",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("section", String),
    Column("grp", String),
    Column("name", String),
    Column("room", String),
    Column("time", String),
)

# create all tables 
metadata_obj.create_all(engine)

# create objects and persist: insert data in the database
# with Session(engine) as session:
#     course_1 = Course(
#         section="M1",
#         grp="alternant",
#         name="math",
#         room="S2",
#         time="11:00"
#     )
#     course_2 = Course(
#         section="M2",
#         grp="classique",
#         name="ecom",
#         room="S6",
#         time="13:30"
#     )
#     # insert values to database
#     session.add_all([course_1,course_2])
#     session.commit()

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

    
# retrieve a course in the database
one_instance = Query_Db()
res = one_instance.retrieve_name_room('M1','classique','11:00')
print(res) 

