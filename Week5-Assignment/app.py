from flask import Flask
from flask import Flask,request
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Session
from sqlalchemy import exc

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///database.sqlite3'
db=SQLAlchemy()
db.init_app(app)
app.app_context().push()

class course(db.Model):
    __tablename__='course'
    course_id = db.Column(db.Integer,autoincrement=True,primary_key=True)
    course_code = db.Column(db.String, unique=True,nullable=False)
    course_name = db.Column(db.String, unique=True)
    course_description = db.Column(db.String, unique=True)
    students = db.relationship('enrollments',backref='students')
      
class student(db.Model):
    __tablename__='student'
    student_id = db.Column(db.Integer,autoincrement=True,primary_key=True)
    roll_number = db.Column(db.String,nullable=False)
    first_name = db.Column(db.String,nullable=False)
    last_name = db.Column(db.String)  
    courses = db.relationship('enrollments',backref='courses')
      
class enrollments(db.Model):
    __tablename__='enrollments'
    enrollment_id = db.Column(db.Integer,autoincrement=True,primary_key=True)
    estudent_id = db.Column(db.Integer,db.ForeignKey("student.student_id"),nullable=False)
    ecourse_id = db.Column(db.Integer,db.ForeignKey("course.course_id"),nullable=False)

db.create_all() 

@app.route("/", methods=["GET","POST"])    
def launch():
    print("Inside launch method")
    students = student.query.all()
    return render_template("index.html",students=students)
    
@app.route("/student/create", methods=["GET"])    
def addStudent():
    print("Inside addStudent method")
    return render_template("addStudent.html")
    
@app.route("/student/create", methods=["POST"])    
def addStudentConfirm():
    print("Inside addStudentConfirm method")
    roll = request.form['roll']
    firstName = request.form['f_name']
    lastName = request.form['l_name']
    course1 = request.form.getlist('courses')
    print(course1);

    try:
        
       #add the course in filter list and get the course object from db 
        student_obj = student(roll_number=roll,first_name=firstName,last_name=lastName)
        db.session.add(student_obj)
        
        if len(course1)>0:
            for code in course1:
                print(code)
                enrollment_obj=enrollments(estudent_id=roll,ecourse_id=int(code[7]))
                student_obj.courses.append(enrollment_obj)
                
        db.session.commit()
    
    except exc.IntegrityError:
        db.session.rollback()
        return render_template('error.html',msg='Roll_No should be unique. Try adding with a unique roll number.')
        
    except Exception as err:
        print(err)
        db.session.rollback()
        return render_template('error.html',msg='An error occoured. Student not added. Try Again')
    

    
    return render_template("index.html")


if __name__=='__main__':
    app.run(host='0.0.0.0',debug=True,port=8080)
    
