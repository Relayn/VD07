# run.py
import os
from app import app

app.template_folder = os.path.join(os.path.dirname(__file__), 'templates')

if __name__ == '__main__':
    app.run(debug=True)
