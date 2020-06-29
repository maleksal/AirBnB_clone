#!/usr/bin/python3
import cmd


class HBNBCommand(cmd.Cmd):
    """ AriBnB Console"""

    prompt = '(hbnb) '

    def do_quit(self, line):
        ''' Quit command to exit program '''
        return True

    def do_EOF(self, line):
        ''' EOF command to exit program '''
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
