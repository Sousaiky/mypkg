# mypkg

![test](https://github.com/Sousaiky/mypkg/actions/workflows/test.yml/badge.svg)
*  * mypkgは千葉工業大学の2023年度ロボットシステム学の授業内課題です。また、このリポジトリはROS 2のパッケージです。  

## mypkgについて

*  このリポジトリにはtalker,listener,launch,testが含まれます。  

## コマンドの使用例

# talker.py  
* このノードは誕生日を受け取ると、その人の星座を返し、それ以外の入力を受け取るとその人の運勢を返すサービスです。  

* 通信には[person_msgs](https://github.com/Sousaiky/person_msgs)のQuery.srv,Person.msgに内蔵されているbirthdayとageを用いています。  

サービス名は/queryです。  

* 動作例  
  
端末１  
``` 
$ ros2 run mypkg talker  
```  

端末２  

例１  
```
$ ros2 service call /query person_msgs/srv/Query "birthday: 813"
waiting for service to become available...
requester: making request: person_msgs.srv.Query_Request(birthday=813)

response:
person_msgs.srv.Query_Response(age='獅子座')
```  
例２  
```
$ ros2 service call /query person_msgs/srv/Query "birthday: 1221"
waiting for service to become available...
requester: making request: person_msgs.srv.Query_Request(birthday=1221)

response:
person_msgs.srv.Query_Response(age='射手座')
```

存在しない日を入力した場合  
```
$ ros2 service call /query person_msgs/srv/Query "birthday: 842"
requester: making request: person_msgs.srv.Query_Request(birthday=842)

response:
person_msgs.srv.Query_Response(age='今日の運勢が吉')
```

# listener.py  
* このノードはtalker.pyを用いて存在する誕生日星座を列挙します  

* 動作例 

端末１  
```
$ ros2 run mypkg talker
```

端末２  
```
$ ros2 run mypkg listener
[INFO] [1703910395.569374612] [listener]: 君は魚座
[INFO] [1703910395.570552153] [listener]: 君は牡羊座
[INFO] [1703910395.571453409] [listener]: 君は双子座
[INFO] [1703910395.572497196] [listener]: 君は蟹座
[INFO] [1703910395.574015496] [listener]: 君は獅子座
[INFO] [1703910395.578337025] [listener]: 君は乙女座
[INFO] [1703910395.579290152] [listener]: 君は乙女座
[INFO] [1703910395.580379964] [listener]: 君は天秤座
[INFO] [1703910395.581240750] [listener]: 君は蠍座
[INFO] [1703910395.582171559] [listener]: 君は射手座
[INFO] [1703910395.583104315] [listener]: 君は山羊座
[INFO] [1703910395.584010215] [listener]: 君は水瓶座
```

# talk_listen.launch.py
* このノードはtalkerとlistenerを同時に起動するlaunchファイルです  

```
$ ros2 launch mypkg talk_listen.launch.py
[INFO] [launch]: All log files can be found below /home/saiki/.ros/log/2023-12-30-13-29-38-414088-saikisoshi-32553
[INFO] [launch]: Default logging verbosity is set to INFO
[INFO] [talker-1]: process started with pid [32555]
[INFO] [listener-2]: process started with pid [32557]
[listener-2] [INFO] [1703910579.065907936] [listener]: 君は魚座
[listener-2] [INFO] [1703910579.067253731] [listener]: 君は牡羊座
[listener-2] [INFO] [1703910579.068399587] [listener]: 君は双子座
[listener-2] [INFO] [1703910579.069560784] [listener]: 君は蟹座
[listener-2] [INFO] [1703910579.070807817] [listener]: 君は獅子座
[listener-2] [INFO] [1703910579.072037176] [listener]: 君は乙女座
[listener-2] [INFO] [1703910579.073102118] [listener]: 君は乙女座
[listener-2] [INFO] [1703910579.074398607] [listener]: 君は天秤座
[listener-2] [INFO] [1703910579.075455681] [listener]: 君は蠍座
[listener-2] [INFO] [1703910579.076380459] [listener]: 君は射手座
[listener-2] [INFO] [1703910579.077293677] [listener]: 君は山羊座
[listener-2] [INFO] [1703910579.078526403] [listener]: 君は水瓶座
[INFO] [listener-2]: process has finished cleanly [pid 32557]
```

# 導入方法

```
~/ros2_ws/src/$ git clone https://github.com/Sousaiky/mypkg.git  

~/ros2_ws/src/$ ./test.bash
Starting >>> mypkg
Starting >>> person_msgs
[2.988s] WARNING:colcon.colcon_ros.task.ament_python.build:Package 'mypkg' doesn't explicitly install the 'package.xml' file (colcon-ros currently does it implicitly but that fallback will be removed in the future)
Finished <<< person_msgs [1.47s]
Finished <<< mypkg [1.76s]

Summary: 2 packages finished [3.50s]
uint16 birthday
---
string age
Starting >>> mypkg
Starting >>> person_msgs
[2.914s] WARNING:colcon.colcon_ros.task.ament_python.build:Package 'mypkg' doesn't explicitly install the 'package.xml' file (colcon-ros currently does it implicitly but that fallback will be removed in the future)
Finished <<< person_msgs [1.50s]
Finished <<< mypkg [1.80s]

Summary: 2 packages finished [3.52s]
[listener-2] [INFO] [1703911322.350850458] [listener]: 君は牡羊座
[listener-2] [INFO] [1703911322.351996440] [listener]: 君は双子座
[listener-2] [INFO] [1703911322.353932095] [listener]: 君は獅子座
[listener-2] [INFO] [1703911322.354829833] [listener]: 君は乙女座
[listener-2] [INFO] [1703911322.355721797] [listener]: 君は乙女座
[listener-2] [INFO] [1703911322.356619683] [listener]: 君は天秤座
[listener-2] [INFO] [1703911322.357548788] [listener]: 君は蠍座
[listener-2] [INFO] [1703911322.358566673] [listener]: 君は射手座
[listener-2] [INFO] [1703911322.359521410] [listener]: 君は山羊座
[listener-2] [INFO] [1703911322.360630684] [listener]: 君は水瓶座
[listener-2] [INFO] [1703911322.349358488] [listener]: 君は魚座

~/ros2_ws/src/$ cd ~/ros_ws

~/ros2_ws$ colcon build
```

このレポジトリのクローンはros2_ws/src内で行ってください  

使用の前には必ずビルド作業を行ってください  

上記の talk_listen.launch.py起動し、動作を確認してください 

# テスト環境 

* Ubuntu20.04.6 LTS  
* ROS 2 foxy  
* Python 
  * テスト済み: 3.8.10  
* 千葉工業大学の上田隆一先生のソースコードを授業のため流用しています。  
* Github Actionsのテストには千葉工業大学の上田隆一先生のコンテナを使用しています。  
  * URL:https://hub.docker.com/repository/docker/ryuichiueda/ubuntu22.04-ros2

# 著作権/ライセンス
* このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます。  
* このパッケージのコードは、下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）の物を、本人の許可を得て自身の著作とし,いくつかの機能を追加したものです。  
  * [ryuichiueda/my_slides/robosys_2022](https://github.com/ryuichiueda/my_slides/blob/master/robosys_2022)  
  * [LICENCE](https://github.com/Sousaiky/mypkg/blob/master/LICENSE)  


©2023 Soshi Saiki
