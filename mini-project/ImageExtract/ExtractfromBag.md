windows11
window terminal - ubuntu 22.04.03 LTS x86_64
ros2 
접근방법
bag파일은 ros에 쓰이는 file format이며,
ros message data를 기록, replaying하기 위해 사용.


ros command로 분석, 추출한 뒤
ffmpeg로 mpeg영상 저장.
ros topic이 control commands, camera streams, sensor data와 같은 data를 publish한다.
astra사의 ros2 repository와 같이 depth 추정 기능이 있는 3d camera 제어를 위한 package가 있다.
gscam 패키지는 ros에서 webcam을 사용하기 위해 gstreamer를 사용하며 , 멀티미디어 파이프라인 기능이 있는 gstreamer의 기능을 사용할 수 있다.
하지만 gstreamer가 ros의 코어 dependency는 아님.
ros는 멀티미디어 데이터 처리를 위해 
용도에 맞는 다양한 ros-native package를 사용한다. 
rosbag -> 녹화, 플레이백 -> 데이터 분석, 시뮬레이션
image_pipeline -> 카메라 캘리브레이션, depth processing,-> depth 매핑, stereo vision
stereo_image_proc -> stereo image 처리 -> 3d vision, slam(simultaneous localization and mapping)에 사용
<window wsl 세팅>
<ros 설치 준비>
sudo apt update
sudo apt install software-properties-common
sudo add-apt-repository universe
sudo apt update && sudo apt install curl -y
sudo curl -sSL {github repository ros master  key, gpg key } apt key 등록
ecoo “key ring추가
apt update install ros-dev-tools

<ros 설치>
25.01.기준 ros-humble-desktop 설치
<text editor 설치>
<vscode 설치>
로케일 us로 수정
bashrc 파일 수정
source 
ros2 동작 확인 with talker-listener
<ros-humble-rosbag2 설치 >
<curl -o demo.bag https://…>
<bag파일은 ros1용이므로 python library rosbags를 이용하여 ros2 bag에 맞게 변환.=> 이 python lib를 사용하면 Ros1을 설치할 필요없음.>
rosbags-convert —src demo.bag –dst demo
demo.db3로 변환됨(sqlite3 데이터베이스 파일)
ros2 bag info demo

Files:             demo.db3
Bag size:          119.5 MiB
Storage id:        sqlite3
Duration:          7.780758504s
Start:             Mar 22 2017 11:26:20.103843113 (1490149580.103843113)
End:               Mar 22 2017 11:26:27.884601617 (1490149587.884601617)
Messages:          1606
Topic information: 
Topic: /diagnostics | Type: diagnostic_msgs/msg/DiagnosticArray | Count: 52 | Serialization Format: cdr
Topic: /image_color/compressed | Type: sensor_msgs/msg/CompressedImage | Count: 234 | Serialization Format: cdr
Topic: /tf | Type: tf2_msgs/msg/TFMessage | Count: 774 | Serialization Format: cdr
Topic: /radar/points | Type: sensor_msgs/msg/PointCloud2 | Count: 156 | Serialization Format: cdr
 Topic: /radar/range | Type: sensor_msgs/msg/Range | Count: 156 | Serialization Format: cdr
Topic: /radar/tracks | Type: radar_driver/msg/RadarTracks | Count: 156 | Serialization Format: cdr
 Topic: /velodyne_points | Type: sensor_msgs/msg/PointCloud2 | Count: 78 | Serialization Format: cdr


약 8초 길이 파일
message 1606개
sudo apt install ros-humble-image-transport ros-humble-cv-bridge python3-opencv

echo 로 image_color/comprressed topic으로부터 메시지가 publish되는지 확인해본 결과
확인됨.
frame_id : camera
format: bgr8, jpeg compressed bgr8
subscription, callback 이 호출되지 않음.
image module 이 아닌 compressedimage module을 사용해야함.

ros2 bag play demo —topics /image_color/compressed

ffmpeg 설치 후
root@laborahanws:~/extracted# ffmpeg -framerate 30 -i frame_%04d.jpg -c:v libx264 output.mp4
ffmpeg version 4.4.2-0ubuntu0.22.04.1 Copyright (c) 2000-2021 the FFmpeg developers
  built with gcc 11 (Ubuntu 11.2.0-19ubuntu1)
  configuration: --prefix=/usr --extra-version=0ubuntu0.22.04.1 --toolchain=hardened --libdir=/usr/lib/x86_64-linux-gnu --incdir=/usr/include/x86_64-linux-gnu --arch=amd64 --enable-gpl --disable-stripping --enable-gnutls --enable-ladspa --enable-libaom --enable-libass --enable-libbluray --enable-libbs2b --enable-libcaca --enable-libcdio --enable-libcodec2 --enable-libdav1d --enable-libflite --enable-libfontconfig --enable-libfreetype --enable-libfribidi --enable-libgme --enable-libgsm --enable-libjack --enable-libmp3lame --enable-libmysofa --enable-libopenjpeg --enable-libopenmpt --enable-libopus --enable-libpulse --enable-librabbitmq --enable-librubberband --enable-libshine --enable-libsnappy --enable-libsoxr --enable-libspeex --enable-libsrt --enable-libssh --enable-libtheora --enable-libtwolame --enable-libvidstab --enable-libvorbis --enable-libvpx --enable-libwebp --enable-libx265 --enable-libxml2 --enable-libxvid --enable-libzimg --enable-libzmq --enable-libzvbi --enable-lv2 --enable-omx --enable-openal --enable-opencl --enable-opengl --enable-sdl2 --enable-pocketsphinx --enable-librsvg --enable-libmfx --enable-libdc1394 --enable-libdrm --enable-libiec61883 --enable-chromaprint --enable-frei0r --enable-libx264 --enable-shared
  libavutil      56. 70.100 / 56. 70.100
  libavcodec     58.134.100 / 58.134.100
  libavformat    58. 76.100 / 58. 76.100
  libavdevice    58. 13.100 / 58. 13.100
  libavfilter     7.110.100 /  7.110.100
  libswscale      5.  9.100 /  5.  9.100
  libswresample   3.  9.100 /  3.  9.100
  libpostproc    55.  9.100 / 55.  9.100
