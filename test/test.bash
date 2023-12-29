#!/bin/bash

dir=~
[ "$1" != "" ] && dir="$1"   #引数があったら、そちらをホームに変える。

cd $dir/ros2_ws
colcon build
source $dir/.bashrc
timeout 20 ros2 launch mypkg talk_listen.launch.py > /tmp/mypkg.log

cat /tmp/mypkg.log |
	grep '牡羊座'

cat /tmp/mypkg.log |
        grep '牡牛座'

cat /tmp/mypkg.log |
        grep '双子座'

cat /tmp/mypkg.log |
        grep '獅子座'

cat /tmp/mypkg.log |
        grep '乙女座'

cat /tmp/mypkg.log |
        grep '天秤座'

cat /tmp/mypkg.log |
        grep '蠍座'

cat /tmp/mypkg.log |
        grep '射手座'

cat /tmp/mypkg.log |
        grep '山羊座'

cat /tmp/mypkg.log |
        grep '水瓶座'

cat /tmp/mypkg.log |
        grep '魚座'
