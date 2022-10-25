#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        #if cls is None:
            #return FileStorage.__objects

        #cls_objects = {}

        #for val in FileStorage.__objects.values():
            #if type(val) == cls:
                #cls_objects.update(
                    #{val.to_dict()['__class__'] + '.' + val.id: val}
                #)

        #return cls_objects
        if cls in not None:
            new_dict = {}
            for key, val in self.__objects.items():
                if cls == val.__class__:
                    new_dict[key] = val
            return new_dict
        return self.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    #def delete(self, obj=None):
        #"""deletes obj from _objects"""
        #if obj is None:
            #return
        #for key, val in dict(FileStorage.__objects).items():
            #if val == obj:
                #del FileStorage.__objects[key]

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """ Delete object from __objects """
        if not obj:
            return
        key = "{}.{}".format(type(obj).__name__, obj.id)
        if key in self.__objects:
            del self.__objects[key]
            self.save()

    def close(self):
        """ call reload() for deserialization """
        self.reload()
