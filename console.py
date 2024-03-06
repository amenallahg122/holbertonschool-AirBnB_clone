#!/usr/bin/python3
"""Cmd class file"""
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
from models.user import User
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models.amenity import Amenity

classnames = ["BaseModel", "User", "Review",
              "City", "Place", "State", "Amenity"]


class HBNBCommand(cmd.Cmd):
    """Cmd class"""

    prompt = "(hbnb) "

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, args):
        """press EOF key to exit program"""
        print("")
        return True

    def emptyline(self):
        """ignore the default behavior of printing the last command"""
        pass

    def do_create(self, line):
        """Creates a new instance of BaseModel, saves it 
        (to the JSON file), and prints the id"""
        if line == "":
            print("** class name missing **")
        elif line not in classnames:
            print("** class doesn't exist **")
        else:
            print(eval(line)().id)
            storage.save()

    def do_show(self, line):
        """Prints the string representation of an instance 
        based on the class name and id"""
        commands = line.split()
        if line == "":
            print("** class name missing **")
        elif commands[0] not in classnames:
            print("** class doesn't exist **")
        elif len(commands) == 1:
            print("** instance id missing **")
        else:
            dic = storage.all()
            key = "{}.{}".format(commands[0], commands[1])
            if key in dic:
                print(dic[key])
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        """Delete an instance based on the class name and id"""
        commands = line.split()
        if line == "":
            print("** class name missing **")
        elif commands[0] not in classnames:
            print("** class doesn't exist **")
        elif len(commands) == 1:
            print("** instance id missing **")
        else:
            dic = storage.all()
            key = "{}.{}".format(commands[0], commands[1])
            if key in dic:
                del dic[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, line):
        """Print string representation of all
        instances based on a class name""" 
        dic = storage.all()
        if line == "":
            for key in dic.keys():
                print(dic[key])
        elif line not in classnames:
            print("** class doesn't exist **")
        else:
            for key in dic.keys():
                classname, classid = key.split(".")
                if classname == line:
                    print(dic[key])
