from flask import Flask, render_template  # Fixed import statement
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'roottoor'
app.config['MYSQL_DB'] = 'chandan_ece'
mysql = MySQL(app)

@app.route("/", methods=["GET"])
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM peoples")
    results = cur.fetchall()
    cur.close()
    return render_template("index.html", result=results)

@app.route("/about", methods=["GET"])
def about():
    return render_template("about.html")

@app.route("/blog", methods=["GET"])
def blog():
    return render_template("blog.html")

@app.route("/contact", methods=["GET"])
def contact():
    return render_template("contact.html")

# FIXED this line:
if __name__ == '__main__':  # Corrected from 'main' to '__main__'
    app.run(debug=True)     # Added debug=True for development

