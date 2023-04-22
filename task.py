from datetime import datetime

# datetime object containing current date and time
begin = datetime.now()

for i in range(1000000):
    print(i)

print(begin)
print(datetime.now())