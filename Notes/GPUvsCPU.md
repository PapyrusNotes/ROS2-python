matrix operation, image processing, deep learning에서 사용하는 벡터 연산과 같이
병렬성이 높은 애플리케이션은 멀티코어 CPU 병렬 연산보다 GPU 병렬 연산이 유리하다.

<CPython 단독 사용, CPU 병렬 연산>
multiprocessing 모듈을 사용하여 코어마다 1개의 파이썬 인터프리터가 돌면서 연산을 수행.

<GPU 병렬 연산>
CPU보다 월등히 많은 수의 병렬 스레드를 사용하여 같은 명령어를 실행할 수 있음.
원본 픽셀 데이터는 처리 후의 픽셀 데이터에 영향을 끼치지 않으므로 병렬처리 될 수 있음
cpu칩 보다 큰 대역폭으로 동작하며, 많은 양의 데이터가 이동할 수 있음.
