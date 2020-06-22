#! /usr/bin/env python
# -*- coding: utf-8 -*-

import socket


def get_ip_status(ip, port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server.connect((ip, port))
        print('{0} port {1} is open'.format(ip, port))
    except Exception as err:
        print('{0} port {1} is not open'.format(ip, port))
    finally:
        server.close()


if __name__ == '__main__':
    host = '127.0.0.1'
    for port in range(3305, 3307):
        get_ip_status(host, port)