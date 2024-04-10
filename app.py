from flask import Flask, render_template, request
from college_search import get_colleges

app = Flask(__name__)

# Define routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/search_colleges', methods=['POST'])
@app.route('/search_colleges', methods=['POST'])
def search_colleges():
    state = request.form['state']
    city = request.form['city']
    
    colleges = get_colleges(state, city)
    
    return render_template('result.html', colleges=colleges)

if __name__ == '__main__':
    app.run(debug=True)