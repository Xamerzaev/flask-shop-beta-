from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user

from shop import app
from shop.models import Product, User, db

from shop.forms import RegForm

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

@app.route('/login', methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    if request.method == 'POST':
        user = User.query.filter_by(email=request.form.get('email')).first()
        if user and user.email == request.form.get('email'):
            login_user(user)
            return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/reg', methods=['GET', 'POST'])
def reg():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegForm()
    if form.validate_on_submit():
        user = User(email=form.email.data, password=form.pasword.data)
        db.session.add(user)
        db.session.commit()
        login_user(user)
        flash('Регистрация прошла успешно!', 'success')
        return redirect(url_for('login'))      
    return render_template('reg.html', form=form)
    
@app.route('/index')
def home():
    products = Product.query.all()
    return render_template('index.html', products=products)

@app.route('/add_product', methods=['GET','POST'])
def add_product():
    if request.method == 'POST':
        f = request.form 
        file_name = request.files.get('image')   
        filename = secure_filename (file_name.filename)
        file_name.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        p = Product(title=f.get('title'),price=f.get('price'),category=f.get('category'),availibility=f.get('availibility'),description=f.get('description'),
        image=file_name.filename)  
        db.session.add(p)
        db.session.commit()
    return render_template('add_product.html')

@app.route('/products/<int:product_id>')
def product_detail(product_id):
    product = Product.query.get(product_id)
    return render_template('product_detail.html', product=product)