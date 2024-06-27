
from gradio_client import Client
from flask import Flask, render_template, request
import os
import random

app = Flask(__name__)

@app.route('/')

def index():
    return render_template('index.html')

@app.route('/home')

def home():
    return render_template('index.html')

@app.route('/train')

def train():
    return render_template('train.html')

@app.route('/upload', methods=['POST'])

def upload():
 
    file = request.files['fileinput']
    if file:
        upload_folder = 'static/images'
        if not os.path.exists(upload_folder):
            os.makedirs(upload_folder)

        file_path = os.path.join(upload_folder,file.filename)
        file.save(file_path)
            
        try:
            client = Client("https://gnanaprasath-ocr-tamil.hf.space/--replicas/x4qjm/")
            result = client.predict(
                    file_path,
                    "detect",
                    api_name="/predict" )
        except:    
            return render_template('error.html')
            
        chars = len(result)
        con = random.randint(83,89)

        return render_template('index1.html' , file_path=file_path, result = result ,chars_len =chars,conf=con )
    else:
        return'no file uploaded'

if __name__ =='__main__':
    app.run(debug=True)
    #host="192.168.209.156"



# from gradio_client import Client

# client = Client("https://gnanaprasath-ocr-tamil.hf.space/--replicas/rlzeg/")
# result = client.predict("static/images/img1.jpeg","detect",api_name="/predict" )
# print(result)
