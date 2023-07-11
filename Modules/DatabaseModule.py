
import pymongo
from Modules.Collections.ProjectsCollection import ProjectsCollection


class DatabaseModule():
    def __init__(self) -> None:
        self.password = "oloFt4PSQND4MY2c"
        self.mycluster = None
        self.mydb = None            # Database name
        self.projects_collection = None
        

    def connect_db(self):
        self.mycluster = pymongo.MongoClient("mongodb+srv://sevdayucedagg:"+ self.password +"@cluster0.5cb1udp.mongodb.net/")
        self.mydb = self.mycluster["mydatabase"]

        self.projects_collection = ProjectsCollection(self.mydb["projects"])


    def get_databases(self):
        if self.mycluster:
            return self.mycluster.list_database_names()
        else:
            print("Database didnt create")

    def get_collections(self):
        return self.mydb.list_collection_names()

    def get_projects(self):
        return self.mydb["projects"].find()









