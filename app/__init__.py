from flask import Flask, render_template
 
from flask_cors import CORS
 
app = Flask(__name__)
CORS(app, resources=r'/*')

app.debug = True
 

from app.main import main as main_blueprint
app.register_blueprint(main_blueprint)