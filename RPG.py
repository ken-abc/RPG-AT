import re
import time
import ast
from prettytable import PrettyTable


class mainl:
    def shows(rd):
        with open("lit", "r") as f:
            fil = f.readlines()
            data = fil[0]
            data = ast.literal_eval(data)
            fil = fil[1]
            fil = list(eval(fil))
            tb = PrettyTable()
            tb.field_names = ["匹配到的模块", "所适用的操作系统"]
        for i in range(len(fil)):
            file = fil[int(i)]
            if re.findall(f".*{rd}.*", file):
                abc = data[file]
                tb.add_row([file, abc])

        print(tb)

    def showw(rd):
        with open("lit", "r") as f:
            data = f.readline()
        data = ast.literal_eval(data)
        abc = data[str(rd[0])]
        tb = PrettyTable()
        tb.field_names = ["查找到的模块", "所适用的操作系统"]
        tb.add_row([rd[0], abc])
        print(tb)

    def showw_1():
        tb = PrettyTable()
        try:
            with open("lit", "r") as f:
                fil = f.readlines()
                data = fil[0]
                data = ast.literal_eval(data)
                fil = fil[1]
                fil = list(eval(fil))

        except:
            print("[E] E:?? open")
        tb.field_names = ["索引列表里的模块", "所适用的操作系统"]
        for i in range(len(fil)):
            tb.add_row([fil[int(i)], data[fil[int(i)]]])
        print(tb)

    def withtt(rd):
        ree = f"bin.{rd[0]}"
        red = ree.replace("\\", ".")
        with open("info.py", "w") as ff:
            ff.write(f"def mainll(): \n from {red} import main \n main()")
        from info import mainll

        mainll()

    def janzao(d):

        if re.findall("use (.*)", d):
            try:
                rd = re.findall("use (.*)", str(d))
            except:
                print("[E] E:use ??")
            else:
                mainl.withtt(rd)
        elif d == "help":
            print("[?] help")
        elif d == "show":
            mainl.showw_1()
        elif re.findall("show (.*)", d):
            try:

                rd = re.findall("show (.*)", str(d))

            except:
                print("[E] E:show ??")
            else:
                mainl.showw(rd)
        elif re.findall("shows (.*)", d):
            try:
                rd = re.findall("shows (.*)", str(d))
            except:
                print("[E] E:shows ??")
            else:
                mainl.shows(rd)
        else:
            print("[E] E:?? help")

    def scanf():

        while True:
            d = input("RPG >")
            if d:
                mainl.janzao(d)
            else:
                print("[E] E:you is one 'd' ")


if __name__ == "__main__":
    mainl.scanf()
