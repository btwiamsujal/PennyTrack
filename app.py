from flask import Flask, render_template, redirect, url_for, flash, request
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from bson.objectid import ObjectId
from pymongo import MongoClient
from bson.errors import InvalidId
from flask_login import login_required
from forms import RegistrationForm, LoginForm

# -------------------- App Config --------------------
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

# MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
db = client.pennytrack
users_collection = db.users
expenses_collection = db.expenses

# -------------------- Login Manager --------------------
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Custom User class for Flask-Login
class User(UserMixin):
    def __init__(self, user_data):
        self.id = str(user_data['_id'])  # Must be str for Flask-Login
        self.username = user_data.get('username')
        self.email = user_data.get('email')

@login_manager.user_loader
def load_user(user_id):
    try:
        user_data = users_collection.find_one({'_id': ObjectId(user_id)})
        if user_data:
            return User(user_data)
    except (InvalidId, TypeError):
        return None

# -------------------- Routes --------------------

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # Check if email or username already exists
        existing_user = users_collection.find_one({
            '$or': [
                {'email': form.email.data},
                {'username': form.username.data}
            ]
        })

        if existing_user:
            flash('Username or email already exists.', 'danger')
            return redirect(url_for('register'))

        hashed_pw = generate_password_hash(form.password.data)
        user_id = users_collection.insert_one({
            'username': form.username.data,
            'email': form.email.data,
            'password': hashed_pw
        }).inserted_id

        flash("Account created! Please login.", "success")
        return redirect(url_for('login'))

    return render_template("register.html", form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user_data = users_collection.find_one({'email': form.email.data})
        if user_data and check_password_hash(user_data['password'], form.password.data):
            user = User(user_data)
            login_user(user)
            return redirect(url_for('dashboard'))
        else:
            flash("Invalid email or password.", "danger")
    return render_template("login.html", form=form)

@app.route('/dashboard')
@login_required
def dashboard():
    expenses = list(expenses_collection.find({'user_id': current_user.id}))
    for exp in expenses:
        exp['_id'] = str(exp['_id'])  # Convert ObjectId to str for HTML templates
    return render_template("dashboard.html", expenses=expenses)

@app.route('/add_expense', methods=['GET', 'POST'])
@login_required
def add_expense():
    if request.method == 'POST':
        category = request.form.get('category')
        amount = float(request.form.get('amount'))
        date = datetime.strptime(request.form.get('date'), '%Y-%m-%d')
        description = request.form.get('description', '')

        expenses_collection.insert_one({
            'user_id': current_user.id,
            'category': category,
            'amount': amount,
            'date': date,
            'description': description
        })

        flash("Expense added successfully!", "success")
        return redirect(url_for('dashboard'))

    return render_template("add_expense.html")

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You have been logged out.", "info")
    return redirect(url_for('login'))

# -------------------- Run --------------------
if __name__ == "__main__":
    app.run(debug=True)
