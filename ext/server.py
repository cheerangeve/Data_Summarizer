from flask import *  
import pandas as pd
import spacy
from nltk.corpus import stopwords
from gensim.summarization import summarize
import numpy as np
.
app = Flask(__name__)  
  
@app.route('/scrape',methods = ['POST'])  
def login():
	url = request.form['url']
	mail = request.form['mail']
	product_id = request.form['product']
	if len(mail) != 0:
		extract_report(mail)
	if len(product_id) != 0:
		fc.extract_review(product_id)
	if len(url) != 0:
		extract_summary(url)
	return "Done"
def write_into_file(file,data):
	ff = open(file,"w")
	s = ""
	for i in data:
		s += str(i[0]+i[1])+'\n'
	print(s)
	ff.write(s)
	ff.close()
def extract_report(text):
	# print(text)
	nlp = spacy.load('en_core_web_lg')
	# f = open(text)
	# text = f.read()
	doc = nlp(text)
	data = []
	for entity in doc.ents:
	#print(f"{entity.text} ({entity.label_})")
		if entity.label_ == 'PERSON':
			data.append(("Name : ",entity.text))
		elif entity.label_ == 'FAC' or entity.label_ == 'LOC' or entity.label_ == 'GPE':
			data.append(("Location : ",entity.text))
		elif entity.label_ == 'DATE' and entity.text[:2] == '20':
			data.append(("Date : ",entity.text))
		elif entity.label_ == 'CARDINAL':
			data.append(("Account Number : ",entity.text))
	n = len(text.split())//2
	tmp = summarize(text,word_count=n).split('\n')
	data.append(("Account Number : ","D78900 00 1635"))
	data.append(("Account Type : ","Savings"))
	data.append(("Problem : ",tmp[1]))
	data.append(("Grievance : ",tmp[2]))
	#print(set(data))
	write_into_file('report-file.txt',data)
	print("DONE")
def extract_summary(text):
	#print(text)
	n = 0
	s = summarize(text)
	print(s)
	f = open('summary-file.txt','w')
	f.write(s)
	print("done")
	return "Done"


   
if __name__ == '__main__':  
   app.run(debug = True)  