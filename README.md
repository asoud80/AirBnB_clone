# Project Description
This is an AirBnB clone (named HBNB) which is capable of controlling web page modules. OOP and command line logic were used.

# The Command Interpreter
* create your data model
* manage (create, update, destroy, etc) objects via a console / command interpreter
* store and persist objects to a file (JSON file)

The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”. This means: from your console code (the command interpreter itself) and from the front-end and RestAPI you will build later, you won’t have to pay attention (take care) of how your objects are stored.

This abstraction will also allow you to change the type of storage easily without updating all of your codebase.

The console will be a tool to validate this storage engine


## How to start

```bash
git clone https://github.com/asoud80/AirBnB_clone.git
cd AirBnB_clone
python3 console.py
```
## How to use

### Commands

* `create`: Creates a new instance of `BaseModel`, saves it (to the JSON file) and prints the id. Ex: `$ create BaseModel`
* `show`: Prints the string representation of an instance based on the class name and id. Ex: `$ show BaseModel 1234-1234-1234`
* `all`: Prints all string representation of all instances based or not on the class name. Ex: `$ all BaseModel`
* `update`: Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file). Ex: `$ update BaseModel 1234-1234-1234 email "aibnb@holbertonschool.com"`
