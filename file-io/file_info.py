def fileInfo():
    fo = open("../files/hello.txt", "r")
    print("File Name", fo.name)
    print("File Mode ", fo.mode)
    print("Is Closed", fo.closed)
    fo.close()

    print("After Closed", fo.closed)


fileInfo()
