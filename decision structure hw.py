"""
Terrell Robertson
"""

distance = float(input("Enter the distance in miles: "))
speedlimit = float(input("Enter miles/ hour speed limit: "))
speed = float(input("Enter your average speed in miles/hour: "))

time = distance / speedlimit
speedtime = distance / speed

print(time, speedtime)

min_in_hour = 60

speedtimemin = speedtime * min_in_hour
timemin = time * min_in_hour

if speed > speedlimit:
    savedtime = timemin - speedtimemin
else:
    print("safe driver but no time saved")

print(f'time taken at speed limit: {timemin:.2f} minutes')
print(f'time taken your speed: {speedtimemin:.2f} minutes')
print(f'time saved in min: {savedtime:.2f}')