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
- 파이썬 코드의 파일 이름에 주의하여 작성하자.
- 코드가 바뀐 후에는 환경설정 파일 노드 설정 해줘야함. (. ~/robot_ws/install/local_setup.bash) ? -> 확인 필요
