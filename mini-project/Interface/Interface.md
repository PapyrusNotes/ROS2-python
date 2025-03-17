# 인터페이스

## 인터페이스 패키징
인터페이스로만 구성된 패캐지를 별도로 만들어 사용하는 거이 의존성면에서 관리하기 편하다.
인터페이스는 별도의 독립된 패키지로 구성해야한다.

## 실습
- msg 인터페이스
- srv 인터페이스
- action 인터페이스

ros2 pkg create 명령어를 사용해 msg_srv_action_interface_example 패키지를 만든다.
인터페이스 파일을 담을 msg, src, action 폴더를 생성한다.

cd ~/robot_ws/src
ros2 pkg create --build-type ament_cmake msg_srv_action_interface_example
cd msg_srv_action_interface_example
mkdir msg srv action

* ROS2 인터페이스 종류의 파일명은 CamelCased 규칙을 따른다.
* .msg, .srv, .action은 .h(pp)로 변환한 후 인터페이스 타입으로 구조체 및 타입으로 사용되기 때문이다.
EX ) action - ArithmeticChecker.action
EX )  msg - ArithmeticArgument.msg
EX ) src - ArithmeticOperator.srv

### 기본형식
fieldtype1 - fieldname1
fieldtype2 - fieldname2

### msg 인터페이스 데이터
- 토픽 데이터 , Topic data

### srv 인터페이스 데이터
- 서비스 요청, request
- 서비스 응답, response

### action 인터페이스 데이터
- 액션 목표 = goal
- 액션 결과 = result
- 액션 피드백 = feedback

## 빌드
### 패키지 설정 파일 package.xml
- 일반적인 패키지와 다른 점은,
DDS에서 사용되는 IDL(Interface Definition Langauge)생성과 관련한
rosidl_default_generators가 사용된다.

- 실행 시에 builtin_interfaces와 rosidl_default_runtime이 사용된다.

### 빌드 설정 파일 CMakeList.txt
