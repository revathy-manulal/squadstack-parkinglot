class Vehicle:
	def __init__(self, regno, driver_age):
		self.regno = regno
		self.driver_age = driver_age


class ParkingLot:
	def __init__(self):
		self._capacity = None
		self._slots = []
		self._numOfOccupiedSlots = 0

	def create_parking_lot(self, capacity):
		self._slots = [None] * capacity
		self._capacity = capacity
		return self._capacity

	def get_capacity(self):
		if self._capacity is None:
			return None
		else:
			return self._capacity

	def get_availability(self):
		if self._capacity == self._numOfOccupiedSlots:
			return False
		else:
			return True

	def _get_empty_slot(self):
		for i in range(len(self._slots)):
			if self._slots[i] == None:
				return i

	def park(self, regno, driver_age):
		if self._numOfOccupiedSlots < self._capacity: 
			slot_no = self._get_empty_slot()
			self._slots[slot_no] = Vehicle(regno, driver_age)
			slot_no += 1
			self._numOfOccupiedSlots = self._numOfOccupiedSlots + 1
			return slot_no
		else:
			return False


	def leave(self, slot_no):
		if self._numOfOccupiedSlots > 0 and self._slots[slot_no - 1] != None:
			car_info = self._slots[slot_no - 1] 
			self._slots[slot_no - 1] = None
			self._numOfOccupiedSlots = self._numOfOccupiedSlots - 1
			return car_info
		else:
			return False


	def get_slots_with_age(self, driver_age):
		slots = []
		for key, slot_info in enumerate(self._slots):
			if slot_info and slot_info.driver_age == driver_age:
				slots.append(key+1)
		return slots


	def get_slot_with_regno(self, regno):
		for i, slot_info in enumerate(self._slots):
			if slot_info and slot_info.regno == regno:
				return i+1
			else:
				continue
		return None


	def get_regno_for_driver(self, driver_age):
		regnos = []
		for slot_info in self._slots:
			if slot_info and slot_info.driver_age == driver_age:
				regnos.append(slot_info.regno)
		return regnos
			