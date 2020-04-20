#pm2.5.py
#空气质量提醒

def main():
    PM=eval(input("What is today's PM2.5? "))
    # 打印相应提醒
    if PM > 75:
        print("Unhealthy. Be careful!")    #仅>75提醒
    if PM < 35:
        print("Good. Go running!")    #仅<35提醒，35-75之间不提醒
main()
