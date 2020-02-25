from datetime import timedelta
import re
print("Greetings! This is a calculator of average pace. At first you should print running kilometers and then time")
km = input("Print running Kilometers:", )
while not re.match(r'^-?\d+(?:(\,|\.)\d+)?$', km):
    print("Non correct number! Please, insert correct number!")
    km= input("Print running Kilometers:", )
    km = float(km.replace(",", "."))
th = input("Print hours: ", )
while not re.match(r'^-?\d+?$', th):
    print("Non correct number! Please, insert correct number!")
    th = input("Print hours: ", )
tm = input("Print minutes: ", )
while not re.match(r'^-?\d+?$', tm):
    print("Non correct number! Please, insert correct number!")
    tm = input("Print minutes: ", )
ts = input("Print seconds: ", )
while not re.match(r'^-?\d+?$', tm):
    print("Non correct number! Please, insert correct number!")
    ts = input("Print seconds: ", )

d = timedelta(hours=th, minutes=tm, seconds=ts)
seconds_per_km = d.seconds / km
d1 = timedelta(seconds=seconds_per_km)
minutes = (d1.seconds // 60) % 60
seconds = d1.seconds - minutes * 60
print("aver pace minutes: {0} seconds: {1}".format(minutes, seconds))
delta_per_km = timedelta(minutes=minutes, seconds=seconds)
hours_per_km = delta_per_km.seconds / 3600
velocity_km_sec =1/hours_per_km
print("velocity: {0} km\\h".format(round(velocity_km_sec, 2)))


#print("Введи первое число и нажми Enter")
#a = input()
#while not re.match(r'^-?\d+(?:(\,|\.)\d+)?$', a):
    #print("ты дурак? Введи правильное ЧИСЛО!")
    #a = input()
#a = float(a.replace(",", "."))
#print("Введи второе число и нажми Enter")
#b = input()
#while not re.match(r'^-?\d+(?:(\,|\.)\d+)?$', b):
    #print("ты опять дурак? Введи правильное число и будет тебе счастье!")
   # b = input()
#b=float(b)
#c = a + b
#print("Ответ %s" % c)
#if c == 300:
 #   print("Отсоси у тракториста")
#else:
  #  print("Для выхода нажмите Enter")
#input()