Input #0, image2, from 'frame_%04d.jpg':
  Duration: 00:00:07.37, start: 0.000000, bitrate: N/A
  Stream #0:0: Video: mjpeg (Baseline), yuvj420p(pc, bt470bg/unknown/unknown), 1400x512 [SAR 1:1 DAR 175:64], 30 fps, 30 tbr, 30 tbn, 30 tbc
Stream mapping:
  Stream #0:0 -> #0:0 (mjpeg (native) -> h264 (libx264))
Press [q] to stop, [?] for help
[libx264 @ 0x562c76149740] using SAR=1/1
[libx264 @ 0x562c76149740] using cpu capabilities: MMX2 SSE2Fast SSSE3 SSE4.2 AVX FMA3 BMI2 AVX2
[libx264 @ 0x562c76149740] profile High, level 3.1, 4:2:0, 8-bit
[libx264 @ 0x562c76149740] 264 - core 163 r3060 5db6aa6 - H.264/MPEG-4 AVC codec - Copyleft 2003-2021 - http://www.videolan.org/x264.html - options: cabac=1 ref=3 deblock=1:0:0 analyse=0x3:0x113 me=hex subme=7 psy=1 psy_rd=1.00:0.00 mixed_ref=1 me_range=16 chroma_me=1 trellis=1 8x8dct=1 cqm=0 deadzone=21,11 fast_pskip=1 chroma_qp_offset=-2 threads=16 lookahead_threads=2 sliced_threads=0 nr=0 decimate=1 interlaced=0 bluray_compat=0 constrained_intra=0 bframes=3 b_pyramid=2 b_adapt=1 b_bias=0 direct=1 weightb=1 open_gop=0 weightp=2 keyint=250 keyint_min=25 scenecut=40 intra_refresh=0 rc_lookahead=40 rc=crf mbtree=1 crf=23.0 qcomp=0.60 qpmin=0 qpmax=69 qpstep=4 ip_ratio=1.40 aq=1:1.00
Output #0, mp4, to 'output.mp4':
  Metadata:
    encoder         : Lavf58.76.100
  Stream #0:0: Video: h264 (avc1 / 0x31637661), yuvj420p(pc, bt470bg/unknown/unknown, progressive), 1400x512 [SAR 1:1 DAR 175:64], q=2-31, 30 fps, 15360 tbn
    Metadata:
      encoder         : Lavc58.134.100 libx264
    Side data:
      cpb: bitrate max/min/avg: 0/0/0 buffer size: 0 vbv_delay: N/A
frame=  221 fps=0.0 q=-1.0 Lsize=    3373kB time=00:00:07.26 bitrate=3802.2kbits/s speed=8.45x
video:3369kB audio:0kB subtitle:0kB other streams:0kB global headers:0kB muxing overhead: 0.103764%
[libx264 @ 0x562c76149740] frame I:1     Avg QP:25.95  size: 59217
[libx264 @ 0x562c76149740] frame P:55    Avg QP:26.04  size: 30918
[libx264 @ 0x562c76149740] frame B:165   Avg QP:27.71  size: 10241
[libx264 @ 0x562c76149740] consecutive B-frames:  0.5%  0.0%  0.0% 99.5%
[libx264 @ 0x562c76149740] mb I  I16..4:  2.2% 94.9%  2.9%
[libx264 @ 0x562c76149740] mb P  I16..4:  0.2% 16.1%  0.2%  P16..4: 44.0% 22.2% 13.4%  0.0%  0.0%    skip: 3.8%
[libx264 @ 0x562c76149740] mb B  I16..4:  0.0%  3.4%  0.0%  B16..8: 43.4%  5.9%  1.0%  direct: 5.8%  skip:40.5%  L0:49.2% L1:44.9% BI: 5.9%
[libx264 @ 0x562c76149740] 8x8 transform intra:97.9% inter:79.7%
[libx264 @ 0x562c76149740] coded y,uvDC,uvAC intra: 92.4% 84.6% 32.5% inter: 34.5% 36.3% 1.6%
[libx264 @ 0x562c76149740] i16 v,h,dc,p:  6% 67%  9% 18%
[libx264 @ 0x562c76149740] i8 v,h,dc,ddl,ddr,vr,hd,vl,hu: 10% 17% 40%  5%  5%  5%  5%  6%  7%
[libx264 @ 0x562c76149740] i4 v,h,dc,ddl,ddr,vr,hd,vl,hu: 13% 43% 13%  5%  6%  5%  7%  4%  5%
[libx264 @ 0x562c76149740] i8c dc,h,v,p: 68% 16% 14%  2%
[libx264 @ 0x562c76149740] Weighted P-Frames: Y:0.0% UV:0.0%
[libx264 @ 0x562c76149740] ref P L0: 28.0% 11.6% 47.7% 12.7%
[libx264 @ 0x562c76149740] ref B L0: 67.6% 26.1%  6.3%
[libx264 @ 0x562c76149740] ref B L1: 90.3%  9.7%
[libx264 @ 0x562c76149740] kb/s:3746.02

