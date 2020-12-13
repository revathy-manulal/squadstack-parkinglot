
from utils import create_parking_lot, park_car, leave_slot, \
	get_slots_with_driver_age, get_slot_by_car_registration, \
	get_vehical_regno_for_driver
	

def executeCommand(parkingLot, command):
	if command[0] == 'Create_parking_lot':
		parkingLot = create_parking_lot(command[1])
	elif command[0] == 'Park':
		print(park_car(parkingLot, command[1], command[3]))
	elif command[0] == 'Leave':
		print(leave_slot(parkingLot, command[1]))
	elif command[0] == 'Slot_numbers_for_driver_of_age':
		print(get_slots_with_driver_age(parkingLot, command[1]))
	elif command[0] == 'Slot_number_for_car_with_number':
		print(get_slot_by_car_registration(parkingLot, command[1]))
	elif command[0] == 'Vehicle_registration_number_for_driver_of_age':
		print(get_vehical_regno_for_driver(parkingLot, command[1]))
	else:
		print('Undefined command!')
	return parkingLot
	
"""
Read input command from file_inputs.txt
and execute commands one by one
"""
def main():
	parkingLot = None
	try:
		with open('file_inputs.txt') as file:
			commands = file.readlines()
			for command in commands:
				split_command = command.strip().split()
				parkingLot = executeCommand(parkingLot, split_command)

	except Exception as e:
		print(e)

if __name__ == '__main__':
	main()