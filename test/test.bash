#!/bin/bash
#SPDX-FileCopyrightText: 2023 Soshi Saiki
#SPDX-Licence-Identifire: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"   #引数があったら、そちらをホームに変える。

#cd $dir/ros2_ws
#colcon build
#source $dir/.bashrc
#timeout 20 ros2 launch mypkg talk_listen.launch.py > /tmp/mypkg.log
source $dir/.bashrc

cd $dir/ros2_ws/src

git clone https://github.com/Sousaiky/person_msgs.git

cd $dir/ros2_ws

colcon build

source $dir/.bashrc

ros2 interface show "person_msgs/srv/Query"

cd $dir/ros2_ws

colcon build

source $dir/.bashrc

timeout 30 ros2 launch mypkg talk_listen.launch.py > /tmp/mypkg.log

if 321 <= request.birthday <= 331 and grep -q '牡羊座' /tmp/mypkg.log; then 
	echo 0
else 
	echo 1
fi
