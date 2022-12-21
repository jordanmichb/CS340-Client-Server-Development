from pymongo import MongoClient
from bson.objectid import ObjectId

class DatabaseCRUD(object):
    """ CRUD operations for collections in MongoDB """

    def __init__(self, username, password, port, database, collection):
        # Initialize the MongoClient. 
        self.client = MongoClient('mongodb://%s:%s@localhost:%s/%s' % (username, password, port, database))
        self.database = self.client[database] # get the database
        self.collection = self.database[collection] # get the collection

        
    def create(self, data: dict):
        """ Add document to the collection. If the data is empty, an exception is thrown. """
        if data: # if data argument is not empty
            self.collection.insert(data) # insert the data into the collection
            return True
        else: # if data argument is emtpy
            raise Exception("Nothing to save, data parameter is empty.")
            
    
    def read(self, data: dict):
        """ Read document from the collection. """
        cursor = self.collection.find(data, {"_id": False}) # search for the document
        if cursor.count() != 0: # if a document is found
            return cursor # return cursor object
        else: # if a document is not found
            raise Exception("Document not found.")
            
        
    def update(self, data: dict, newData: dict):
        """ Update document from collection. If either arguments are empty or document is not found, an exception is thrown.
            If any fields from "data" are updated, the document will still update but not print as the fields won't match the
            query. """
        if data and newData: # if these arguments are not emtpy
            cursor = self.collection.find(data) # search for the document
            if cursor.count() != 0: # if a document is found
                self.collection.update(data, {"$set": newData}) # update the document, using $set to keep other fields
                updatedCursor = self.collection.find(data)
                for doc in updatedCursor:
                    print(doc)
            else: # if no matching document was found
                raise Exception("Document not found.")
        else: # if data argument is empty
            raise Exception("Nothing to update, either data or newData parameter is empty.")
            
            
    def delete(self, data: dict):
        if data: # if data argument is not emtpy
            deleted = self.collection.delete_many(data) # delete the document
            print("Number of documents deleted: ", deleted.deleted_count) # display number of deleted documents, 0 if none found
        else: # if data argument is empty
            raise Exception("Nothing to delete, data parameter is empty.")
            
            