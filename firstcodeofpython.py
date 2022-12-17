import time
seconds = input("Enter the number in seconds, the excat time you want a nuclear disaster")
def gettime(seconds):
    while seconds > 0 :
        min = int(seconds/60)
        aoksdfak = int(seconds%60)
        t = f'{min}:{aoksdfak}'
        print(t)
        time.sleep(1)
        seconds = seconds-1
        
    print("timeuppp")
gettime(int(seconds))


