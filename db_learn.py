import sqlite3
from flask import *
import os
# pip install opencv-python
# import cv2
# from werkzeug.utils import secure_filename

app = Flask(__name__)


def connect_to_db():
    conn = sqlite3.connect("my.db")
    conn.row_factory = sqlite3.Row
    
    return conn


def filling_db():
    connect = connect_to_db()
    cursor = connect.cursor()
    
    cursor.execute("DROP TABLE IF EXISTS cities")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS cities (
        id INTEGER, 
        name_ VARCHAR(50), 
        population_ INTEGER, 
        description_ TEXT, 
        year_of_foundation DATE, 
        image_ VARCHAR(255)
    )
    """
    )
    cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS users (     
        id INTEGER, 
        name TEXT, 
        password VARCHAR(50), 
        login VARCHAR(50),
        years_old INTEGER, 
        description TEXT
    )
    '''
    )

    cursor.execute("INSERT INTO cities (id, name_, population_, description_, year_of_foundation, image_) VALUES (1, 'Одеса', 1000000, 'Перлина у моря', 1794, 'https://osama.com.ua/wp-content/uploads/2021/12/36.jpg')")
    cursor.execute("INSERT INTO cities (id, name_, population_, description_, year_of_foundation, image_) VALUES (2, 'Київ', 3000000, 'Столиця України', 430, 'https://www.nta.ua/wp-content/uploads/2022/02/kyyiv.jpg')")

    connect.commit()
    
  
@app.route("/")
def index():
    connect = connect_to_db()
    cursor = connect.cursor()
    
    cursor.execute("SELECT * FROM cities")
    sities = cursor.fetchall()
    
    return render_template('index.html', sities=sities)

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == 'POST':
        # connect = connect_to_db()
        # cursor = connect.cursor()
        
        # password = request.form.get('password')
        # login = request.form.get('login')
        
        # cursor.execute("""INSERT INTO users (password, login)
        #              VALUES (?,?)""", [login, password])
        # connect.commit()

        # print(password, login)
        flash("Hello, world)")
        
    return render_template('register.html')


@app.route("/users")
def users():
    connect = connect_to_db()
    cursor = connect.cursor()
    
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    
    return render_template('users.html', users = users)





def main():
    #filling_db()
    app.config['SECRET_KEY'] = 'the random string'  
    app.run(debug=True)

if __name__ == '__main__':
    main()