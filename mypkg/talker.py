#!/user/bin/python3
# SPDX-FileCopyrightText: 2023 Soshi Saiki　　　　　
# SPDX-License-Identifier: BSD-3-Clause

import rclpy                     #ROS 2のクライアントのためのライブラリ
from rclpy.node import Node      #ノードを実装するためのNodeクラス（クラスは第10回で）
from person_msgs.srv import Query   #通信の型（16ビットの符号付き整数）

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
    if request.name == "上田隆一":
        response.age = 44
    else:
        response.age = 255

    return response

rclpy.init()
node = Node("talker")
#talker = Talker(node)
srv = node.create_service(Query, "query", cb)
rclpy.spin(node)

#if __name__ == '__main__':
    #main()
