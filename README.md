Database-Assignment_2

## Dependencies
You need a machine with python and mongoDB and docker to run this code.

The needed imports for python are :

import zipfile - I think this is a part of the standard lib
import pymongo <----------------------- This on you neeed to pip install using pip install pymongo
from pymongo import MongoClient
import subprocess I think this is a part of the standard lib
import os I think this is a part of the standard lib
import pprint I think this is a part of the standard lib
import re I think this is a part of the standard lib


## how to run program.

1. clone the git project.

2. cd to the project folder.(!important)

3. Run the following command in the terminal :

'''
docker run --rm -v $(pwd)/data:/data/db --publish=27017:27017 --name dbms -d mongo
'''
This code will start a mongodb.

4. Run the python file main.py with the following command.

'''
python main.py
'''

5. This will out put the following output

