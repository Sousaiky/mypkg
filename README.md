# mypkg

![test](https://github.com/Sousaiky/mypkg/actions/workflows/test.yml/badge.svg)
*  ROS 2のパッケージであるmypkgは千葉工業大学の2023年度ロボットシステム学の授業内課題です。中には誕生日を受け取ると、その人の星座を返し、それ以外の入力を受け取るとその人の運勢を返すtalkerとlistenerが入っています。  

# talker.pyとlistener.pyについて  

## トピックについて  

* person型のQueryで、talkerからはperson_msgs.srvが送信されています。  

## コマンドの使用例  

# talker.py  

* 通信には[person_msgs](https://github.com/Sousaiky/person_msgs)のQuery.srv,Person.msgで設定したbirthdayとageを用いています。  

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
[INFO] [1704372681.168881832] [listener]: 君は魚座
[INFO] [1704372681.171309597] [listener]: 君は牡羊座
[INFO] [1704372681.173179145] [listener]: 君は牡牛座
[INFO] [1704372681.175152663] [listener]: 君は双子座
[INFO] [1704372681.177236213] [listener]: 君は蟹座
[INFO] [1704372681.179137471] [listener]: 君は獅子座
[INFO] [1704372681.181059027] [listener]: 君は乙女座
[INFO] [1704372681.182966136] [listener]: 君は天秤座
[INFO] [1704372681.184794864] [listener]: 君は蠍座
[INFO] [1704372681.186460437] [listener]: 君は射手座
[INFO] [1704372681.188262249] [listener]: 君は山羊座
[INFO] [1704372681.189589874] [listener]: 君は水瓶座
[INFO] [1704372681.191171231] [listener]: 君は今日の運勢が大吉
```

# talk_listen.launch.py
* このノードはtalkerとlistenerを同時に起動するlaunchファイルです  

```
$ ros2 launch mypkg talk_listen.launch.py
[INFO] [launch]: All log files can be found below /home/saiki/.ros/log/2024-01-04-21-55-45-208432-saikisoshi-20430
[INFO] [launch]: Default logging verbosity is set to INFO
[INFO] [talker-1]: process started with pid [20432]
[INFO] [listener-2]: process started with pid [20434]
[listener-2] [INFO] [1704372945.713835499] [listener]: 君は魚座
[listener-2] [INFO] [1704372945.715375393] [listener]: 君は牡羊座
[listener-2] [INFO] [1704372945.716507644] [listener]: 君は牡牛座
[listener-2] [INFO] [1704372945.717559610] [listener]: 君は双子座
[listener-2] [INFO] [1704372945.718467485] [listener]: 君は蟹座
[listener-2] [INFO] [1704372945.719593244] [listener]: 君は獅子座
[listener-2] [INFO] [1704372945.720846840] [listener]: 君は乙女座
[listener-2] [INFO] [1704372945.721927427] [listener]: 君は天秤座
[listener-2] [INFO] [1704372945.722934953] [listener]: 君は蠍座
[listener-2] [INFO] [1704372945.723927998] [listener]: 君は射手座
[listener-2] [INFO] [1704372945.725065112] [listener]: 君は山羊座
[listener-2] [INFO] [1704372945.725999350] [listener]: 君は水瓶座
[listener-2] [INFO] [1704372945.726937855] [listener]: 君は今日の運勢が吉
[INFO] [listener-2]: process has finished cleanly [pid 20434]
```

# 導入方法

```
~/ros2_ws/src/$ git clone https://github.com/Sousaiky/mypkg.git  

~/ros2_ws/src/$ ./test.bash

~~~

Starting >>> mypkg
Starting >>> person_msgs
[2.080s] WARNING:colcon.colcon_ros.task.ament_python.build:Package 'mypkg' doesn't explicitly install the 'package.xml' file (colcon-ros currently does it implicitly but that fallback will be removed in the future)
Finished <<< person_msgs [0.94s]
Finished <<< mypkg [1.14s]

Summary: 2 packages finished [2.32s]

~~~

#SPDX-FileCopyrightText: 2023 Soshi Saiki
#SPDX-Licence-Identifire: BSD-3-Clause

uint16 birthday
---
string age

~~~

Starting >>> mypkg
Starting >>> person_msgs
[2.085s] WARNING:colcon.colcon_ros.task.ament_python.build:Package 'mypkg' doesn't explicitly install the 'package.xml' file (colcon-ros currently does it implicitly but that fallback will be removed in the future)
Finished <<< person_msgs [0.95s]
Finished <<< mypkg [1.14s]

Summary: 2 packages finished [2.34s]

~~~

~/ros2_ws/src/$ cd ros_ws

~/ros2_ws$ colcon build
```

このレポジトリのクローンはros2_ws/src内で行ってください  

使用の前には必ずビルド作業を行ってください  

上記の talk_listen.launch.py起動し、動作を確認してください  

# 必要なソフトウェア  

* Ubuntu20.04.6 LTS
* ROS 2 Foxy Fitzroy テストの結果は問題なく動作しています。
* Python  
  * テスト済み: 3.7~3.10

# テスト環境 

* Github Actionsのテストには千葉工業大学の上田隆一先生のコンテナを使用しています。  
  * URL:https://hub.docker.com/repository/docker/ryuichiueda/ubuntu22.04-ros2  

# 著作権/ライセンス
* このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます。  
* このパッケージのコードは、下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）の物を、本人の許可を得て自身の著作とし,いくつかの機能を追加したものです。  
  * [ryuichiueda/my_slides/robosys_2022](https://github.com/ryuichiueda/my_slides/blob/master/robosys_2022)  
  * [LICENCE](https://github.com/Sousaiky/mypkg/blob/master/LICENSE)  


©2023 Soshi Saiki
