from flask import render_template, request
from werkzeug.utils import secure_filename
from shop.models import Product,db
from shop import app
import os

@app.route('/')
def index():
    products = Product.query.all()
    return render_template('index.html', products=products)

@app.route('/shop')
def shop():
    products = Product.query.all()
    return render_template('shop.html', products=products)

@app.route('/furniture')
def furniture():
    return render_template ('furniture.html')

@app.route('/contact')
def contact():
    return render_template ('contact.html')

@app.route('/about')
def about():
    return render_template ('about.html')

@app.route('/index')
def home():
    products = Product.query.all()
    return render_template('index.html', products=products)

@app.route('/add_product', methods=['GET','POST'])
def add_product():
    if request.method == 'POST':
        f = request.form 
        file_name = request.files.get('image')   
        filename = secure_filename(file_name.filename)
        file_name.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        p = Product(title=f.get('title'),price=f.get('price'),category=f.get('category'),availibility=f.get('availibility'),description=f.get('description'),
        image=file_name.filename)  
        db.session.add(p)
        db.session.commit()
    return render_template('add_product.html')