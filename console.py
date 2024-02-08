#!/usr/bin/python3
"""
"""
import cmd
from models import base_model, storage


class HBNBCommand(cmd.Cmd):
    """
    This class is the entry point 
    """

    intro = ""
    prompt =  "(hbnb) "

    def do_create(self, model_name):
        if not model_name:
            print("** class name missing **")    
        elif model_name not in dir(base_model):
            print("** class doesn't exist **")
        else:
            my_model = getattr(base_model, model_name)()
            my_model.save()
            print(my_model.id)

    def do_show(self, line):
        print(storage.all())

    def do_quit(self, line):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, line):
        """
        exit the program
        """
        return True




if __name__ == '__main__':
    HBNBCommand().cmdloop()
