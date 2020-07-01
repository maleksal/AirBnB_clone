#!/usr/bin/python3
""" Console code """
import cmd
import shlex
from models.base_model import BaseModel
from models import storage


def check_class_exists(classes, class_name):
    """ checks if class exists in a list of classes """
    if class_name not in classes:
        return False
    return True


def handle_conditions(classes, full_args):
    """
    Handle condition for commands that have +1 argument,

    Args:
        classes: List of available classes
        full_args: (str) command line arguments

    Returns:
        True: if pass all conditions
        False & prints (associated error message): if condition fail

    """
    if full_args:
        args = full_args.split()
        if check_class_exists(classes, args[0]):
            if len(args) > 1:
                return True
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")
    else:
        print("** class name missing **")
    return False


class HBNBCommand(cmd.Cmd):
    """ AriBnB Console """
    prompt = '(hbnb) '
    classes = ["BaseModel"]

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, line):
        '''EOF command to exit the program
        '''
        return True

    def emptyline(self):
        """ do nothing when an empty line """
        pass

    def do_create(self, line):
        """
        Creates a new instance of BaseModel, saves it to the JSON file
        and prints the id. Ex: $ create BaseModel.

        """
        if line:
            param = line.split()
            if check_class_exists(self.classes, param[0]):
                dummy_instance = eval(param[0])()
                dummy_instance.save()
                print(dummy_instance.id)
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, line):
        """
        Prints the string representation of an instance based on
        the class name and id.

        Example:
            $ show BaseModel 1234-1234-1234.

        """
        database = storage.all()

        if handle_conditions(self.classes, line):
            param = line.split()
            key = "{}.{}".format(param[0], param[1])
            if key in database.keys():
                print(database[key])
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id,
        save the change into the JSON file.

        """
        database = storage.all()

        if handle_conditions(self.classes, line):
            param = line.split()
            key = "{}.{}".format(param[0], param[1])
            if key in database.keys():
                del database[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, line):
        """
        Prints all string representation of all instances.

        """
        output = []

        if line and not check_class_exists(self.classes, line.split()[0]):
            print("** class doesn't exist **")
            return

        for object in storage.all().values():
            if line:
                if type(object).__name__ == line.split()[0]:
                    output.append(object.__str__())
            else:
                output.append(object.__str__())
        print(output)

    def do_update(self, line):
        """  Updates an instance based on the class name and id """

        if handle_conditions(self.classes, line):
            args = shlex.split(line)
            if len(args) > 2:
                if len(args) > 3:
                    key = "{}.{}".format(args[0], args[1])
                    if key in storage.all():
                        setattr(storage.all()[key], args[2], args[3])
                        storage.all()[key].save()
                    else:
                        print("** no instance found **")
                else:
                    print("** value missing **")
            else:
                print("** attribute name missing **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
