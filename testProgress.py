from tqdm import tqdm
import time

myList = []
for i in range(10):
    myList.append(i)

for i in tqdm(myList, desc="Loading..."):
    time.sleep(0.5)
	
print("Complete.")
