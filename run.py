from flask import Flask
from flask_restful import Resource, Api ,reqparse, abort, request
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
import os
from sqlalchemy.orm import sessionmaker
from marshmallow_sqlalchemy import ModelSchema
import json


SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}/{database}?charset=utf8'.format(
    **{
      'user': os.getenv('DB_USER', 'root'),
      'password': os.getenv('DB_PASSWORD', 'root'),
      'host': os.getenv('DB_HOST', '172.20.0.1'),
      'database': os.getenv('DB_DATABASE', 'sample01'),
    })

    
engine = create_engine(SQLALCHEMY_DATABASE_URI)

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'
 
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
 
    def __repr__(self):
        return "<Student(id='%s', name='%s')>" % (self.id, self.name)


class StudentSchema(ModelSchema):
    class Meta:
        model = Student
 
# テーブルの作成
# テーブルがない場合 CREATE TABLE 文が実行される
Base.metadata.create_all(engine)  # 作成した engine を引数にすること



# SQLAlchemy はセッションを介してクエリを実行する
Session = sessionmaker(bind=engine)
session = Session()



app = Flask(__name__)
api = Api(app)



class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


class StudentListAPI(Resource):
    def get(self):
        query = session.query(Student).all()
        result = StudentSchema(many=True).dump(query)
        return result
    def post(self):
        args = request.json
        student_name = args["name"]
        session.add(Student(name=student_name))
        session.commit()
        return student_name

class StudentIdAPI(Resource):
    def get(self,index):
        result = session.query(Student).get(index)
        if result is None:
            abort(404)

        res = StudentSchema().dump(result)
        return res

    def put(self,index):
        result = session.query(Student).get(index)
        if result is None:
            abort(404)
        args = request.json
        new_student_name = args["name"]
        result.name = new_student_name
        session.commit()
        new_result = session.query(Student).get(index)
        res = StudentSchema().dump(new_result)
        return res

    def delete(self,index):
        result = session.query(Student).get(index)
        if result is None:
            abort(404)
        session.delete(result)
        session.commit()
        return None, 204


api.add_resource(HelloWorld, '/hello')
api.add_resource(StudentListAPI,'/student')
api.add_resource(StudentIdAPI,'/student/<index>')

#author aoi nakamura


if __name__ == '__main__':
    app.run(debug=True)

