class Cours:
    def __init__(self,section,grp,name,room,time) -> None:
        self.section = section
        self.grp = grp
        self.name = name
        self.room = room
        self.time = time
    
    def create_cours(self,section,grp,name,room,time):
        self.section = section
        self.grp = grp
        self.name = name
        self.room = room
        self.time = time