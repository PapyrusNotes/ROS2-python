# Clock & Time
## 시간 동기화
ROS2 시스템에 참여하는 센서와 같은 노드 객체들은 
서로 통신하며 다양한 정보를 주고받는다.

다수 센서간의 시간 동기화가 필요하다.

동기화를 위해서는
해당 정보가 생성된 정확한 시간이 필수적.

## TOPIC's Time 
ROS2의 Published되는 Topic은 {data}+{published time}을 함께 포함한다.
std_msgs/msg/header = ROS2의 표준 메시지 타입 중 하나
sensor_msgs, geometry_msgs, nav_msgs등의 메시지 타입에 포함됨.
published =time은 2개의 정수형으로 표현됨. 초-나노초

## ROS2의 기본시계
RIOS2의 기본 시계는 SYSTEM CLOCK = UTC(협정 세계시)
RCLCPP C++ -> STD::CHRONO
RCLPY PYTHON -> TIME모듈을 캡슐화하여 사용

## TIME ABSTRACTIONS
ros2bag를 통해 로깅된 데이터를 디버그하거나
gazebo, ignition과 같은 로봇 시뮬레이션에서의 사용 목적으로
세 가지의 추상화된 시간을 제공한다.

- system time : system clock을 사용한 시간
- ros time : 
- steady time :

## time api
- TIME CLASS : 시간을 다룰 수 있는 오퍼레이터 제공. SECONDS(DOUBLE), NANOSECONDS(UNSIGNED INT 64비트) 중 하나로 반환.
- NODE->NOW() 멤버 함수는 노드의 시간을 확인하는 함수이다.
- DURATION :  순간의 시간이 아닌 기간을 다룰 수 있는 오퍼레이터 제공. TIME CLASS와 마찬가지로 결과를 SECONDS혹은 NANO SECONDS로 반환
- DURATION은 이전 시간을 표시할 수 있고 음수로 표기한다. TIME과 연산 가능
- RATE : 반복문에서 특정 주기를 유지시켜준다. W
- RATE는 SYSTEM CLOK, WALLRATE는 STEADY CLOKC을 사용하여 시간을 확인한다.
- ROS2에서는  CALLBACK함수를 사용하는 TIMER API를 권장함