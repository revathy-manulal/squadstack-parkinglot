import unittest
from utils import create_parking_lot, park_car, leave_slot, \
    get_slots_with_driver_age, get_slot_by_car_registration, get_vehical_regno_for_driver

"""
Parking lot testcases
"""
class TestParkingLot(unittest.TestCase):
    
    def test_create_parking_lot(self):
        parkingLot = create_parking_lot(str(8))
        self.assertEqual(8, parkingLot.get_capacity())


    def test_parking_lot_allocation(self):
        parkingLot = create_parking_lot(str(6))
        testResponse = park_car(parkingLot, 'PB-01-HH-1234', '27')
        self.assertEqual('Car with vehicle registration number "PB-01-HH-1234" '\
            'has been parked at slot number 1', testResponse)


    def test_leave_slot_free(self):
        parkingLot = create_parking_lot(str(6))
        park_car(parkingLot, 'PB-01-HH-1234', '21')
        testResponse = leave_slot(parkingLot, '1')
        self.assertEqual('Slot number 1 vacated, the car with vehicle '\
            'registration number "PB-01-HH-1234" left the space, '\
            'the driver of the car was of age 21', testResponse)


    def test_get_car_slot_number(self):
        parkingLot = create_parking_lot(str(6))
        park_car(parkingLot, 'PB-01-HH-1234', '27')
        testResponse = get_slot_by_car_registration(parkingLot, 'PB-01-HH-1234')
        self.assertEqual(testResponse, 1)


    def test_get_drivers_of_age(self):
        parkingLot = create_parking_lot(str(6))
        park_car(parkingLot, 'PB-01-HH-1234', '27')
        testResponse = get_slots_with_driver_age(parkingLot, '27')
        self.assertEqual(testResponse, '1')

    def test_get_regno_with_driver_age(self):
        parkingLot = create_parking_lot(str(6))
        park_car(parkingLot, 'PB-01-HH-1234', '27')
        park_car(parkingLot, 'PB-01-HH-1233', '27')
        testResponse = get_vehical_regno_for_driver(parkingLot, '27')
        self.assertEqual(testResponse, 'PB-01-HH-1234, PB-01-HH-1233')


    def test_parking_without_car_park(self):
        testResponse = park_car(None, 'PB-01-HH-1234', 20)
        self.assertEqual('Parking lot has not been created yet', testResponse)


    def test_leave_slot_empty(self):
        parkingLot = create_parking_lot(str(6))
        testResponse = leave_slot(parkingLot, '1')
        self.assertEqual('No car found this in this slot!', testResponse)


    def test_unknown_car_slot_number(self):
        parkingLot = create_parking_lot(str(6))
        park_car(parkingLot, 'PB-01-HH-1234', '27')
        testResponse = get_slot_by_car_registration(parkingLot, 'PB-01-HH-1233')
        self.assertEqual(testResponse, 'No such car found!')


    def test_full_car_parking_lot(self):
        parkingLot = create_parking_lot(str(1))
        park_car(parkingLot, 'PB-01-HH-1234', '27')
        testResponse = park_car(parkingLot, 'PB-01-HH-1222', '27')
        self.assertEqual('Sorry, parking lot is full!', testResponse)


    def test_leave_slot_cannot_exit(self):
        parkingLot = create_parking_lot(str(6))
        park_car(parkingLot, 'PB-01-HH-1234', '27')
        testResponse = leave_slot(parkingLot, '7')
        self.assertEqual('No such lot exists!', testResponse)


    def test_leave_slot_unoccupied(self):
        parkingLot = create_parking_lot(str(6))
        park_car(parkingLot, 'PB-01-HH-1234', '27')
        testResponse = leave_slot(parkingLot, '2')
        self.assertEqual('No car found this in this slot!', testResponse)


    def test_leave_slot_not_defined(self):
        testResponse = leave_slot(None, '1')
        self.assertEqual('Parking lot has not been created yet!', testResponse)


if __name__ == '__main__':
    unittest.main()