import orm_sqlite

class Schedule(orm_sqlite.Model):
    id = orm_sqlite.IntegerField(primary_key=True)
    section = orm_sqlite.StringField()
    grp = orm_sqlite.StringField()
    name = orm_sqlite.StringField()
    room = orm_sqlite.StringField()
    time = orm_sqlite.StringField()

# create a database
db = orm_sqlite.Database('scehdule.db')
# set db to backend
Schedule.objects.backend = db
