#This code collect some data and past it in a Django webserver

#! /usr/bin/env python3
import os
import requests

list_of_files = os.listdir('/data/feedback')
for file in list_of_files:
        fp = open('/data/feedback/'+file)
        data = fp.read()
        data = data.split('\n')
        dic = {"title":data[0], "name":data[1], "date":data[2], "feedback":data[3]}
        response = requests.post('http://104.197.6.205/feedback/', json=dic)
        print(response.status_code)
