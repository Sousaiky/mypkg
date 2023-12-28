#!/user/bin/python3
# SPDX-FileCopyrightText: 2023 Soshi Saiki　　　　　
# SPDX-License-Identifier: BSD-3-Clause

import rclpy                     #ROS 2のクライアントのためのライブラリ
from rclpy.node import Node      #ノードを実装するためのNodeクラス（クラスは第10回で）
from person_msgs.srv import Query   #通信の型（16ビットの符号付き整数）
import random

#class Talker():
    #def __init__(self, node):  # オブジェクトを作ると呼ばれる関数
        #self.pub = node.create_publisher(Int16, "countup", 10)
        #self.n = 0
        #node.create_timer(0.5, self.cb)
        # ↑ selfはオブジェクトのこと
        # ↑ オブジェクトにひとつパブリッシャと変数をもたせる。
    #def cb(self):
        #msg = Int16()
        #msg.data = self.n
        #self.pub.publish(msg)
        #self.n += 1

#def main():

def cb(request, response):
    if 321 <= request.birthday <= 419:
        response.age = "牡羊座"#random.choice(("大吉", "中吉", "吉", "凶"))#44
    elif 420 <= request.birthday <= 520:
        response.age = "牡牛座"
    elif 521 <= request.birthday <= 621:
        response.age = "双子座"
    elif 622 <= request.birthday <= 722:
        response.age = "蟹座"
    elif 723 <= request.birthday <= 822:
        response.age = "獅子座"
    elif 823 <= request.birthday <= 922:
        response.age = "乙女座"
    elif 923 <= request.birthday <= 1023:
        response.age = "天秤座"
    elif 1024 <= request.birthday <= 1122:
        response.age = "蠍座"
    elif 1123 <= request.birthday <= 1221:
        response.age = "射手座"
    elif 1222 <= request.birthday <= 1231:
        response.age = "山羊座"
    elif 101 <= request.birthday <= 119:
        response.age = "水瓶座"
    elif 229 <= request.birthday <= 320:
        response.age = "魚座"
    else:
        response.age = "無し"

    return response

rclpy.init()
node = Node("talker")
#talker = Talker(node)
srv = node.create_service(Query, "query", cb)
rclpy.spin(node)

#if __name__ == '__main__':
    #main()
