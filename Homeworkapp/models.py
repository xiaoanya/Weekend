from flask_sqlalchemy import SQLAlchemy

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