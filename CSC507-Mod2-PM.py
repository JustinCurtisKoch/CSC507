import datetime
import random
import time

file_py = open('py-CSC507-Mod2-PM.txt', 'w')

start = time.time()

date = datetime.datetime.now()
print(f"PM Python script called at {date}", file = file_py)

for i in range(1000000):
	random_number = random.randint(0, 32767)
	print(random_number, file = file_py)
	
elapsed = time.time() - start
minutes = int(elapsed/60)
seconds = int(elapsed%60)
print(f"{minutes} minutes {seconds} seconds", file = file_py)