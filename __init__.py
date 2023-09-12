from flask import Flask
app = Flask(__name__ , static_folder='./templates/blog_image')
import flaskr.main