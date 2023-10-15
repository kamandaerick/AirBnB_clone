#!/usr/bin/python3
"""An interpreter for my AirBnB clone commands"""
import cmd
import sys


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, args):
        """Quit command to exit the program\n"""
        sys.exit()

    def do_EOF(self, args):
        """EOF command to quit the program\n"""
        return True

    def emptyline(self):
        """Does nothing when an empty line + ENTER"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
