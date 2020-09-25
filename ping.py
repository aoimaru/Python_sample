# -*- coding: utf-8 -*-
import subprocess

class Ping(object):
    def __init__(self, hosts):
        for host in hosts:
            # pingコマンド
            ping = subprocess.Popen(["ping", "-c", "1", host],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )

            # ping試験
            out, error = ping.communicate()

            # 接続できなかったら
            if error:
                print('[NG]: ' +  host + ', Msg->\'' + error.rstrip() + '\'')

            # 接続できたら
            else:
                print('[OK]: ' +  host)

def main():
    # ping試験するホスト
    hosts = ['www.google.com', 'algorithm.joho.info',]

    # ping試験
    Ping(hosts)

if __name__ == '__main__':
    main()
