from shop import app
from flask import render_template

@app.route('/')
def index():
    return render_template ('index.html')

@app.route('/shop')
def shop():
    return render_template ('shop.html')

app.route('/furniture')
def furniture():
    return render_template ('furniture.html')

app.route('/contact')
def contact():
    return render_template ('contact.html')