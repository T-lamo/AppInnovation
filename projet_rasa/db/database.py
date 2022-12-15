from asyncio import open_connection
import psycopg2


class DatabaseSingletonMeta(type):
    """
    The Singleton class can be implemented in different ways in Python. Some
    possible methods include: base class, decorator, metaclass. We will use the
    metaclass because it is best suited for this purpose.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Database(metaclass=DatabaseSingletonMeta):

    def __init__(self):
        self.db = "rasa_demo_db"
        self.user = 'postgres'
        self.password = 'admin'
        self.port = '5432'
        self.host = '127.0.0.1'

        

        data = {
            'name': "agenda",
            'columns':"section, grp, name, room, time",
            'values': ('M1', 'classique', 'outils pour apprentis', 'S4', '13:00')
        }
        
        self.insert(data)

    def open_connexion(self):
        # establishing the connection
        return psycopg2.connect(
            database=self.db, user=self.user, password=self.password, host=self.host, port=self.port
        )

    def select(self):
        conn = self.open_connexion()
        cursor = conn.cursor()
        # Executing an MYSQL function using the execute() method
        cursor.execute("select * from agenda")
        # Fetch a single row using fetchone() method.
        res_tuple = cursor.fetchall()
        conn.close()
        return res_tuple
        # Closing the connection
        
    def insert(self,data):
        conn = self.open_connexion()
        #Setting auto commit false
        conn.autocommit = True
        #Creating a cursor object using the cursor() method
        cursor = conn.cursor()
        query = '''INSERT INTO {} ({}) VALUES {};'''.format(data['name'],data['columns'],data['values'])
        # Preparing SQL queries to INSERT a record into the database.
        print(query)
        cursor.execute(query)
        # Commit your changes in the database
        conn.commit()
        conn.close()
    
    def delet_values(self):
        conn = self.open_connexion()
        #Setting auto commit false
        conn.autocommit = True
        #Creating a cursor object using the cursor() method
        cursor = conn.cursor()
        query = "DELETE FROM agenda"
        # Preparing SQL queries to INSERT a record into the database.
        print(query)
        cursor.execute(query)
        # Commit your changes in the database
        conn.commit()
        conn.close()

    def get_schedule(self,item,data):
        if(item[0]==data[0] and item[1]==data[1]):
            return True
        else: 
            return False


if __name__ == "__main__":
    # The client code.
    print(Database().select())
    def convert_to_dict(item):
        return {"section":item[0], "group":item[1], "subject":item[2], "class": item[3], "time": item[4]}
    result=list(filter(lambda item:Database().get_schedule(item, ("M1","alternant")),Database().select()))
    print(list(map(convert_to_dict, result)))
    print(result)
    Database().delet_values()
    data = [{
            'name': "agenda",
            'columns':"section, grp, name, room, time",
            'values': ('M2', 'alternant', 'Middleware', 'S7', '8:30')
        },
        {
            'name': "agenda",
            'columns':"section, grp, name, room, time",
            'values': ('M2', 'alternant', 'appli inovation', 'S8', '10:00')
        },
        {
            'name': "agenda",
            'columns':"section, grp, name, room, time",
            'values': ('M2', 'alternant', 'data warehouse', 'S3', '13:00')
        },
        
        
        ]
    for i in range(len(data)):
        Database().insert(data=data[i])
    print("---------------------")
    print(Database().select())

   
