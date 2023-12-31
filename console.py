#!/usr/bin/python3
""" The console that represents the frontend of the App """
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Define the command interpreter"""

    prompt = "(hbnb) "
    classes = {
        "BaseModel": BaseModel, "User": User, "State": State,
        "City": City, "Amenity": Amenity,
        "Place": Place, "Review": Review}

    def do_quit(self, arg):
        """Quit command to exit the program"""
        exit()

    def do_EOF(self, arg):
        """Exit the program"""
        print("")
        exit()

    def emptyline(self):
        """pass when emptyline entered"""
        pass

    def do_create(self, arg):
        """Create instance of a specific class"""
        if arg:
            argv = arg.split()
            if len(argv) == 1:
                if arg in self.classes.keys():
                    instance = self.classes[arg]()
                    instance.save()
                    print(instance.id)
                else:
                    print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, arg):
        """Prints the string representation
        of an instance based on the class name and id
        """
        if arg:
            arg1 = arg.split()[0]
            if arg1 not in self.classes.keys():
                print("** class doesn't exist **")
                return
            if len(arg.split()) > 1:
                key = arg1 + '.' + arg.split()[1]
                objects = storage.all()
                if key in objects.keys():
                    print(objects[key])
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class name missing **")
            return

    def do_destroy(self, arg):
        """
            Deletes an instance based on
            the class name and id
        """
        if arg:
            arg1 = arg.split()[0]
            if arg1 not in self.classes.keys():
                print("** class doesn't exist **")
                return
            if len(arg.split()) > 1:
                key = arg1 + '.' + arg.split()[1]
                objects = storage.all()
                if key in objects.keys():
                    storage.all().pop(key)
                    storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class name missing **")
            return

    def do_all(self, arg):
        """Prints all string representation of all instances
            based or not on the class name
        """
        if arg:
            if arg not in self.classes.keys():
                print("** class doesn't exist **")
            else:
                emptyList = []
                for key, value in storage.all().items():
                    if arg in key:
                        emptyList.append(str(value))
                print(emptyList)
        else:
            emptyList = []
            for value in storage.all().values():
                emptyList.append(str(value))
                print(emptyList)

    def do_update(self, arg):
        """
        Updates an instance based on the class name
        and id by adding or updating attribute
        """
        if arg:
            argv = arg.split()
            if argv[0] not in self.classes.keys():
                print("** class doesn't exist **")
            elif len(argv) == 1:
                print('** instance id missing **')
                return
            else:
                key = argv[0] + '.' + argv[1]
                if key in storage.all().keys():
                    if len(argv) > 2:
                        if len(argv) == 3:
                            print('** value missing **')
                        else:
                            setattr(storage.all()[key],
                                    argv[2],
                                    argv[3][1:-1])
                            storage.all()[key].save()
                    else:
                        print('** attribute name missing **')
                else:
                    print('** no instance found **')
        else:
            print('** class name missing **')
            return


if __name__ == '__main__':
    HBNBCommand().cmdloop()
