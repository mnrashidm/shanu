# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 13:37:50 2021

@author: shanu
"""

import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'experience':2, 'test_score':9, 'interview_score':6})

print(r.json())