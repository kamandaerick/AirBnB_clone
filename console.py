#!/usr/bin/python3
"""An interpreter for my AirBnB clone commands"""
import cmd
import sys

from typing import Dict

from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, args):
        """Quit command to exit the program\n"""
        sys.exit()

    def do_EOF(self, args):
        """EOF command to quit the program\n"""
        return True

    def emptyline(self):
        pass

    def do_create(self, args):
        """Create a new instance of BaseModel and save to JSON"""
        if args == BaseModel.get_name():
            new_base_model = BaseModel()
            new_base_model.save()
            print(new_base_model.id)
        elif not args:
            print("** class name missing **")
        elif args != BaseModel.get_name():
            print("** class doesn't exist **")

    def do_show(self, args):
        """Print the string representation of an
        instance based on class name and id"""
        if not args:
            print("** class name missing **")
        elif len(args.split()) == 1:
            # first if
            if args != BaseModel.get_name():
                print("** class doesn't exist **")
            else:
                print("** instance id missing **")
        elif len(args.split()) == 2:
            _name = args.split()[0]
            _id = args.split()[1]
            if _name != BaseModel.get_name():
                print("** class doesn't exist **")
            else:
                # access the stored models
                from models import storage
                data = list(storage.all().values())
                for d in data:
                    if d.get('id') == _id:
                        bm = BaseModel(**d)
                        print(str(bm))
                        break
                    else:
                        print('** no instance found **')
                        break

    def do_destroy(self, args):
        """Destroys an object"""
        if not args:
            print("** class name missing **")
        elif len(args.split()) == 1:
            if args != BaseModel.get_name():
                print("** class doesn't exist **")
            else:
                print("** instance id missing **")
        elif len(args.split()) == 2:
            _name = args.split()[0]
            _id = args.split()[1]
            if _name != BaseModel.get_name():
                print("** class doesn't exist **")
            else:
                # access the stored models
                from models import storage

                _data = storage.all()
                data = _data.items()
                key_to_del = ''
                for k, v in data:
                    if v.get('id') == _id:
                        key_to_del = k
                        break
                    else:
                        print('** no instance found **')
                        break

                del _data[key_to_del]
                for k, v in _data.items():
                    bm = BaseModel(**v)
                    bm.save()

    def do_all(self, args):
        """Print all string representation of all instances
        based or not on the class name"""
        if len(args.split()) == 1 or len(args.split()) == 0:
            if len(args.split()) == 1 and args != BaseModel.get_name():
                print("** class doesn't exist **")
            else:
                from models import storage
                all_data = []
                data = list(storage.all().values())
                for d in data:
                    bm = BaseModel(**d)
                    all_data.append(str(bm))
                print(all_data)

    def do_update(self, args):
        """Update an instance based on the class name and id
         by adding or updating attribute (save change into json)
         """
        if not args:
            print("** class name missing **")
        else:
            arg_list = args.split()
            class_name = arg_list[0]
            if class_name != BaseModel.get_name():
                print("** class doesn't exist **")
            elif len(arg_list) < 2:
                print("** instance id missing **")
            else:
                instance_id = arg_list[1]
                from models import storage
                all_data = storage.all()
                key_to_update = f"{class_name}.{instance_id}"

                if key_to_update not in all_data:
                    print("** no instance found **")
                elif len(arg_list) < 3:
                    print("** attribute name missing **")
                elif len(arg_list) < 4:
                    print("** value missing **")
                else:
                    attribute_name = arg_list[2]
                    attribute_value = arg_list[3]

                    try:
                        attribute_value = eval(attribute_value)
                    except(ValueError, SyntaxError, TypeError):
                        pass

                    instance_data = all_data[key_to_update]
                    instance_data[attribute_name] = attribute_value
                    ut = datetime.now().strftime(BaseModel.__fmt_datetime)
                    instance_data['updated_at'] = ut
                    storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
