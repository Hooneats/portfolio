# -*- coding: utf-8 -*-
from db.db import db

class JenkinsJob(db.Model):
    '''
        젠킨스 잡
    '''
    __tablename__  = 'jenkins_job'

    id = db.Column(db.Integer, primary_key=True)
    app_id = db.Column(db.Integer, db.ForeignKey('service_app.id'), nullable=False)
    last_status = db.Column(db.String(20), nullable=False)
    job_name = db.Column(db.String(200), nullable=False)

    def __init__(self, app_id, job_name, last_status=None):
        self.app_id = app_id
        self.self_name = job_name
        self.last_status = last_status

    def change_status(self, status):
        self.last_status = status

# class BuildHistory(db.Model):
#     '''
#         빌드 히스토리 관리
#     '''
#     __tablename__  = 'build_history'
    
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
#     project_id = db.Column(db.Integer, db.ForeignKey('service_project.id'), nullable=False)

#     def __init__(self, flaskuser_id, project_id):
#         self.user_id = flaskuser_id
#         self.project_id = project_id