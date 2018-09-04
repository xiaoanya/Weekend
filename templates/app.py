from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
Bootstrap(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1111@localhost:3306/mydb?charset=utf8'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

class Grade(db.Model):
    __tablename__ = 'grades'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(20),nullable=False)
    students = db.relationship("Student",backref="grade")

    def __str__(self):
        return self.name

class Student(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    score = db.Column(db.Float)
    grade_id = db.Column(db.Integer,db.ForeignKey("grades.id"))

    def __str__(self):
        return self.name

migrate = Migrate(app,db)  # 实例化迁移对象
manager = Manager(app)
manager.add_command("db",MigrateCommand) # 添加迁移命令

@app.route('/')
def index():
    students = Student.query.all()
    # grade = Grade.query.all()
    return render_template("index.html", **locals())
@app.route('/add')
def add_student():

    return redirect(url_for("index"))


# @app.route('/login', methods=['POST', 'GET'])
# def login():
#     error = None
#     if request.method == 'POST':
#         if valid_login(request.form['username'],
#                        request.form['password']):
#             return log_the_user_in(request.form['username'])
#         else:
#             error = 'Invalid username/password'
#     # the code below is executed if the request method
#     # was GET or the credentials were invalid
#     return render_template('login.html', error=error)

if __name__ == '__main__':
    manager.run()
