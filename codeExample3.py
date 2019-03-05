def main():
    fileName = input("请输入你要打开的文件名")
    filedata = open(fileName, 'r')
    for i in filedata:
        print(i)
    filedata.close()
main()