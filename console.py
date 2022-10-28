#!/usr/bin/python3

import cmd
from utils.parser import parse


class HBNBCommand(cmd.Cmd):
    """ Define comand interpreter """

    prompt = "(hbnb) "
    __classes = {
            "BaseModel",
            "User"
            }

    def emptyline(self):
        """ ignore"""
        pass

    def do_quit(self,line):
        """ Exit Cmd"""
        return True
    
    def do_EOF(self, line):
        """ Exit on End of File instancei """
        return True



if __name__ == "__main__":
    HBNBCommand().cmdloop()
