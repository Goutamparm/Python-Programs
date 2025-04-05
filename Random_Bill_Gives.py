################## Random Bill Gives ##################
import random

friends=["akash","harsh","goutam","darshan","kishore"]
random_person=random.randint(0,len(friends))
if random_person==0:
    print(friends[0])
elif random_person == 1:
    print(friends[1])
elif random_person == 2:
    print(friends[2])
elif random_person == 3:
    print(friends[3])
else:
    print(friends[4])
