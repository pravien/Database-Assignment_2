import webget
import zipfile
import pymongo
from pymongo import MongoClient
import subprocess
import os
import pprint
import re

def populate_db(file):
    subprocess.run(["mongoimport",
                     "--drop",
                     "--db",
                     "social_net",
                     "--collection",
                     "tweets",
                     "--type",
                     "csv",
                     "--file",
                     file,
                     "--fields",
                     "polarity,id,date,query,user,text"
    ])

def pp(obj):
    pprint.pprint(obj)

def ppall(col):
    for p in col:
        pp( p )

def q1():

    return len(tweets.distinct("user"))

def q2():
    pipeline_2 = [
                {
                    '$match':{
                        'text':{
                            '$regex':'@\w+'
                        }
                    }
                },
                {
                    '$group':{
                        '_id':'$user',
                        'links':{
                            '$sum':1
                        }
                    }
                },
                {
                    '$sort':{
                        'links': -1
                    }
                },
                {
                '$limit': 10
                }
    ]
    return tweets.aggregate(pipeline_2)

def q3():
    pipeline_3 = [
                {
                    '$match':{
                        'text':{
                            '$regex':'@\w+'
                        }
                    }
                }
    ]
    temp_dict={}
    for p in tweets.aggregate(pipeline_3):
        #print(p['text'])
        #print(re.findall("@\w+", p['text']))
        for user in re.findall(r'@\w+', p['text']):
            if user in temp_dict:
                temp_dict[user]+=1
            else:
                temp_dict[user]=0
    s = [(k, temp_dict[k]) for k in sorted(temp_dict, key=temp_dict.get,
     reverse=True)]
    for i in range(0,5):
        print(s[i])


def q4():
    pipeline_4 = [
        {
            '$group':{
                '_id':'$user',
                'count':{
                    '$sum':1
                }
            }
        },
        {
            '$sort':{
                'count': -1
            }
        },
        {
        '$limit': 10
        }
    ]
    return tweets.aggregate(pipeline_4)

def q5():
    pipeline_5=[
        {
            '$facet':
                {
                    'negative':[
                            {
                                '$match':{
                                    'polarity':{
                                            '$eq':0
                                    }
                                }
                            },
                            {
                                '$group':{
                                    '_id' : '$user',
                                    'count' : {
                                        '$sum' : 1
                                    }
                                }
                            },
                            {
                                '$sort':{
                                    'count': -1
                                }
                            },
                            {
                            '$limit': 5
                            }
                    ],
                    'positiv':[
                        {
                            '$match':{
                                'polarity':{
                                        '$eq':4
                                }
                            }
                        },
                        {
                            '$group':{
                                '_id' : '$user',
                                'count' : {
                                    '$sum' : 1
                                }
                            }
                        },
                        {
                            '$sort':{
                                'count': -1
                            }
                        },
                        {
                        '$limit': 5
                        }
                    ]
                }
        }
    ]
    return tweets.aggregate(pipeline_5)


if __name__ == '__main__':
    webget.download("http://cs.stanford.edu/people/alecmgo/trainingandtestdata.zip")
    zip_ref = zipfile.ZipFile('./trainingandtestdata.zip', 'r')
    zip_ref.extractall()
    zip_ref.close()
    cwd = os.getcwd()
    path_2_file = os.path.join(cwd,"training.1600000.processed.noemoticon.csv")
    client = MongoClient()
    db = client.social_net
    tweets = db.tweets
    populate_db(path_2_file)
    print('How many Twitter users are in the database?')
    print("Result : ",q1())
    print()
    print('Which Twitter users link the most to other Twitter users?')
    ppall(q2())
    print()
    print('Who is are the most mentioned Twitter users? (Provide the top five.)')
    q3()
    print()
    print('Who are the most active Twitter users (top ten)?')
    ppall(q4())
    print()
    print('Who are the five most grumpy (most negative tweets) and the most happy (most positive tweets)?')
    ppall(q5())
