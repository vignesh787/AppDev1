from flask import Flask,request
from flask_restful import Resource,Api
from flask_sqlalchemy import SQLAlchemy


app=Flask(__name__)
api=Api(app)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///database.sqlite3'
db=SQLAlchemy()
db.init_app(app)
app.app_context().push()

class student_table(db.Model):
    __tablename__="student"
    student_id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    roll_number=db.Column(db.String,unique=True,nullable=False)
    first_name=db.Column(db.String,nullable=False)
    last_name=db.Column(db.String)
    course=db.relationship('enrollments_table',backref='students')
    
class course_table(db.Model):
    __tablename__='course'
    course_id=db.Column(db.Integer,primary_key=True, autoincrement=True)
    course_code=db.Column(db.String,unique=True, nullable=False)
    course_name=db.Column(db.String,nullable=False)
    course_description=db.Column(db.String)
    students=db.relationship('endollments_table',backref='courses)
    
class enrollments_table(db.Model):
    __tablename__='enrollment'
    enrollment_id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    student_id=db.Column(db.Integer,db.ForeignKey('student.student_id'),nullable=False)
    course_id=db.Column(db.Integer,db.ForeignKey('course.course_id'),nullable=False)
    
class student(Resource):

    def get[self,student_id]:
        try:
            student_obj=student_Table.query.filter(student_table.student_id==student_id).first()
            if student_obj:
                return('student_id':student_obj.student_id,'first_name':student_obj.first_name,'last_name':student_obj.last_name,'roll_number':student_obj.roll_number),200
            else:
                return '',404
                
        except Exception as err:
            return '',500
            
    def put(self,student_id):
        try:
            try:
                f_name=request.form['first_name']
                if type(f_name)!=str or len(f_name)<1:
                    return('error_code':'STUDENT002','error_message':'First Name is required and should be a string'),400
            except:
                return('error_code':'STUDENT002','error_message':'First Name is required and should be a string'),400
            
            try:
                roll_no=request.form['roll_number']
                if type(roll_no)!=str or len(roll_no)<1:
                    return('error_code':'STUDENT001','error_message':'Roll Number is required and should be a string'),400
            except:
                return('error_code':'STUDENT001','error_message':'Roll Number is required and should be a string'),400
                
                
            try:
                l_name=request.form['last_name']
                if type(l_name)!=str or len(l_name)<1:
                    return('error_code':'STUDENT003','error_message':'Last Name is required and should be a string'),400
            except:
                l_name=''
                
                
            student_obj=student_Table.query.filter(student_table.student_id==student_id).first()
            
            if student_obj:
                student_obj.first_name=f_name
                student_obj.last_name=l_name
                student_obj.roll_number=roll_no\
                
                db.session.commit()
                return('student_id':student_obj.student_id,'first_name':student_obj.first_name,
                'last_name':student_obj.last_name,'roll_number':student_obj.roll_number),200
            else:
                return '',404
        except:
            return '',500
            
            
    def delete(self,student_id):
        try:
            student_obj=student_table.query.filter(student_table.student_id==student_id).first()
            if student_obj:
                e_obj=enrollments_table.query.filter(enrollments_Table.student_id==student_id).all()
                for i in e_obj:
                    db.session.delete(i)
                db.session.delete(student_obj)
                db.session.commit()
                return '',200
            else:
                return '',404
        except:
            return '',500
            
class enrollments(Resource):
    def get(self,student_id):
        try:
            student_obj=student_table.query.filter(student_table.student_id==student_id).first()
            if student_obj:
                entollments_obj=enrollments_table.quer.filter(enrollments_Table.student_id==student_id).all()
                if enrollments_obk:
                    ana=[]
                    for i in enrollments_obj:
                        ana.append(('enrollments_id':i.enrollments_id,'student_id':i.student_id,'course_id':i.course_id))
                    return ana,200
                else:
                    return '',404
            else:
                return('error_code':'Enrollments002','error_message':'Student does not exists'),400
        except:
            return '',500
            
    def post(self,student_id):
        try:
            try:
                
        

class course(Resource):
        def get(sefl,course_id):
            try:
                course_obj=course_table.query.filter(course_table.course_id==course_id).first()
                if course_obj:
                    return ('course_id':course_obj.course_id,'course_name':course_obj.course_name,'course_code':course_obj.course_code,'course_description':course_obj.course_description)
                else:
                    return '',404
            except:
                return '',500
                
        def put(self,course_id):
            try:
                try:
                    c_name=request.form['course_name']
                    if type(c_name_!=str or len[c_name]<1:
                        return ('error_code':'COURSE001','error_message':'Course Name is required and should be string.'),400
                except:
                    return ('error_code':'Course001','error_message':'Course Name is required and shoulf be string.'),400
                    
                try:
                    c_code=request.form['course_code']
                    if type(c_code)!=str or len[c_code]<1:
                        return ('error_code':'COURSE002','error_message':'Course Code is required and should be string.'),400
                except:
                    return ('error_code':'Course002','error_message':'Course Code is required and shoulf be string.'),400
                
                try:
                    c_desc=request.form['course_description']
                    if type(c_desc)!=str or len[c_code]<1:
                        return ('error_code':'COURSE003','error_message':'Course Description is required and should be string.'),400
                except:
                    c_Desc=''
                    
                    
                    
                course_obj=course_table.query.filter(course_Table.course_id==course_id).first()
                if course_obj:
                    course_obj.course_name=c_name
                    course_obj.course_code=c_code
                    course_obj.course_description=c_desc
                    
                db.session.commit()
                return('course_id':course_obj.course_id','course_name':course_obj.course_name,'course_code':course_obj.course_code,'couse_description':course_obj.course_description),200
                else:
                    return '',404
            except:
                return '',500 
                
class add_course(Resource):
        def post(self):
            try:
                try:
                    c_name=request.form['course_name']
                    if type(c_name_!=str or len[c_name]<1:
                        return ('error_code':'COURSE001','error_message':'Course Name is required and should be string.'),400
                except:
                    return ('error_code':'Course001','error_message':'Course Name is required and shoulf be string.'),400
                    
                try:
                    c_code=request.form['course_code']
                    if type(c_code)!=str or len[c_code]<1:
                        return ('error_code':'COURSE002','error_message':'Course Code is required and should be string.'),400
                except:
                    return ('error_code':'Course002','error_message':'Course Code is required and shoulf be string.'),400
                
                try:
                    c_desc=request.form['course_description']
                    if type(c_desc)!=str or len[c_code]<1:
                        return ('error_code':'COURSE003','error_message':'Course Description is required and should be string.'),400
                except:
                    c_Desc=''
                    
                    
                    
                test_course=course_table.query.filter(course_table.course_code==c_code).first()
                if test_course:
                    return ''.409
                else
                    course_obj=course_table(course_name=c_name,course_code=c_code,course_description=c_desc)
                    db.session.add(course_obj)
                    db.session.commit()
                    
                return('course_id':course_obj.course_id','course_name':course_obj.course_name,'course_code':course_obj.course_code,'couse_description':course_obj.course_description),200
                else:
                    return '',404
            except:
                return '',500                 


api.add_resource(course,'/api/course/<int:course_id>')
api.add_resource(student,'/api/student/<int:student_id>')
api.add_resource(enrollments,'/api/student/<int:student_id/course')
api.add_resource(enrollments_,'/api/student/<int:student_id>/course/<int:course_id>')
api.add_resource(add_student,'/api/student/')
api.add_resource(add_course,'/api/course')


if __name__=='__main__':
    app.run()
