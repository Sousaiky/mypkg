#!/bin/bash

dir=~
[ "$1" != "" ] && dir="$1"   #引数があったら、そちらをホームに変える。

cd $dir/ros2_ws

colcon build

source $dir/.bashrc

ros2 interface show "person_msgs/srv/Query"

cd $dir/ros2_ws

colcon build

source $dir/.bashrc

timeout 10 ros2 launch mypkg talk_listen.launch.py > /tmp/mypkg.log

cat /tmp/mypkg.log |
	grep '44'


