geometry_msgs/msgs/Twist message  
(float64) 
- linear.x, linear.y, linear.z (m/s)
- angular.x, angular.y, angular.z (rad/s)

ROS2 Standard Unit = SI derived unit

SI단위=7개
SI유도단위=20개

Voltage = ㅅV
Angle = RAD
Length =, Meter
Mass질량 = kilogram
Time - second
Current = ampere
Frequency = hjertz
Force = newton
Power = watt
Temperature = Celsius
Magnetism = tesla

-> 병진 속도 = m/s
-> 회전 속도 = rad/s
                                         
Python에 PEP가 있다면 ROS2엔 REP가 있다.
노드 간의 주고받는 데이터의 이름과 자료형을 ROS2인터페이스에서 규정한다.
단위는 REP103에 정해놓음.
다양환 패키지를 사용했을 때 나타날 수 있는 버그를 줄임.
