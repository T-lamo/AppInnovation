class Cours:
    def __init__(self,section,grp,name,room,time) -> None:
        self.section = section
        self.grp = grp
        self.name = name
        self.room = room
        self.time = time

class SalleDisponibilite:
    def __init__(self,label,start_time,end_time,date) -> None:
        self.label = label
        self.start_time = start_time
        self.end_time = end_time
        self.date = date

class Prof:
    def __init__(self,name,phone,cours) -> None:
        self.name = name
        self.phone = phone
        self.cours = cours

        