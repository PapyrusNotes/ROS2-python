# Package 생성

## 작업폴더 구성
- /home/{사용자 디렉터리 robot_ws}/ 생성
- /home/robot_ws/{src 디렉터리} 생성

## 소스코드 복사
- ~/robot_ws # cd src
- ~/robot_ws/src # git clone https://github.com/ros2/teleop_twist_joy.git

## helloworld 패키지 생성
- ~/robot_ws/src # ros2 pkg create my_first_ros_rclpy_pkg --build-type ament_python --dependencies rclpy std_msgs

## 빌드
- colcon = collective construction . cli tool to improve the workflow of building, testing, 
using multiple software packages.
- https://github.com/colcon/colcon-core

[0.173s] WARNING:colcon.colcon_core.verb:No task extension to 'build' a 'ros.ament_python' package

package.xml에 있는 
    <export>
        <build_type>ament_python</build_type>
    </export>
타이포 ㅎㅎ(amend가 아닌 ament)

- 특정 패키지의 첫 빌드 후에는 환경설정 파일을 불러와서 실행가능한 패키지의 노드 설정을 해줘야
- 빌드된 노드를 실행할 수 있다.
-> . ~/robot_ws/install/local_setup.bash

## 실행
- ros2 run my_first_ros_rclpy_pkg helloworld_subscriber
- ros2 run my_first_ros_rclpy_pkg helloworld_publisher



# 중요한 포인트?
- 파이썬 ROS2 패키지는 파이썬 코드 외에도 해당 패키지가 참조하는 다양한 파일들을 '설치 폴더'에 추가해야 하기 때문에
최소한 한 번의 빌드는 해야한다.
-> 심볼릭 링크 파일이나 원본이 복사된 파일이 '설치 폴더'에 신규 생성된다.

- 파이썬 코드의 파일 이름에 주의하여 작성하자.
- 코드가 바뀐 후에는 환경설정 파일 노드 설정 해줘야함. (. ~/robot_ws/install/local_setup.bash) ? -> 확인 필요

## 빌드 후
~/robot_ws/install/msg_srv_action_interface_example 폴더 안에
작성한 ROS 인터페이스를 사용하기 위한 파일들이 저장되어 있다.

- C언어를 위한 .h(헤더 파일), C++를 위한 (.hpp) > include/msg_srv_action_interface_example
- 파이썬 모듈 (.py)  > lib/python3.6/site-packages/msg_srv_action_interface_example
- IDL 파일들 (.idl) > share/msg_srv_action_interface_example

* python3.10 기준 파이썬 모듈이 빌드되는 경로
python 3.10 기준으로는 lib/python3.6/site-packages가 아닌
local/lib/python3.10/dist-packages임.

# setup.py
## data_files
이 패키지에 사용되는 파일들을 기입하여 함께 배포한다.
- package.xml
- *.launch.py (런치 파일)
- *.yaml (파라미터 파일)
## entry_points
사용할 스크립트의 이름, 호출 함수를 등록한다.
'{노드 이름} = {함수}'
ros2 run과 같은 노드 실행 명령어로 노드를 실행한다.