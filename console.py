#!/usr/bin/python3
""" Console code """
import cmd
import shlex
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
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
    classes = [
        "BaseModel", "User",
        'State', 'City',
        'Amenity', 'Place',
        'Review']

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

    def default(self, line):
        """ Handle advanced args """
        advanced_args = {
            ".all()": self.advanced_all,
            ".count()": self.advanced_count,
            ".show(": self.advanced_show,
            ".destroy(": self.advanced_destroy,
            ".update(": self.advanced_update

            }
        # check for valid command
        for cmd in advanced_args.keys():
            if cmd in line:
                return advanced_args[cmd](line)
        print("*** Unknown syntax: ", line)

    def advanced_all(self, args):
        """
        handle <class_name>.all()
        gets all instances of specific class_name.

        """
        args_list = args.split(".")
        self.do_all(args_list[0])

    def advanced_count(self, args):
        """
        handle <class_name>.count()
        number of instance of specific class_name.

        """
        args_list = args.split(".")
        objects = self.do_all(args_list[0], to_return=True)
        if objects:
            print(len(objects))

    def advanced_show(self, args):
        """
        handle <class_name>.show(<id>)
        gets instance of <class_name> and specific <id>.

        """
        args_list = args.split(".show")
        id = args_list[1][2:-2]
        self.do_show("{} {}".format(args_list[0], id))

    def advanced_destroy(self, args):
        """
        handle <class_name>.destroy(<id>)
        deletes instance of specific <class_name> and <id>.

        """
        args_list = args.split(".destroy")
        id = args_list[1][2:-2]
        self.do_destroy("{} {}".format(args_list[0], id))

    def advanced_update(self, args):
        """
        handle <class_name>.update(<id> <attr> <value>)
        update an instance of specific <class_name> based on <id>.

        """
        arguments = args.split('.update')
        if '{' in arguments[1]:
            return self.advanced_update_dictionary(args)
        params = shlex.split(arguments[1][1:-1])
        len_params = len(params)
        update_arguments = ""

        for i in range(len_params):
            update_arguments += "{}".format(params[i].strip(','))
            if i + 1 < len_params:
                update_arguments += " "
        self.do_update("{} {}".format(arguments[0], update_arguments))

    ''' This code is not completed yet: Logic need to be upfated
    def advanced_update_dictionary(self, args):
        """ handle update from dictionary """
        full_args = args.split('.update')
        class_name = full_args[0]
        dictionary_part = full_args[1].partition(',')
        class_id = dictionary_part[0][1:]

        try:
            this_dictionary = eval(dictionary_part[2][:-1])
            print(this_dictionary)

            if not type(this_dictionary) == dict:
                raise Exception
        except Exception:
            this_dictionary = {"":""}
        for attr, value in this_dictionary.items():
            self.do_update("{} {} {} {}".format(
                class_name, class_id, attr, value))
    '''

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

    def do_all(self, line, to_return=None):
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
        if to_return:
            return output
        print(output)

    def do_update(self, line):
        """  Updates an instance based on the class name and id """

        def type_cast_value(obj, attr, value):
            """
            Type cast attribute value to attribute type.

            """
            cast_typing = type(obj.__dict__[attr]).__name__
            return eval(cast_typing)(value)

        if handle_conditions(self.classes, line):
            args = shlex.split(line)
            if len(args) > 2:
                if len(args) > 3:
                    key = "{}.{}".format(args[0], args[1])
                    if key in storage.all():
                        value = type_cast_value(
                            storage.all()[key], args[2], args[3])
                        print(type(value))
                        setattr(storage.all()[key], args[2], value)
                        storage.all()[key].save()
                    else:
                        print("** no instance found **")
                else:
                    print("** value missing **")
            else:
                print("** attribute name missing **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
