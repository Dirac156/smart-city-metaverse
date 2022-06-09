import json
from os import getenv

from blockchain.block import Block

classes = {"Blockchain": "Blockchain"}

class FileStorage:
    """serializes instances to a JSON file & deserializes back to instances"""

    # string - path to the JSON file
    __file_path = "default_blockchain.json"
    # dictionary - empty but will store all objects by <class name>.id
    __objects = {}

    def __init__(self):
        pass

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        if obj is not None:
            key = obj.block_hash
            self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        json_objects = {}
        for key in self.__objects:
            json_objects[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(json_objects, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        obj = []
        try:
            with open(self.__file_path, 'r') as f:
                jo = json.load(f)
            for key in jo:
                block = Block(**jo[key])
                self.__objects[key] = block
                obj.append(block)
            # return object of blocks
            return obj
        except:
            pass

    def delete(self, obj=None):
        """delete obj from __objects if it’s inside"""
        if obj is not None:
            key = obj.__class__.__name__ + '.' + obj.id
            if key in self.__objects:
                del self.__objects[key]

    def close(self):
        """call reload() method for deserializing the JSON file to objects"""
        self.reload()

    # def get(self, cls, id):
    #     """
    #     Returns the object based on the class name and its ID, or
    #     None if not found
    #     """
    #     if cls not in classes.values():
    #         return None

    #     all_cls = models.storage.all(cls)
    #     for value in all_cls.values():
    #         if (value.id == id):
    #             return value

    #     return None

    # def count(self, cls=None):
    #     """
    #     count the number of objects in storage
    #     """
    #     all_class = classes.values()

    #     if not cls:
    #         count = 0
    #         for clas in all_class:
    #             count += len(models.storage.all(clas).values())
    #     else:
    #         count = len(models.storage.all(cls).values())

    #     return count