# ROS2-python
ROS2-python practice

gpu-risc, cpu-cisc
cuda opencl
kernel 코드 작성.
CUDA 프로그래밍 모델을 사용한다고 가정할 때,
호스트(cpu) 코드, 
디바이스(gpu) 코드
 호스트-디바이스 데이터 전송 코드를 작성해야함.
장점
일반적으로 gpu가 cpu보다 throughput이 더 큽니다.
각 원본 픽셀 데이터끼리는 처리된 픽셀 데이터에 영향을 끼치지 않으므로 병렬처리 될 수 있습니다.
gpu스레드와 cpu 스레드의 차이. 
gpu스레드가 cpu스레드보다 믾음.일반적으로 수천개. 스레드 그룹이 있고 같은 명령어를 실행할 수 있음. 
cpu 스레드의 경우 물리 cpu core
out-of-order 실행 대 thread rotation. 
순차 실행에 강점. clock speed<->throughput
gpu 코드, 커널코드에 분기문이 있으면 하드웨어에서 스레드들이 직렬로 수행되는 결과가 나타난다.
1개의 블록=스레드블록=1 커널 블록 =1SM(GPU 스트릐밍 다중프로세서)
스레드 블록수 < SM 수.

https://junstar92.tistory.com/246