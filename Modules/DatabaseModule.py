
import pymongo

class DatabaseModule():
    def __init__(self) -> None:
        self.password = "oloFt4PSQND4MY2c"
        self.mycluster = None
        self.mydb = None
        self.collection = None
        

    def connect_db(self):
        self.mycluster = pymongo.MongoClient("mongodb+srv://sevdayucedagg:"+ self.password +"@cluster0.5cb1udp.mongodb.net/")
        self.mydb = self.mycluster["mydatabase"]

    def get_databases(self):
        if self.mycluster:
            print(self.mycluster.list_database_names())
        else:
            print("Database didnt create")

    def create_project(self, project_name, date, company_name, keywords):
        data = [
                {"project name" : project_name, "date" : date, "company name": company_name, "Keywords":keywords},
            ]
        db.collection.insert_many(data)

    def create_db(self,db_name):
        self.collection = self.mydb[db_name]



# db = DatabaseModule()
# db.connect_db()
# db.get_databases()
# db.create_db("projects")

