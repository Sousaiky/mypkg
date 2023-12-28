# SPDX-FileCopyrightText: 2023 Soshi Saiki　　　　　
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from person_msgs.srv import Query

def main():
    rclpy.init()
    node = Node("listener")
    client = node.create_client(Query, 'query') #サービスのクライアントの作成
    while not client.wait_for_service(timeout_sec=1.0): #サービスの待ち待ち
        node.get_logger().info('待機中')

    req = Query.Request()
    req.birthday = 320
    future = client.call_async(req) #非同期でサービスを呼び出し

    while rclpy.ok():
        rclpy.spin_once(node) #一回だけサービスを呼び出したら終わり
        if future.done():     #終わっていたら
            try:
                response = future.result() #結果を受取り
            except:
                node.get_logger().info('呼び出し失敗')
            else: #このelseは「exceptじゃなかったら」という意味のelse
                node.get_logger().info("君は{}".format(response.age))

            break #whileを出る

    req = Query.Request()
    req.birthday = 419
    future = client.call_async(req) #非同期でサービスを呼び出し

    while rclpy.ok():
        rclpy.spin_once(node) #一回だけサービスを呼び出したら終わり
        if future.done():     #終わっていたら
            try:
                response = future.result() #結果を受取り
            except:
                node.get_logger().info('呼び出し失敗')
            else: #このelseは「exceptじゃなかったら」という意味のelse
                node.get_logger().info("君は{}".format(response.age))

            break #whileを出る

    req = Query.Request()
    req.birthday = 521
    future = client.call_async(req) #非同期でサービスを呼び出し

    while rclpy.ok():
        rclpy.spin_once(node) #一回だけサービスを呼び出したら終わり
        if future.done():     #終わっていたら
            try:
                response = future.result() #結果を受取り
            except:
                node.get_logger().info('呼び出し失敗')
            else: #このelseは「exceptじゃなかったら」という意味のelse
                node.get_logger().info("君は{}".format(response.age))

            break #whileを出る

    req = Query.Request()
    req.birthday = 622
    future = client.call_async(req) #非同期でサービスを呼び出し

    while rclpy.ok():
        rclpy.spin_once(node) #一回だけサービスを呼び出したら終わり
        if future.done():     #終わっていたら
            try:
                response = future.result() #結果を受取り
            except:
                node.get_logger().info('呼び出し失敗')
            else: #このelseは「exceptじゃなかったら」という意味のelse
                node.get_logger().info("君は{}".format(response.age))

            break #whileを出る

    req = Query.Request()
    req.birthday = 723
    future = client.call_async(req) #非同期でサービスを呼び出し

    while rclpy.ok():
        rclpy.spin_once(node) #一回だけサービスを呼び出したら終わり
        if future.done():     #終わっていたら
            try:
                response = future.result() #結果を受取り
            except:
                node.get_logger().info('呼び出し失敗')
            else: #このelseは「exceptじゃなかったら」という意味のelse
                node.get_logger().info("君は{}".format(response.age))

            break #whileを出る

    req = Query.Request()
    req.birthday = 823
    future = client.call_async(req) #非同期でサービスを呼び出し

    while rclpy.ok():
        rclpy.spin_once(node) #一回だけサービスを呼び出したら終わり
        if future.done():     #終わっていたら
            try:
                response = future.result() #結果を受取り
            except:
                node.get_logger().info('呼び出し失敗')
            else: #このelseは「exceptじゃなかったら」という意味のelse
                node.get_logger().info("君は{}".format(response.age))

            break #whileを出る

    req = Query.Request()
    req.birthday = 922
    future = client.call_async(req) #非同期でサービスを呼び出し

    while rclpy.ok():
        rclpy.spin_once(node) #一回だけサービスを呼び出したら終わり
        if future.done():     #終わっていたら
            try:
                response = future.result() #結果を受取り
            except:
                node.get_logger().info('呼び出し失敗')
            else: #このelseは「exceptじゃなかったら」という意味のelse
                node.get_logger().info("君は{}".format(response.age))

            break #whileを出る

    req = Query.Request()
    req.birthday = 1023
    future = client.call_async(req) #非同期でサービスを呼び出し

    while rclpy.ok():
        rclpy.spin_once(node) #一回だけサービスを呼び出したら終わり
        if future.done():     #終わっていたら
            try:
                response = future.result() #結果を受取り
            except:
                node.get_logger().info('呼び出し失敗')
            else: #このelseは「exceptじゃなかったら」という意味のelse
                node.get_logger().info("君は{}".format(response.age))

            break #whileを出る

    req = Query.Request()
    req.birthday = 1122
    future = client.call_async(req) #非同期でサービスを呼び出し

    while rclpy.ok():
        rclpy.spin_once(node) #一回だけサービスを呼び出したら終わり
        if future.done():     #終わっていたら
            try:
                response = future.result() #結果を受取り
            except:
                node.get_logger().info('呼び出し失敗')
            else: #このelseは「exceptじゃなかったら」という意味のelse
                node.get_logger().info("君は{}".format(response.age))

            break #whileを出る

    req = Query.Request()
    req.birthday = 1221
    future = client.call_async(req) #非同期でサービスを呼び出し

    while rclpy.ok():
        rclpy.spin_once(node) #一回だけサービスを呼び出したら終わり
        if future.done():     #終わっていたら
            try:
                response = future.result() #結果を受取り
            except:
                node.get_logger().info('呼び出し失敗')
            else: #このelseは「exceptじゃなかったら」という意味のelse
                node.get_logger().info("君は{}".format(response.age))

            break #whileを出る

    req = Query.Request()
    req.birthday = 119
    future = client.call_async(req) #非同期でサービスを呼び出し

    while rclpy.ok():
        rclpy.spin_once(node) #一回だけサービスを呼び出したら終わり
        if future.done():     #終わっていたら
            try:
                response = future.result() #結果を受取り
            except:
                node.get_logger().info('呼び出し失敗')
            else: #このelseは「exceptじゃなかったら」という意味のelse
                node.get_logger().info("君は{}".format(response.age))

            break #whileを出る

    req = Query.Request()
    req.birthday = 218
    future = client.call_async(req) #非同期でサービスを呼び出し

    while rclpy.ok():
        rclpy.spin_once(node) #一回だけサービスを呼び出したら終わり
        if future.done():     #終わっていたら
            try:
                response = future.result() #結果を受取り
            except:
                node.get_logger().info('呼び出し失敗')
            else: #このelseは「exceptじゃなかったら」という意味のelse
                node.get_logger().info("君は{}".format(response.age))

            break #whileを出る

    node.destroy_node() #ノードの後始末
    rclpy.shutdown()    #ノードの後始末

if __name__ == '__main__': #ライブラリと区別するためのPythonの記法
    main()
