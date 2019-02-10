Database-Assignment_2

## Dependencies
You need a machine with python and mongoDB and docker to run this code.

The needed imports for python are :

import zipfile - I think this is a part of the standard lib. </br>

import pymongo <----------------------- This on you neeed to pip install using pip install pymongo.</br>
from pymongo import MongoClient.</br>

import subprocess I think this is a part of the standard lib.</br>

import os I think this is a part of the standard lib.</br>

import pprint I think this is a part of the standard lib.</br>

import re I think this is a part of the standard lib.


## how to run program.

1. clone the git project.

2. cd to the project folder.(!important)

3. Inside the project folder create a folder called 'data':

```
mkdir data
```

4. Run the following command in the terminal :

```
docker run --rm -v $(pwd)/data:/data/db --publish=27017:27017 --name dbms -d mongo
```
This code will start a mongodb.

5. Run the python file main.py with the following command.


```
python main.py

```

6. This will out put the following output

```
How many Twitter users are in the database?
Result :  659774

Which Twitter users link the most to other Twitter users?
{'_id': 'lost_dog', 'links': 549}
{'_id': 'tweetpet', 'links': 310}
{'_id': 'VioletsCRUK', 'links': 251}
{'_id': 'what_bugs_u', 'links': 246}
{'_id': 'tsarnick', 'links': 245}
{'_id': 'SallytheShizzle', 'links': 229}
{'_id': 'mcraddictal', 'links': 217}
{'_id': 'Karen230683', 'links': 216}
{'_id': 'keza34', 'links': 211}
{'_id': 'TraceyHewins', 'links': 202}

Who is are the most mentioned Twitter users? (Provide the top five.)
('@mileycyrus', 4499)
('@tommcfly', 3886)
('@ddlovato', 3466)
('@DavidArchie', 1298)
('@Jonasbrothers', 1286)

Who are the most active Twitter users (top ten)?
{'_id': 'lost_dog', 'count': 549}
{'_id': 'webwoke', 'count': 345}
{'_id': 'tweetpet', 'count': 310}
{'_id': 'SallytheShizzle', 'count': 281}
{'_id': 'VioletsCRUK', 'count': 279}
{'_id': 'mcraddictal', 'count': 276}
{'_id': 'tsarnick', 'count': 248}
{'_id': 'what_bugs_u', 'count': 246}
{'_id': 'Karen230683', 'count': 238}
{'_id': 'DarkPiano', 'count': 236}

Who are the five most grumpy (most negative tweets) and the most happy (most positive tweets)?
{'negative': [{'_id': 'lost_dog', 'count': 549},
              {'_id': 'tweetpet', 'count': 310},
              {'_id': 'webwoke', 'count': 264},
              {'_id': 'mcraddictal', 'count': 210},
              {'_id': 'wowlew', 'count': 210}],
 'positiv': [{'_id': 'what_bugs_u', 'count': 246},
             {'_id': 'DarkPiano', 'count': 231},
             {'_id': 'VioletsCRUK', 'count': 218},
             {'_id': 'tsarnick', 'count': 212},
             {'_id': 'keza34', 'count': 211}]}
 
