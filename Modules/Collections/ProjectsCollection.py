# import CollectionEnums

class ProjectsCollection():
    def __init__(self,collection):
        self.collection = collection


    def insert_project(self,order, project_name, date, company_name, keywords):
        data = [
                {"order": order, "project name" : project_name, "date" : date, "company name": company_name, "keywords":keywords},
            ]
        self.collection.insert_many(data)
        print("Successfully added.")


