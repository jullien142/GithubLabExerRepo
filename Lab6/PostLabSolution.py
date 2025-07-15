import pandas as pd
from pymongo import MongoClient
import os

class MongoDBImporter:
    def __init__(self, connection_string="mongodb://localhost:27017/"):
        try:
            self.client = MongoClient(connection_string, serverSelectionTimeoutMS=5000)
            self.client.admin.command('ping')
            self.db_name = "music_database"
            self.db = self.client[self.db_name]
        except Exception as e:
            print(f"MongoDB connection failed: {str(e)}")
            raise
        
    def import_csv_to_collection(self, csv_file, collection_name):
        try:
            if not os.path.exists(csv_file):
                print(f"File not found: {csv_file}")
                return False
            df = pd.read_csv(csv_file)
            if df.empty:
                print(f"CSV is empty: {csv_file}")
                return False
            records = df.to_dict('records')
            collection = self.db[collection_name]
            collection.delete_many({})
            if records:
                collection.insert_many(records)
                return True
            print(f"No records to insert for: {csv_file}")
            return False
        except Exception as e:
            print(f"Error importing {csv_file} to {collection_name}: {str(e)}")
            return False
    
    def import_all_collections(self):
        csv_collections = {
            "albums.csv": "albums",
            "artists.csv": "artists", 
            "tracks.csv": "tracks"
        }
        success = True
        for csv_file, collection_name in csv_collections.items():
            if not self.import_csv_to_collection(csv_file, collection_name):
                success = False
        return success
    
    def close_connection(self):
        if hasattr(self, 'client'):
            self.client.close()

def main():
    try:
        importer = MongoDBImporter("mongodb://localhost:27017/")
        if importer.import_all_collections():
            print("Data imported")
        else:
            print("Failed")
    except Exception as e:
        print("Failed")
    finally:
        if 'importer' in locals():
            importer.close_connection()

if __name__ == "__main__":
    main() 