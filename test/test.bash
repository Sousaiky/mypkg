#!/bin/bash -xv
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

timeout 10 ros2 launch mypkg talk_listen.launch.py > /tmp/mypkg.log

ng () {
    echo "NG at Line $1"
    res=1
}

res=0

if grep -q '座' /tmp/mypkg.log; then
    res=0
else
    res=1

[ "$?" = 0 ] || ng ${LINENO}

[ "$res" = 0 ] && echo "OK"
exit $res
fi
