 #PuzzlOR December 2016 - Galaxy on fire

# tenata

import sys
import operator
from operator import itemgetter

def main():
	try:
		
		"""
		Ship Name, Cargo, Weapons, Equipment, Cost
		"""
		ship_info = {
			"Cicero":	[25,2,6,51975],
			"Cormorant":[350,0,8,168900],
			'Dace':		[38,4,5,235600],
			'Hatsuyuki':[28,2,8,171900],
			"H'Soc":	[45,2,7,150000],
			"N'Tirrk":	[80,2,8,250000],
			"Razor6":	[60,4,6,294900],
			"Taipan":	[50,3,5,100100],
			"Teneta":	[65,2,7,125400],
			"Type43":	[30,2,6,72500]
		}

		cargo_info = [[ship,ship_info[ship][0]] for ship in ship_info]
		weapon_info = [[ship,ship_info[ship][1]] for ship in ship_info]
		equipment_info = [[ship,ship_info[ship][2]] for ship in ship_info]
		cost_info = [[ship,ship_info[ship][3]] for ship in ship_info]

		sorted_cargo = sorted(cargo_info,key=operator.itemgetter(1))
		sorted_weapon = sorted(weapon_info,key=operator.itemgetter(1))
		sorted_equipment = sorted(equipment_info,key=operator.itemgetter(1))
		sorted_cost = sorted(cost_info,key=operator.itemgetter(1), reverse=True)

		options = []
		options.append(sorted_cargo[0][0])
		options.append(sorted_weapon[0][0])
		options.append(sorted_equipment[0][0])
		options.append(sorted_cost[0][0])

		print(options)

		# #option_info = {}
		# for option in options:
		# 	if option not in option_info:
		# 		option_info[option] = 1
		# 	else:
		# 		option_info[option]+=1
		
		# sorted_option = sorted(option_info,key=operator.itemgetter(1))
		# print(sorted_option)
		
	except:
		e = sys.exc_info()
		print(e)
		sys.exit(1)

if __name__ == "__main__":
	main()