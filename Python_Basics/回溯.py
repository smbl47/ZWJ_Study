import traceback

try:
    lis = [11, 22, 33, 44]
    print("***************************")
    print(lis[4])
except:
    traceback.print_exc()
