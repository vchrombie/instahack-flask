from flask import Flask,render_template,request
import requests
from bs4 import BeautifulSoup
import urllib

app= Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
	if request.method=='POST': # basic Flask structure 
		url=request.form['iurl'] 
		raw=requests.get(url) # make a request to the URL
		soup=BeautifulSoup(raw.text,'html.parser') # get the HTML

		links= soup.find(property="og:image") #f ind meta with property=og:image		
		# "og:video" if you want to download a video
		
		image=links.get('content') # get its content
		# urllib.request.urlretrieve(image, "img.jpg")  # save it as img.jpg

		# return in the browser
		while image!='':
			return '<img src="'+image+'"'+ 'align="center">' # insert content in img tag

	return render_template('index.html')

if __name__=='__main__':
	app.run()
