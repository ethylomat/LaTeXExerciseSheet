import os
import shutil

"""
    Removing files if not needed after template creation.
"""

def remove(filepath):
    if os.path.isfile(filepath):
        os.remove(filepath)
    elif os.path.isdir(filepath):
        shutil.rmtree(filepath)


# Remove literature.bib

create_literature = '{{cookiecutter.Literature}}' == 'y'

if not create_literature:
    remove('literature.bib')