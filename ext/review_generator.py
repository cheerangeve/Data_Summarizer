import pandas as pd
from gensim.summarization import summarize
import random
import web_scrapper as ws
import re

import json 
import csv 

def convert_json_to_csv():

	with open('data.json') as json_file: 
		data = json.load(json_file) 

	employee_data = data[0]['reviews']
	data_file = open('data_file.csv', 'w') 
	csv_writer = csv.writer(data_file) 
	count = 0

	for emp in employee_data: 
		if count == 0: 
 
			header = emp.keys() 
			csv_writer.writerow(header) 
			count += 1

		csv_writer.writerow(emp.values()) 

	data_file.close() 
def extract_review(product_id):
	ws.ReadAsin(product_id)
	convert_json_to_csv()

	my_csv = pd.read_csv('data_file.csv',encoding= 'unicode_escape')
	content = my_csv['review_text']
	rating = my_csv['review_rating']
	reviews = ""
	rate = 0
	var = []
	n = len(content)
	for i in range(n):
		reviews += content[i] + ","
		rate += float(rating[i])
	tmp = summarize(reviews,word_count=50).split(",")
	s = ""
	for i in tmp:
		print(i)
		s += i+'\n'
	print("Overall rating of the product is : %.1f"%(rate/n))
	s += "Overall rating of the product is : "+str((rate/n))
	f = open('review-file.txt','w')
	f.write(s)
	f.close