#!/usr/bin/python3
"""This is a commandline interpreter for commands specific to the AirBnB project"""

import cmd
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    def do_EOF(self, line):
        """Quit the console"""
        return True
    def help_EOF(self):
        """A function that provides information on the EOF command"""
        print("Quit command to exit the program")

    do_quit = do_EOF
    help_quit = help_EOF

    """PROJECT-RELATED COMMANDS"""
    def do_create(self, line):
        """Create a new instance of BaseModel and save it to JSON file and Print its id"""
        if not line:
            print("** class name missing **")
        elif line not in globals():
            print("** class doesn't exist **")
        else:
            model_class = globals()[line]
            instance = model_class()
            instance.save()
            print(instance.id)

if __name__ == '__main__':
    HBNBCommand().cmdloop()