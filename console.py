#!/usr/bin/python3
"""
Official,Here We Go
"""
import cmd
import JSON
from datetime import datetime
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class HBNBCommand(cmd.Cmd):
    """This is the entry point of the interpreter"""

    prompt = "(hbnb) "
    classes = {"BaseModel", "User", "State", "City",
                   "Amenity", "Place", "Review"}

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """Quit command to exit the program at end of file"""
        print("")
        return True

    def do_create(self, line):
        """Creates an instance specified by the user.
        """
        if line == "" or line is None:
            print("** class name missing **")
        elif line not in storage.classes():
            print("** class doesn't exist **")
        else:
            r = storage.classes()[line]()
            r.save()
            print(r.id)
    def emptyline(self):
        """Overwrite default behavior to repeat last cmd"""

        pass

    def parse(line):
        """Helper method to parse user typed input"""
        return tuple(line.split())

    def do_show(self, line):
        """Print string representation of an instace
        Exceptions:
            SyntaxError: when there is no args given
            NameError: when no object with that name
            IndexError: when there is no id given
            KeyError: when there is no valid id given
        """

        if len(line) == 0:
            print("** class name missing **")
            return
        argu = parse(line)
        objedict = storage.all()
        if argu[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        try:
            if argu[1]:
                keys = "{}.{}".format(argu[0], argu[1])
                if keys not in objedict ().keys():
                    print("** no instance found **")
                else:
                    print(objedict()[keys])
        except IndexError:
            print("** instance id missing **")
    def do_destroy(self, arg):
        """Destroys an instance based on the class name and id
        Exceptions; save changes to JSON file

        """
        argu = parse(line)
        objedict = storage.all()
        if len(argu) == 0:
            print("** class name missing **")
        elif argu[0] not in HBNBCommand.all_classes:
            print("** class doesn't exist **")
        elif len(argu) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argu[0], argu[1]) not in objedict.keys():
            print("** no instance found **")
        else:
            del objedict["{}.{}".format(argu[0], argu[1])]
            storage.save()

    def do_count(self, line):
        """Display count of number of instances in specified class"""
        if line in HBNBCommand.classes:
            count = 0
            for key, objs in storage.all().items():
                if line in key:
                    count += 1
            print(count)
        else:
            print("** class doesn't exist **")


    def do_all(self, line):
        """Prints all string representation of all instances
        Exceptions:
            NameError: when no object with that name"""
        args = parse(line)
        obj_list = []
        if len(line) == 0:
            for objs in storage.all().values():
                obj_list.append(objs)
            print(obj_list)
        elif args[0] in HBNBCommand.classes:
            for key, objs in storage.all().items():
                if args[0] in key:
                    obj_list.append(objs)
            print(obj_list)
        else:
            print("** class doesn't exist **")
    def do_update(self, line):
        """Update if given exact object, exact attribute"""
        args = parse(line)
        if len(args) >= 4:
            key = "{}.{}".format(args[0], args[1])
            cast = type(eval(args[3]))
            arg3 = args[3]
            arg3 = arg3.strip('"')
            arg3 = arg3.strip("'")
            setattr(storage.all()[key], args[2], cast(arg3))
            storage.all()[key].save()
        elif len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif ("{}.{}".format(args[0], args[1])) not in storage.all().keys():
            print("** no instance found **")
        elif len(args) == 2:
            print("** attribute name missing **")
        else:
            print("** value missing **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()