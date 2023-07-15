#!/usr/bin/python3

"""
Module for Command line Interpreter
"""

import cmd
import json
import re
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User
from models import storage


class HBNBCommand(cmd.Cmd):
    """Class for command line interpreter"""

    prompt = "(hbnb) "

    classes = {
            "BaseModel": BaseModel,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review,
            "User": User
    }

    attr_types = {
            "number_rooms": int,
            "number_bathrooms": int,
            "max_guest": int,
            "price_by_night": int,
            "latitude": float,
            "longitude": float
    }

    def do_quit(self, arg):
        """Quit command to exit program"""
        return True

    def do_EOF(self, arg):
        """Exit the program"""
        print()
        return True

    def emptyline(self):
        """Do nothing for empty line"""
        pass

    def process_command(line):
         match = re.search(r"^(\w*)\.(\w+)(?:\(([^)]*)\))?$", line)
         if not match:
             return line
         classname = match.group(1)
         method = match.group(2)
         args = match.group(3)

         if method == "update":
             if args and args.startswith("{") and args.endswith("}"):
                 process_update_dict(classname, args[1:-1])
             else:
                 process_update_attributes(classname, args)

    def process_update_attributes(classname, attributes):
        print(f"Update attributes for {classname}: {attributes}")



    def do_create(self, arg):
        """Create a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
            return
        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def update_dict(self, classname, uid, s_dict):
        """
        Method for updated() with a dictionary
        """
        s = s_dict.replace("'", "'")
        d = json.loads(s)

        if not classname:
            print("** class name missing **")
            return

        storage = storage_instance()

        if classmate not in storage.classes():
            print("** class doesn't exist **")
            return

        if uid is None:
            print("** instance id is missing **")
            return

        key = f"{classname}.{uid}"
        if key not in storage.all():
            print("** no instance found **")
            return

        attributes = storage.attributes()[classname]
        instance = storage.all()[key]

        for attribute, value in d.items():
            if attribute in attributes:
                value = attributes[attribute](value)
            setattr(instance, attribute, value)

        instance.save()

    def do_show(self, arg):
        """Print the string representation of an instance"""
        if not arg:
            print("** class name missing **")
            return
        arg_list = arg.split()
        try:
            class_name = arg_list[0]
            instance_id = arg_list[1]
            obj_key = class_name + '.' + instance_id
            obj_dict = storage.all()
            if obj_key in obj_dict:
                print(obj_dict[obj_key])
            else:
                print("** no instance found **")
        except IndexError:
            if len(arg_list) == 1:
                print("** instance id is missing **")
            else:
                print("** class doesn't exist **")

    def do_destroy(self, arg):
        """
        Delete an instance based on the class name and id
        """
        if not arg:
            print("** class name missing **")
            return
        arg_list = arg.split()
        try:
            class_name = arg_list[0]
            instance_id = arg_list[1]
            obj_key = f"{class_name}.{instance_id}"
            obj_dict = storage.all()
            if obj_key in obj_dict:
                del obj_dict[obj_key]
                storage.save()
            else:
                print("** no instance found **")
        except IndexError:
            if len(arg_list) == 1:
                print("** instance id is missing **")
            else:
                print("** class doesn't exist **")

    def do_all(self, arg):
        """
        Prints all string representations of instances
        """
        arg_list = arg.split()
        obj_dict = storage.all()
        if not arg_list:
            obj_list = [str(obj) for obj in obj_dict.values()]
            print(obj_list)
        else:
            try:
                class_name = arg_list[0]
                if class_name not in storage.classes:
                    print("** class doesn't exist **")
                    return
                obj_list = [
                        str(obj) for obj in obj_dict.values() if type(
                            obj).__name__ == class_name]
                print(obj_list)
            except IndexError:
                print("** class doesn't exist **")

    def do_count(self, line):
        """
        Counts instances of a class
        """
        args = line.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in storage.classes():
            print("** class does not exist **")
        else:
            count = 0
            for key in storage.all():
                if key.split('.')[0] == args[0]:
                    count += 1
            print(count)

    def do_update(self, arg):
        """
        Update an instance based on the class name and id
        """
        if not arg:
            print("** class name string **")
            return
        args = arg.split()
        try:
            class_name = arg_list[0]
            instance_id = arg_list[1]
            obj_key = class_name + '.' + instance_id
            obj_dict = storage.all()
            if obj_key not in obj_dict:
                print("** no instance found **")
                return
            if len(arg_list) == 2:
                print("** attribute name missing **")
                return
            if len(arg_list) == 3:
                print("** value missing **")
                return
            attribute_name = arg_list[2]
            attribute_value = arg_list[3]
            if attribute_name == "id" or attribute_name == "created_at"\
            or attribute_name == "updated_at":
                return
            instance = obj_dict[obj_key]
            setattr(instance, attribute_name, attribute_value)
            instance.save()
        except IndexError:
            if len(arg_list) == 1:
                print("** instance id missing **")
            else:
                print("** class does not exist **")

    def help_show(self):
        """
        Help message for the show command
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        else:
            class_name = args[0]
            if class_name not in storage.classes():
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                instance_id = args[1]
                obj_key = "{}.{}".format(class_name, instance_id)
                obj_dict = storage.all()
                if obj_key not in obj_dict:
                    print("** no instance found **")
                else:
                    print(obj_dict[obj_key])

    def help_destroy(self):
        """
        Help mesage for the destroy command
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        else:
            class_name = args[0]
            if class_name not in storage.classes():
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id is missing **")
            else:
                instance_id = args[1]
                obj_key = "{}.{}".format(class_name, instance_id)
                obj_dict = storage.all()
                if obj_key not in obj_dict:
                    print("** no instance found **")
                else:
                    del obj_dict[obj_key]
                    storage.save()

    def help_quit(self):
        """
        Help message for the quit command
        """
        print("Quit command to exit the program")

    def help_create(self):
        """
        Help message for the create command
        """
        print("Create a new instance of BaseModel")

    def help_all(self):
        """
        Help message for the all command
        """
        print("Prints all string representation of instances")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
