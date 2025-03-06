컴퓨터 비전 분야의 기본 좌표계 (카메라) z forward, x right, y down

로봇의 기본 좌표게 x forward, y left z up

센서 제조사별 다른 좌표계

단위 뿐 아니라 좌표 표현 통일해야한다.
REP-103

정리하면
3차원 벡터 표기 = 오른손 법칙
로봇의 기본 좌표계 = Red x축, green y축, blue z축
지리적 위치 표현 = 단거리 데카르트 표현 ENU(East North Up)규칙. 
실내 로봇에선 잘 다루지 않는 좌표고, 비교적 큰 맵을 다루는 드론, 실외 자율주행 로봇에서 사용하는 좌표
접미사 프레임
X FORWARD YLEFT ZUP ,ENU좌표에서 벗어나는 경우 접미사 프레임을 사용하여 기본 좌표계와 구별하여 사용.
_OPTICAL
비전 경우 카메라 좌표계로 많이 사용되는 Z FORWARDL X RIGHT, YDOWN 사용
카메라 센서의 메시지에서 _OPTICAL 접미사를 붙여 사용한다.
Z FORWARD XRIGHT, YDOWN의 카메라 좌표계와 로봇좌표계 (XFORWARD YLEFT ZUP) 간의 TF(Transform)가 필요함
_NED
실외 동작 시스템의 경우, NED(NORTH EAST DOWN)

좌표표현의 회전
ros커뮤니티 권장

1. 쿼터니언.간결한 표현 방식(x,y,z,w)특이점 없음
2. 회저매트릭스.특이점없음
3. 고정축.각속도에 사용

권장x
4.오일러 각도.전역 좌표계에서 회전 발생. 한 축이 다른 축의 회전과 겹치는 문제=짐벌락.때문에 사용권장 x



