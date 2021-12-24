from shop import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column (db.Integer(), primary_key=True)
    title = db.Column (db.String(), nullable = False)
    price  = db.Column (db.Integer(), nullable = False)
    category  = db.Column (db.String(), nullable = False)
    availibility  = db.Column (db.String(), nullable = False)
    description  = db.Column (db.Text(), nullable = False)
    image = db.Column (db.String(), nullable = False)
    cartitems = db.relationship('CartItem', backref='Product')

    def __repr__(self):
        return self.title


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column (db.Integer(), primary_key=True)
    email = db.Column (db.String(), nullable = False, unique = True)
    password = db.Column (db.String(), nullable = False)
    IsAdmin = db.Column (db.Boolean, default = False)
    cartitems = db.relationship('CartItem', backref='User')

    def __repr__(self) -> str:
        return self.email

class CartItem(db.Model):
    __tablename__='cartitems'
    id = db.Column(db.Integer,primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
