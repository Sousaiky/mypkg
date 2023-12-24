import rclpy                     #ROS 2のクライアントのためのライブラリ
from rclpy.node import Node      #ノードを実装するためのNodeクラス（クラスは第10回で）
from std_msgs.srv import Int16   #通信の型（16ビットの符号付き整数）

class Talker():
    def __init__(self):  # オブジェクトを作ると呼ばれる関数
        self.pub = node.create_publisher(Int16, "countup", 10)
        self.n = 0
        node.create_timer(0.5,self.cb)
        # ↑ selfはオブジェクトのこと
        # ↑ オブジェクトにひとつパブリッシャと変数をもたせる。
def cb():
    msg = Int16()
    msg.data = self.n
    self.pub.publish(msg)
    self.n += 1

def main():
    rclpy.init()
    node = Node("talker")
    talker = Talker(node)
    rclpy.spin(node)

if __name__ == '__main__':
    main()
