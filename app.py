from flask import Flask, render_template, request, redirect, url_for

# importing required modules 
import requests 
import base64
import os
  
# Enter your api key 
api_key = "Your_API_Key"
  
# url variable store url 
url = "https://maps.googleapis.com/maps/api/staticmap?"
  
# center defines the center of the map 
# equidistant from all edges of the mp.  
center = "12.8259,80.21607"
  
# zoom defines the zoom 
# level of the map 
zoom = 17
  
# get method of requests module 
# return response object 
PEOPLE_FOLDER = os.path.join('static', 'map_image')
  
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER
@app.route('/')
def index():
   return render_template("index.html")

@app.route('/image', methods=['GET', 'POST'])
def image():
        r = requests.get(url + "center=" + center + "&zoom=" +str(zoom)+ "&size="+"1280x720&scale=2&maptype=satellite&key="+api_key) 
        f = open(r'C:/Users/user/folder_name/static/map_image/map.png', 'wb') 
        f.write(r.content)
        f.close()  
        full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'map.png')
        return render_template("image.html", user_image = full_filename)


if __name__ == '__main__':
   app.run(debug=True)