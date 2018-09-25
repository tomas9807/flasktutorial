import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config():
    SECRET_KEY = os.environ.get('SECRET KEY') or 'fuck you'
    DATABASE_URI = os.environ.get('DATABASE_URL') or os.path.join(BASE_DIR,'app.db')
    