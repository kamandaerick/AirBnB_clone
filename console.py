#!/usr/bin/python3
"""This is a commandline interpreter for commands specific to the AirBnB project"""

import cmd

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
        pass

    def do_show(self, line):
        pass

    def do_destroy(self, line):
        pass

    def do_all(self, line):
        pass

    def do_update(self, line):
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()