import MySQLdb

import pickle
with open('mydb.dat','rb') as obj:
    config = pickle.load(obj)
