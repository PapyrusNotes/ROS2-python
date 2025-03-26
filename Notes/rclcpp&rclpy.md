# IPC 지원 여부
IPC는 복수 개의 노드를  
단일 프로세스에서 동작되게 할 수 있다.  

DDS Writer-DDS Reader의 고정된 메모리 공간에 접근하여 
메모리 복사가 이루어지지 않는 ZERO-COPY 방식을 사용한다.  

*rclcpp만 지원한다.* 



# ROS2 Component

## ROS1의 동적 로딩 
ROS1에서는 class_loader와 pluginlib 패키지가  
동적 로딩을 지원한다.     

- class_loader는 ROS와 독립적인 패키지로  
C++클래스를 동적 로딩한다.  


- pluginlib는 ROS 패키지로 작성된 플러그인을
런타임에서 로딩한다.  
  EX) Nodelets Component 

## ROS2에서의 동적 로딩
ROS2에서는 같은 기능을 하는 class_loader 기반의 Components 제공  

*rclcpp만 지원*

