# README
## 소스 코드 다운
이 프로젝트 폴더(topic_service_action_rclpy_example)의
package.xml, setup.py는 
파이썬 패키지를 빌드하기 위한 
각각 패키지 설정 파일, 파이썬 패키지 설정 파일이다.

위 패키지 설정 파일을 포함한 코드 레포지토리는 
https://github.com/robotpilot/ros2-seminar-examples.git을 사용하고
이를 빌드한다.

## 빌드
~without alias  
cd ~/robot_ws/src  
git clone ...  
cd ~/robot_ws && colcon build --symlink-install

~alias version  
cw
cbp topic_service_action_rclpy_example

* 참고
1. git clone된 프로젝트에서 msg_srv_action_interface_example의 빌드 파일이 겹치지 않게 조정해야함
2. 조정 후 interface example과 topic_service_action_rclpy_example을 따로 빌드 해줌
3. home에서 source .bashrc 후
4. 노드를 실행할 것


## 빌드 후 생성되는 것들
### 인터페이스를 사용하기 위한 실행 스크립트
~/robot_ws/install/{topic...}/share/{topic...}

### launch 파일(.py)과 파라미터 파일(.yaml)
~/robot_ws/install/{topic...}/share/{topic...}

## 실행 
### calculator 노드 실행
ros2 run topic_service_action_rclpy_example calculator

### topic publisher 실행
ros2 run topic_service_action_rclpy_example argument

### 서비스 클라이언트 실행
ros2 run topic_service_action_rclpy_example operator

### action client 실행
ros2 run topic_service_action_rclpy_example checker

### launch 파일 실행
argument 노드와 calculator 노드를 한 꺼번에 실행하려면
arithmetic.launch.py을 실행한다.
ros2 launch topic_service_action_rclpy_example arithmetic.launch.py
