# mypkg

![test](https://github.com/Sousaiky/mypkg/actions/workflows/test.yml/badge.svg)

## mypkgについて

mypkgは千葉工業大学の2023年度ロボットシステム学の授業内課題である。
また、このリポジトリははros2のパッケージです。  

## コマンドの使用例

# talker.py  
このノードは誕生日を受け取ると、その人の星座を返し、それ以外の物を受け取るとその人の運勢を返すサービスです。  

サービス名は/queryです  

動作例  

'''
端末１
$ ros2 run mypkg talker

端末２
$ ros2 service call /query person_msgs/srv/Query "birthday: 813"
waiting for service to become available...
requester: making request: person_msgs.srv.Query_Request(birthday=813)

response:
person_msgs.srv.Query_Response(age='獅子座')


