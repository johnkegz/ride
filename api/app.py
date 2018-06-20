"""
This is the main module
"""
import os
import sys
from flask import Flask
sys.path.append(os.path.pardir)
from urls import Get_urls



APP = Flask(__name__)
APP.env = 'development'
APP.testing = True

Get_urls.fetch_urls(APP)

if __name__ == '__main__':
    APP.run(debug=True)
