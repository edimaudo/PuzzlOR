#PuzzlOR February 2014 Pizza Delivery
import random
import sys
import math

"""
assumption only 1 order per round trip

"""
def calc_avg(alist):
	total = 0
	count = 0
	for value in alist:
		if value > 0:
			total+=value
			count+=1
	return math.ceil(total/count)

def calc_driver(alist):
	driverCount = 0
	total = 0
	for value in alist:
		total+=value
		if total  <= 60:
			driverCount+=1
		if total >= 60:
			total = 0
	return driverCount

def main():
	try:
		random.seed(1)
		driver_data = []
		count_begin = 0
		count_end = 100000
		while (count_begin < count_end):

			delivery_data = []
			interarrival_time = 6.0/60.0

			amount_order = int(random.expovariate(interarrival_time))
			
			for value in range(0,amount_order):
				pickup_delivery_time = math.ceil(random.uniform(20,61))
				delivery_data.append(pickup_delivery_time)
			
			driver_data.append(calc_driver(delivery_data))
			count_begin+=1
		driver_data.sort()
		print(calc_avg(driver_data))

	except:
		e = sys.exc_info()
		print(e)
		sys.exit(1)
   

if __name__ == "__main__":
    main()



