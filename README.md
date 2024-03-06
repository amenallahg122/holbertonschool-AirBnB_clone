# [AirBnB clone - The Console]

## Description: 
This project serves as a simplified console clone designed to manage Airbnb-like objects. Users can perform operations such as creating, updating, and deleting instances across various classes, including User, Place, State, City, Amenity, and Review. Additionally, the project incorporates functionality for serializing and deserializing, enabling the storage of instances in a JSON file.

### Console 
The console serves as a command-line interpreter, providing a means to manage the backend of HolbertonBnB. It is also utilized for handling and manipulating all the classes used within HBnB.



## [Usage]

```bash
./console.py
```

## [Testing]

Our shell work like this in interactive mode:

```bash
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$

```
also in non-interactive mode:

```bash
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$

```

## [storage]:

The storage engine, defined within the FileStorage class, manages all the classes. Upon initialization of the backend, HBnB creates an instance of FileStorage named 'storage.' This 'storage' object is responsible for loading and reloading class instances from the JSON file.

# Commands :

### Create
To create an object use format "create <ClassName>" 

### Show
To show an instance based on the class name and id. 

### Destroy
To Delete an instance of an object use "destroy <ClassName> id". 
Destroy BaseModel 4848-4444-8888.
### All
all or all <class name> 

### Update
Updates an instance based on the class name and id:

### Quit
quit or EOF

### Help
help or help <command> 

