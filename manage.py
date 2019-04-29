#!/home/ai/Documents/My_companies_apporach/github/Count_top_words/word_count/bin/python3 

from app import *

if __name__ == "__main__":
	
	db.create_all()
	app.run(host="0.0.0.0", debug=True) 
   