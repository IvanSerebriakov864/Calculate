from datetime import timedelta

print("Greetings! This is a calculator of average pace. At first you should print running kilometers and then time")
km=42#float(input("Print running Kilometers:", ))
t1=3#int(input("Print hours: ", ))
t2=27#int(input("Print minutes: ", ))
t3=20#int(input("Print seconds: ", ))
d = timedelta(hours=t1,minutes=t2,seconds=t3)
seconds_for_km = d.seconds / km
d1 = timedelta(seconds=seconds_for_km)
minutes = (d1.seconds // 60) % 60
seconds = d1.seconds - minutes * 60
print("minutes: {0} seconds: {1}".format(minutes, seconds))
delta_for_km = timedelta(minutes=minutes, seconds=seconds)
hours_for_km = delta_for_km.seconds / 3600
velocity_km_sec =1/hours_for_km
print("velocity {0} km\\h".format(round(velocity_km_sec, 2)))

