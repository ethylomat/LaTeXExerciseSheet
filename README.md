Exercise Sheet Template
=======================

Template generator for LaTeX Exercise sheets.

Requirements
------------
Install `cookiecutter` command line: `pip install cookiecutter`

Usage
-----
Generate a new Cookiecutter template layout: `cookiecutter gh:ethylomat/uebungszettel`    

Example
-------
```console
# Create a project directory
foo@bar:~$ cookiecutter gh:ethylomat/uebungszettel
Name [Max Mustermann]: Max Mustermann
Exercise_Sheet_No [1]: 
Select Class:
1 - Example Class 1 2018/19
2 - Example Class 2 2018/19
3 - Example Class 3 2018/19
Choose from 1, 2, 3 [1]: 1
Literature [n]: y
No_of_Tasks [1]: 4
foo@bar:~$ ls Blatt01
head.tex main.tex literature.bib
```

Compile LaTeX document via `lualatex main.tex`  

Configuration
-------------
To configure the exercise template settings edit the file `cookiecutter.json`.

To edit the template files navigate to the directory: `Blatt{{cookiecutter.Exercise_Sheet_No.zfill(2)}}`


License
-------
This project is licensed under the terms of the [MIT License](/LICENSE)
