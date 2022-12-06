from db_with_orm import Schedule
from models.cours_file import Cours

class Query_db:
    def create_shedule(self,cours):
        # fill the schedule
        print("create here")
        schedule_1 = Schedule({'section':cours.section,'grp':cours.grp,'name':cours.name,'room':cours.room,'time':cours.time})
        schedule_1.save()

    def retrieve_all_courses(self):
        # see all objects
        res = Schedule.objects.all()
        print("See all courses:")
        print(res)

    def retrieve_record_name_room(self,section,grp,time):
        query = 'select * from schedule where section=="'+section+'" and grp=="'+grp+'" and time =="'+time+'";' 
        obj = Schedule.objects.backend.select(query)
        print("Retrieve: ",section," - ",grp, " - ",time)
        for row in obj:
            get_id = row[0]
            get_section = row[1]
            get_grp = row[2]
            get_name_course = row[3]
            get_room = row[4]
            get_time = row[5]
            # print(row[0])
            # print(row[1])
            # print(row[2])
            # print(row[3])
            # print(row[4])
            # print(row[5])
        return {'id':get_id,'section':get_section,'grp':get_grp,'name':get_name_course,'room':get_room,'time':get_time}

    def disconnect_to_backend(self):
        Schedule.objects.backend.close()

one_instance = Query_db()
# new_cours = Cours('M2','classique','ecom','S6','13:30')
# one_instance.create_shedule(new_cours)
# one_instance.retrieve_all_courses()
one_instance.retrieve_record_name_room('M2','classique','13:30')

