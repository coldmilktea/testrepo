'''
Created on AUG 16, 2021
@author: Jue Liu
@affiliations:  City University of Hong Kong
@project: 
(1) simulate the network slicing system with two classes of customers pooling in a queue and served by single server； 
(2) treat the two classes as one given a overall QoS requirement tau and p; 
(3) what's the resulted OoS for each class?
@task: simulate M/M/1 queue
'''

import numpy as np
import pandas as pd
import random,itertools,types,time,csv,math,copy,operator;
import matplotlib.pyplot as plt;
from scipy import stats

lambda1=2
u=4.65
r=100000


interarrival_1=np.zeros(r)
arrival_1=np.zeros(r)
arrival_1_temp=0
for i in range(r):
   interarrival_1[i]=random.expovariate(lambda1)
   arrival_1_temp=arrival_1_temp+interarrival_1[i]
   arrival_1[i]=arrival_1_temp
job1=arrival_1

print(job1)

waiting1=np.zeros(r)
waiting1_sum=0
sojourn1=np.zeros(r)
sojourn1_sum=0


print("\n")
depart_time=0

for i in range(r):

	new_arrival_time=job1[i]
	service_time=random.expovariate(u)

	start_time=max(new_arrival_time,depart_time)
	depart_time=start_time+service_time
	waiting_time=start_time-new_arrival_time
	sojourn_time=depart_time-new_arrival_time

	waiting1[i]=waiting_time
	sojourn1[i]=sojourn_time
	waiting1_sum +=waiting_time
	sojourn1_sum +=sojourn_time

	

	# print("job:",i+2,"; arrival_time",new_arrival_time,"start_time",start_time,"service_time:",service_time,"waiting:",waiting_time,"sojourn:",sojourn_time,"depart:",depart_time)
	# print("\n")

mean_waiting=waiting1_sum/r
mean_sojourn=sojourn1_sum/r

print('mean_waiting:',mean_waiting)
print('mean_sojourn:',mean_sojourn)

tau1=0.8
p1=np.sum(waiting1<tau1)/r
print(p1)