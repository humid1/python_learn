import time

num = 1
while True :
    print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
    # 休眠1秒
    time.sleep(1)
    num += 1
    if (num == 5) :
        print("end...")
        break  