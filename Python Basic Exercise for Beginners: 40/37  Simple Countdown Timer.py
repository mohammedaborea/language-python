"""Create a countdown timer that starts from a given
 number and counts down to zero using a while loop."""
import time

start_acount=5
while start_acount>0:
    print(start_acount,sep=" ",end=" ")
    time.sleep(1)
    start_acount=start_acount-1
print("Finsh")
