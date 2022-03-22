- [1. 자기소개](#1-자기소개)
- [2. 기술](#2-기술)
- [3. 공부정리](#3-공부정리)
  - [3.1 엔지니어](#31-엔지니어)
  - [3.2 개발](#32-개발)
  - [3.3 기타](#33-기타)
- [4. 참고자료 정리](#4-참고자료-정리)

<br>

# 1. 자기소개
컨테이너, 쿠버네티스, 파이썬 기반의 2년차 데브옵스 엔지니어입니다. 온프레미스 환경에서 쿠버네티스 구축과 장애처리, 쿠버네티스 기반인 인공지능 프로젝트 설계와 개발, 운영, CICD 구축 등을 해왔습니다. <br>
좋은 코드와 설계를 고민하기 위해 자기계발을 꾸준히 하고 있습니다. 커뮤니티 활동을 좋아하고 글쓰기를 좋아하여 블로그, 유튜브를 운영하고 있습니다. <br>
자동화를 통한 생산성 향상에 신경쓰고 적극적인 커뮤니케이션을 통해 문제를 해결하려고 노력합니다. 현재는 컨설턴트로 파견업무를 맡아 고객 서비스 성장을 지원하고 있습니다.
* 블로그: https://malwareanalysis.tistory.com
* 유투브: https://www.youtube.com/channel/UC7ctp-Pbn6y3J1VwtCtsnOQ

<br>

# 2. 기술
* python, fastapi, flask, appscheduler
* kubernetes, docker
* redis
* jenkins
* 업무에 사용하지 않았지만 아주얉게 개인공부로 했던 것들은 ...
  * springboot, springsecurity
  * vagrant
  * aws
  * vuejs
  * reactjs  

<br>

# 3. 공부정리
## 3.1 엔지니어
* Docker
  * [Add와 COPY명령어 차이](https://malwareanalysis.tistory.com/233)
  * docker 이미지레이어 분석 시리즈
    * [1편 도커 이미지 레이어 구조](https://malwareanalysis.tistory.com/213)
    * [2편 Dockerfile과 이미지 레이어 관계](https://malwareanalysis.tistory.com/234)
    * [3편 빌드캐시](https://malwareanalysis.tistory.com/236)
    * [4편 빌드과정에서 일어나는 일](https://malwareanalysis.tistory.com/222)
* kubernetes
  * [쿠버네티스 노드당 파드 갯수제한 확인 22.3.21](https://malwareanalysis.tistory.com/300)
  * [facebook 쿠버네티스 밋업 발표 22.3.19](https://github.com/choisungwook/facebook-meetup)
  * [KANS 쿠버네티스 네트워크 스터디 22.1 ~ 22.2](https://malwareanalysis.tistory.com/248)
  * 쿠버네티스 네트워크 스터디(페이스북 쿠버네티스 그룹에서 스터디 모집)
    * [1주차 1편 컨테이너 격리](https://malwareanalysis.tistory.com/248)
    * [1주차 2편 네트워크 네임스페이스](https://malwareanalysis.tistory.com/249)
    * [2주차 1편 Flannel CNI](https://malwareanalysis.tistory.com/254)
    * [2주차 2편 pause 컨테이너](https://malwareanalysis.tistory.com/255)
  * helm 시작하기 시리즈(21)
    * [1편 helm이란](https://malwareanalysis.tistory.com/193)
    * [2편 helm 설치](https://malwareanalysis.tistory.com/194)
    * [3편 helm차트 생성](https://malwareanalysis.tistory.com/195)
    * [4편 helm 차트 설치, 조회, 삭제](https://malwareanalysis.tistory.com/196)
    * [5편 helm 차트 템플릿 값 동적 수정](https://malwareanalysis.tistory.com/197)
    * [6편 values.yaml 오버라이딩](https://malwareanalysis.tistory.com/198)
    * [7편 Release Object사용](https://malwareanalysis.tistory.com/200)
    * [8편 namespace설정](https://malwareanalysis.tistory.com/201)
    * [9편 Release 업그레이드](https://malwareanalysis.tistory.com/202)
    * [10편 Rollback](https://malwareanalysis.tistory.com/203)
* [self-singed 인증서](documentation/linux_selfsigncert.md)
* [nvm으로 javascript 버전관리](https://malwareanalysis.tistory.com/145)
* [docker-mariadb 설치](https://malwareanalysis.tistory.com/140)
* [kubesrapy 온프레미스 설치](https://youtu.be/12vNy4IvF14)
* aws vpc, subnet: https://youtu.be/zG1WFhEV5x8, https://youtu.be/5zF_KXUNt-E
* [github action과 heroku를 이용한 빌드/배포 자동화](https://youtu.be/YMdwYPCyxRk)
* [프로메테스 익스포터 원리](https://youtu.be/iJyC6A38qwY)

## 3.2 개발
* 스프링부트
  * [keycloak 설치](documentation/springboot/keylcoak/keyclaok설치.md)
  * [h2 인모메리 설정](./documentation/springboot/inmemory_h2_configuration.md)
  * [Junit5 restcontroller 테스트](./documentation/springboot/junit5/restcontroller테스트.md)
  * [ResponseEntity Header추가](./documentation/springboot/ResponseEntity_addheader.md)
  * [JPA 참조](./documentation/springboot/jpa/참조.md)
  * [junit 매테스트 끝날때마다 repository 초기화](./documentation/springboot/jpa/junit5_aftereach.md)
  * [springboot-h2인메모리 콘솔접속](https://malwareanalysis.tistory.com/160)
* 스프링시큐리티
  * [filterchain](./documentation/springseucirty/filterchain.md)
  * [springsecurity-인메모리](./documentation/springseucirty/InmemoryUser.md)
  * [스프링시큐리티 강의 시리즈](https://www.youtube.com/watch?v=ewslpCROKXY&list=PL1mta2YyMpPUEidDzJ8kAxhMNhU9Is8Ky)
* flask
  * [애플리케이션 생성](./documentation/flask/create_application.md)
  * [requset_body가져오기](./documentation/flask/request_body.md)
  * [make_response로 응답수정](./documentation/flask/make_response.md)
* javascript
  * [문법정리](./documentation/javascript/Readme.md)
* vuejs
  * [vuetify 설치](./documentation/vuejs/vuetify/install.md)
  * [vuetify 컴퍼넌트](./documentation/vuejs/vuetify/required_vuetify_components.md)
  * [vuetify 페이지 추가](./documentation/vuejs/vuetify/helloworld.md)
  * [vuetify 사이드 네비게이션 메뉴와 라우터연동](./documentation/vuejs/vuetify/vlist-router.md)
* python
 * [python-sqlalchemy](https://malwareanalysis.tistory.com/141)
 * [python-input,stdin속도 비교](https://malwareanalysis.tistory.com/156)
## 3.3 기타
* [bash쉘스크립트-변수확인](https://malwareanalysis.tistory.com/158)

<br>

# 4. 참고자료 정리
* [추천자료 링크모음](./documentation/etc/추천자료.md)
* [UI링크모음](./documentation/etc/참고UI.md)
* [참고할 포트폴리오](./documentation/etc/다른사람포트폴리오.md)
