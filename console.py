#!/usr/bin/python3
"""This is a commandline interpreter for commands specific to the AirBnB project"""

import cmd
import re
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from count_instances import count_user, count_base_model, count_state, count_city, count_amenity, count_place, count_review
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
    def default(self, line):
        """The deault class to handle unknown commands"""
        pattern_user = r'^User\.show\("([^"]+)"\)$'
        match_user = re.match(pattern_user, line)
        pattern_state = r'^State\.show\("([^"]+)"\)$'
        match_state = re.match(pattern_state, line)
        pattern_city = r'^City\.show\("([^"]+)"\)$'
        match_city = re.match(pattern_city, line)
        pattern_amenity = r'^Amenity\.show\("([^"]+)"\)$'
        match_amenity = re.match(pattern_amenity, line)
        pattern_place = r'^Place\.show\("([^"]+)"\)$'
        match_place = re.match(pattern_place, line)
        pattern_review = r'^Review\.show\("([^"]+)"\)$'
        match_review = re.match(pattern_review, line)

        pattern_d_user = r'^User\.destroy\("([^"]+)"\)$'
        match_d_user = re.match(pattern_d_user, line)
        pattern_d_state = r'^State\.destroy\("([^"]+)"\)$'
        match_d_state = re.match(pattern_d_state, line)
        pattern_d_city = r'^City\.destroy\("([^"]+)"\)$'
        match_d_city = re.match(pattern_d_city, line)
        pattern_d_amenity = r'^Amenity\.destroy\("([^"]+)"\)$'
        match_d_amenity = re.match(pattern_d_amenity, line)
        pattern_d_place = r'^Place\.destroy\("([^"]+)"\)$'
        match_d_place = re.match(pattern_d_place, line)
        pattern_d_review = r'^Review\.destroy\("([^"]+)"\)$'
        match_d_review = re.match(pattern_d_review, line)

        if line.strip() == "User.all()":
            self.do_all("User")
        elif line.strip() == "BaseModel.all()":
            self.do_all("BaseModel")
        elif line.strip() == "State.all()":
            self.do_all("State")
        elif line.strip() == "City.all()":
            self.do_all("City")
        elif line.strip() == "Amenity.all()":
            self.do_all("Amenity")
        elif line.strip() == "Place.all()":
            self.do_all("Place")
        elif line.strip() == "Review.all()":
            self.do_all("Review")
        elif line.strip() == "User.count()":
            self.do_count("User")
        elif line.strip() == "BaseModel.count()":
            self.do_count("BaseModel")
        elif line.strip() == "State.count()":
            self.do_count("State")
        elif line.strip() == "City.count()":
            self.do_count("City")
        elif line.strip() == "Amenity.count()":
            self.do_count("Amenity")
        elif line.strip() == "Place.count()":
            self.do_count("Place")
        elif line.strip() == "Review.count()":
            self.do_count("Review")
        elif match_user:
            command = line.strip().split("\"")
            class_id = command[1].strip()
            if f"User.{class_id}" in FileStorage.objects_copy:
                self.do_show(f"User {class_id}")
            else:
                print("** no instance found **")
        elif match_state:
            command = line.strip().split("\"")
            class_id = command[1].strip()
            if f"State.{class_id}" in FileStorage.objects_copy:
                self.do_show(f"State {class_id}")
            else:
                print("** no instance found **")
        elif match_city:
            command = line.strip().split("\"")
            class_id = command[1].strip()
            if f"City.{class_id}" in FileStorage.objects_copy:
                self.do_show(f"City {class_id}")
            else:
                print("** no instance found **")
        elif match_amenity:
            command = line.strip().split("\"")
            class_id = command[1].strip()
            if f"Amenity.{class_id}" in FileStorage.objects_copy:
                self.do_show(f"Amenity {class_id}")
            else:
                print("** no instance found **")
        elif match_place:
            command = line.strip().split("\"")
            class_id = command[1].strip()
            if f"Place.{class_id}" in FileStorage.objects_copy:
                self.do_show(f"Place {class_id}")
            else:
                print("** no instance found **")
        elif match_review:
            command = line.strip().split("\"")
            class_id = command[1].strip()
            if f"Review.{class_id}" in FileStorage.objects_copy:
                self.do_show(f"Review {class_id}")
            else:
                print("** no instance found **")
        elif match_d_user:
            command = line.strip().split("\"")
            class_id = command[1].strip()
            if f"User.{class_id}" in FileStorage.objects_copy:
                self.do_destroy(f"User {class_id}")
            else:
                print("** no instance found **")
        elif match_d_state:
            command = line.strip().split("\"")
            class_id = command[1].strip()
            if f"State.{class_id}" in FileStorage.objects_copy:
                self.do_destroy(f"State {class_id}")
            else:
                print("** no instance found **")
        elif match_d_city:
            command = line.strip().split("\"")
            class_id = command[1].strip()
            if f"City.{class_id}" in FileStorage.objects_copy:
                self.do_destroy(f"City {class_id}")
            else:
                print("** no instance found **")
        elif match_d_amenity:
            command = line.strip().split("\"")
            class_id = command[1].strip()
            if f"Amenity.{class_id}" in FileStorage.objects_copy:
                self.do_destroy(f"Amenity {class_id}")
            else:
                print("** no instance found **")
        elif match_d_place:
            command = line.strip().split("\"")
            class_id = command[1].strip()
            if f"Place.{class_id}" in FileStorage.objects_copy:
                self.do_destroy(f"Place {class_id}")
            else:
                print("** no instance found **")
        elif match_d_review:
            command = line.strip().split("\"")
            class_id = command[1].strip()
            if f"Review.{class_id}" in FileStorage.objects_copy:
                self.do_destroy(f"Review {class_id}")
            else:
                print("** no instance found **")    

        else:
            print("** no instance found **")
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

    def do_show(self, line):
        """Print the string representation of an instance based on the class name and id"""
        tokens = line.split()
        if not tokens:
            print("** class name missing **")
            return
        elif tokens[0] not in globals():
            print("** class doesn't exist **")
            return
        elif len(tokens) == 1:
            print("** instance id missing **")
            return
        else:
            instance_attribute = f"{tokens[0]}.{tokens[1]}"
            if not instance_attribute in FileStorage.objects_copy:
                print("** no instance found **")
            else:
                instance = FileStorage.objects_copy[instance_attribute]
                print(instance)

    def do_destroy(self, line):
        """Delete an instance based on the class name and id"""
        tokens = line.split()
        if not tokens:
            print("** class name missing **")
            return
        elif tokens[0] not in globals():
            print("** class doesn't exist **")
            return
        elif len(tokens) == 1:
            print("** instance id missing **")
            return
        instance_attribute = f"{tokens[0]}.{tokens[1]}"
        if instance_attribute not in FileStorage.objects_copy:
            print("** no instance found **")
        else:
            del FileStorage.objects_copy[instance_attribute]
            FileStorage.save(FileStorage)

    def do_all(self, line):
        """Print string representation of all instances based or not on the class name"""
        tokens = line.split()
        if not tokens:
            print([str(obj) for obj in FileStorage.objects_copy.values()])
        elif tokens[0] not in globals():
            print("** class doesn't exist **")
            return
        else:
            print([str(obj) for obj in FileStorage.objects_copy.values() if type(obj) == globals()[tokens[0]]])
    
    def do_update(self, line):
        """Update an instance based on the class name and id by adding or updating attribute"""
        tokens = line.split()
        if not tokens:
            print("** class name missing **")
            return
        elif tokens[0] not in globals():
            print("** class doesn't exist **")
            return
        elif len(tokens) == 1:
            print("** instance id missing **")
            return
        instance_attribute = f"{tokens[0]}.{tokens[1]}"
        if instance_attribute not in FileStorage.objects_copy:
            print("** no instance found **")
            return
        elif len(tokens) == 2:
            print("** attribute name missing **")
            return
        elif len(tokens) == 3:
            print("** value missing **")
            return
        setattr(FileStorage.objects_copy[instance_attribute], tokens[2], tokens[3])
        FileStorage.save(FileStorage)

    def do_count(self, line):
        """Count the number of instances of a class"""
        if line == "User":
            print(count_user())
        elif line == "BaseModel":
            print(count_base_model())
        elif line == "State":
            print(count_state())
        elif line == "City":
            print(count_city())
        elif line == "Amenity":
            print(count_amenity())
        elif line == "Place":
            print(count_place())
        elif line == "Review":
            print(count_review())
        else:
            print("** class doesn't exist **")       

    
if __name__ == '__main__':
    HBNBCommand().cmdloop()