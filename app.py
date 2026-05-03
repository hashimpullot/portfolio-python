from flask import Flask, render_template
import json

app = Flask(__name__)

#Load porject data
def load_projects():
    with open('data/projects.json') as f:
        return json.load(f)
    
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    projects = load_projects()
    return render_template('projects.html', projects=projects)  

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)