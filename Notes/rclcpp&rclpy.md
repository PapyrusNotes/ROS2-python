# IPC 지원 여부
IPC는 복수 개의 노드를 단일 프로세스에서 동작되게 할 수 있다.
DDS Writer-DDS Reader의 
고정된 메모리 공간에 접근하여 메모리 복사가 이루어지지 않는 ZERO-COPY 방식을 사용한다.
rclcpp만 지원한다. 