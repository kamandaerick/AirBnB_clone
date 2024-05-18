The AirBnB Clone Project

Description of the project

The AirBnB clone project is an important project in the ALX Africa Software Engineering Programme. The project is aimed at testing and enhancing student's understanding of Web development. This first project tested the ability of students to create classes, serialize objects to json and deserialzied json strings back to python objects.

Description of the command interpreter

The project also tested the ability of students to create a command interpreter for the project since the fornt-end design would come later. The cmd module helped us create a command interpreter that was customized to manipulate our file storage. The interpreter had various data manipulation methods such as SHOW, CREATE, DESTROY, AND UPDATE which are conventionally used to manipulate data in SQL.

How to start it

To start the console, clone it to your local machine and run the following command on your terminal:
Windows:
py console.py

Linux
./console.py

How to use it

After running the command, it give a prompt for you to enter commands. You can start by typing help. The help command will give a list of all commands that the console carries out. If you type help <command>, it will give you information about what the command does and how to use it.

Examples
1. create User: This creates a new user and gives it a unique id such as <a5193d6d-3ad2-4bf4-a0d3-813714c2c777> which is displayed immediately.

2. User.show("a5193d6d-3ad2-4bf4-a0d3-813714c2c777"):  This will show the details of the specific user with the id you specified in the bracket.

3. User.count(): This gives you the number of instances of the class User.

4. User.destroy("a5193d6d-3ad2-4bf4-a0d3-813714c2c777"): This destroys the instances whose id you have specified in the brackets.