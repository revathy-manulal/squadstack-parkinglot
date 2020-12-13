import parking_lot

"""
Creates a parking lot
Args:
    size: size of the parking lot
Returns:
    parkingLot: parking lot instance
"""
def create_parking_lot(size):
	parkingLot = parking_lot.ParkingLot()
	parkingLot.create_parking_lot(int(size))
	print('Created parking of ' + size + ' slots')
	return parkingLot


"""
Parks a car in parking lot
Args:
    regno: registration number of car
	driver_age: age of the driver
Returns:
    status: status
"""
def park_car(parkingLot, regno, driver_age):
	
	if parkingLot is None:
		return 'Parking lot has not been created yet'

	available = parkingLot.get_availability()
	if not available:
		return 'Sorry, parking lot is full!'

	valid_slot = parkingLot.park(regno, int(driver_age))

	if valid_slot:
		status = 'Car with vehicle registration number "{0}" '\
			'has been parked at slot number {1}'.format(regno, valid_slot)
	else:
		status = 'Car could not be parked'

	return status


"""
Leaves the particular slot
Args:
    slot: slot number in parking lot
Returns:
    status: status
"""
def leave_slot(parkingLot, slot):
	
	if parkingLot is None:
		return 'Parking lot has not been created yet!'
	slot = int(slot)
	capacity = parkingLot.get_capacity()
	if slot < 1 or slot > capacity:
		return 'No such lot exists!'
	car_info = parkingLot.leave(slot)
	
	if not car_info:
		status = 'No car found this in this slot!'
	else:
		status = 'Slot number {2} vacated, the car with vehicle registration number "{0}" '\
			'left the space, the driver of the car '\
			'was of age {1}'.format(car_info.regno, car_info.driver_age, slot)

	return status


"""
Returns parking slots where the age of the driver
is same the requested age
Args:
    driver_age: age of the driver
Returns:
    status: status
"""
def get_slots_with_driver_age(parkingLot, driver_age):
	valid_slots = parkingLot.get_slots_with_age(int(driver_age))
	status = ', '.join(map(str, valid_slots))
	return status


"""
Returns slot in parking lot where the specified car is parked
Args:
    regno: registration number of car
Returns:
    status: status
"""
def get_slot_by_car_registration(parkingLot, regno):
	valid_slot = parkingLot.get_slot_with_regno(regno)
	if not valid_slot:
		return 'No such car found!'
	return valid_slot


"""
Returns registration number of cars where the drivers of the car
are of the specified age
Args:
    driver_age: age of the driver
Returns:
    status: status
"""
def get_vehical_regno_for_driver(parkingLot, driver_age):
	valid_regnos = parkingLot.get_regno_for_driver(int(driver_age))

	if valid_regnos:
		status = ', '.join(map(str, valid_regnos))
	else:
		status = 'No such cars found!'
	return status


