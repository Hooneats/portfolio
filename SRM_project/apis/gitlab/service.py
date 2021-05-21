# -*- coding: utf-8 -*-
from abc import *
import requests
import json
from urllib.parse import urljoin
from logger.log import log
from pathlib import Path
import os
from apis.auth.models import User
from apis.auth.service import get_userByEmail
from config.gitlab_config import get_GitlabAccessToken, get_GitlabInitPassword, get_gitlabURI, get_default_memberexpires_data
from .models import ServiceProject, UserProjectMappingEntity
from db.db import db
from apis.auth.models import GitlabUser
from config.gitlab_config import get_pythonappId, get_springbootappId

class AbstractGitlab(metaclass=ABCMeta):
    '''
        gitlab서비스클래스 추상화
    '''

    # gitlab API를 사용하기 위한 accesstoekn 설정
    accesstoken = get_GitlabAccessToken() # this is for sample
    gitlabURI = get_gitlabURI()
    initpassword = get_GitlabInitPassword()
    
    @abstractmethod
    def createGroup(self, post_data, requsetuser_information):
        '''
            그룹 생성
            파라미터:
                post_data: CreateGroupRequestDto class.__dict__
                requsetuser_information: 프로젝트 생성 요청자의 이메일
        '''
        pass

    @abstractmethod
    def getUsers(self):
        '''
            gitlab 계정목록 조회
        '''
        pass

    def addMembersToGroup(self, group_id, gitlabuser_id):
        '''
            Group 멤버 추가
            파라미터:
                group_id: gitlab group ID
                user_id: gitlab user_id
        '''    
        pass

    def getUserByflaskuserID(self, flaskuser_id):
        '''
            flask userid로 gitlab user조회
        '''
        pass

    # def forkProject(self, createAppRequestDto):
    #     '''
    #         앱타입에 맞는 프로젝트 fork
    #     '''
    #     pass

class GitlabImpl(AbstractGitlab):
    def __init__(self):
        pass

    def createGroup(self, post_data, requsetuser_information):
        '''
            그룹생성
            파라미터:
                post_data: CreateGroupRequestDto class.__dict__
                requsetuser_information: 프로젝트 생성 요청자의 이메일
        '''

        URI = urljoin(self.gitlabURI, "groups")
        headers = {"Authorization": "Bearer {}".format(self.accesstoken)}

        result = {
            'status': False,
            'data': None
        }

        try:
            
            api_response = requests.post(URI, headers=headers, data=post_data)
            result['status'] = api_response.ok

            if not result['status']:
                log.error('[Error 311] gitlab 그룹 생성 실패')
            else:
                log.debug("[debug 001] {} 그룹생성 성공".format(post_data['name']))
                result['data'] = api_response.json()
                result['status'] = True

            # db 등록
            login_user = get_userByEmail(requsetuser_information)
            project = ServiceProject(result['data']['id'], result['data']['web_url'], result['data']['name'])
            db.session.add(project)
            db.session.commit()

            user_project_mapping = UserProjectMappingEntity(flaskuser_id=login_user.id, project_id=project.id)
            db.session.add(user_project_mapping)
            db.session.commit()

            gitlabuser = self.getUserByflaskuserID(login_user.id)
            self.addMembersToGroup(result['data']['id'], gitlabuser.gitlab_userid)

            log.info("그룹{} DB 등록 성공".format(post_data['name']))

        except Exception as e:
            log.error("[Error 310] gitlab 그룹생성 실패: {}".format(e))
        
        return result

    def addMembersToGroup(self, group_id, gitlabuser_id):
        '''
            Group 멤버 추가
            파라미터:
                group_id: gitlab group ID
                user_id: gitlab user_id
        '''

        result = False

        try:
            
            URI = urljoin(self.gitlabURI, "groups/{}/members".format(group_id))
            headers = {"Authorization": "Bearer {}".format(self.accesstoken)}
            
            data = {
                "id": group_id,
                "user_id": gitlabuser_id,
                "access_level": "30",
                "expires_at": get_default_memberexpires_data()
            }

            api_response = requests.post(URI, headers=headers, data=data)
            
            if api_response.ok:
                result = True

        except Exception as e:
            log.error("[Erorr 312] gitlab Group에 계정추가 실패 :{}".format(e))

        return result

    def existUser(self, email):
        '''
            flask user가 존재하는지 확인
        '''
        log.debug("---------------------")
        log.debug(email)
        return User.query.filter_by(email=email).first()

    def existGitlabUser(self):
        '''
            gitlab User가 존재하는지 확인
        '''
        pass
    
    def getUsers(self):
        '''
            gitlab 계정목록 조회
        '''
        
        response = {
            'status': False,
            'data': []
        }

        try:
            URI = urljoin(self.gitlabURI, "users")
            headers = {"Authorization": "Bearer {}".format(self.accesstoken)}
            api_response = requests.get(URI, headers=headers)
            
            response['status'] = api_response.ok

            if not response['status']:
                log.debug('[Error 301] 계정목록 조회실패. 응답코드: {}'.format(response['status']))
            else:
                log.debug("[OK] 계정목록 조회 성공")
                response['data'] = api_response.json()

        except Exception as e:
            log.error('[Error 300] 계정목록 조회실패: {}'.format(e))

        return response

    def getUserByflaskuserID(self, flaskuser_id):
        '''
            flask userid로 gitlab user조회
        '''
        return GitlabUser.query.filter_by(user_id=flaskuser_id).first()

    # def forkProject(self, createAppRequestDto):
    #     '''
    #         앱타입에 맞는 프로젝트 fork
    #     '''

    #     # fork할 앱 id
    #     if createAppRequestDto.app_type is "python":
    #         id = get_pythonappId()
    #     elif createAppRequestDto.app_type is "springboot":
    #         id = get_springbootappId()

    #     # group ID
    #     User.query.filter_by(email=createAppRequestDto.requet_user_eamil).first()

    #     post_data = {
    #         "id": id, # fork 대상
    #         "name": createAppRequestDto.name,
    #         "path": createAppRequestDto.name,
    #         "namespace_id": "37" # gitlab group ID
    #     }

        
    #     pass