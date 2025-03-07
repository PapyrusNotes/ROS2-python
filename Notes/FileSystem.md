# FILE SYSTEM IN ROS2
- ROS2 패키지 검색
- ROS2 소스코드 검색
- 메시지 파일, 
- 실행 파일
- 파라미터 설정 파일
- 환경설정 파일 등
을 이용하기 위한 일관된 경험 제공.
- 
## 패키지
소프트웨어 구성을 위한 기본 단위
ROS의 응용프로그램은 패키지 단위로 개발되고 관리된다.
패키지는 노드를 하나 이상 포함하거나
다른 노드를 실행하기 위한
런치같은 실행 및 설정파일들을 포함함

20215월 기준 기봊ㄴ 패키지 개수 =450여개
설치가능한 패키지는 1200여개 < ROS1 KINETIC 3,700여개

공통된 목적을 지닌 패키지들의 집합 = 메타 패키지
EX ) NAVIGATION2 메타키지 = NAV2 AMCL, NAV2 BT NAVIGATORL, NAV2 COSTMAP 2D 등 구성

### 패키지 구성 항목
- 각 PCKAGE HAS PACKAGE.XML
XML->패키지 정보를 담은 XML파일
패키지 이름, 저작자, 라이선스, 의존성 패키지 등을 기술

- 각 PACKAGE HAS CMAKELISTS.TXT파일 
왜냐하면 ROS2의 빌드 시스템 = AMENTM, CMAKE 사용.

- MSG, SRV, ACTION 인터페이스 파일


