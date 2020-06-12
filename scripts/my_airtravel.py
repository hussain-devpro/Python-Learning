# Class defines the structure and behavior of the object
# It works as template for creating objects
# It controls object's initial state, attributes, methods

# class MyClassName:
#     """Class name uses UpperCamelCase"""
#     pass  # for empty class, we need at least a pass statement
#
# f = MyClassName()
# print(type(f))  # result is module_name.MyClassName  __main__.MyClassName
#
# method has default parameter as self, similar to this in java

# Class has initializer method, it must be called __init__(). It should not return any thing.
# It is called after the object has been created to configure it. It's not a constructor.

class Flight:
    """A Flight with AirCraft"""

    def __init__(self, number, aircraft):
        self._number = number
        self._aircraft = aircraft
        rows, seats = self._aircraft.seating_plan()  # here rows and seats are local variables
        self._seating = [None] + [{letter: None for letter in seats} for _ in rows]

    def number(self):
        return self._number

    def airline(self):
        return self.number[:2]  # returns the airline code like AF for airfrance

    def aircraft(self):
        return self._aircraft

    def aircraft_model(self):
        return self._aircraft.model()

    def allocate_seat(self, seat, passanger):
        """
        Allocate seats to passanger

        :param seat: A seat designator '12C'
        :param passanger: passanger name
        :return: None
        """
        row, letter = self._parse_seat(seat)

        if self._seating[row][letter] is not None:
            raise ValueError(f"Seat {seat} is already occupied")

        self._seating[row][letter] = passanger

    def relocate_passanger(self, from_seat, to_seat):
        from_row, from_letter = self._parse_seat(from_seat)
        if self._seating[from_row][from_letter] is None:
            raise ValueError(f"No passanger to relocate in Seat {from_seat}")

        to_row, to_letter = self._parse_seat(to_seat)
        if self._seating[to_row][to_letter] is not None:
            raise ValueError(f"Seat {to_seat} is already occupied")

        self._seating[to_row][to_letter] = self._seating[from_row][from_letter]
        self._seating[from_row][from_letter] = None

    def num_avail_seats(self):
        return sum(sum(1 for s in row.values() if s is None)
                   for row in self._seating if row is not None)

    def _parse_seat(self, seat):
        rows, seat_letters = self._aircraft.seating_plan()
        letter = seat[-1]  # here we are retrieving the seat letter provided for booking, C char from '12C'
        row_text = seat[:-1]  # here we are getting the row number, 12 from '12C'
        row = int(row_text)  # converting str to int
        return row, letter


class AirCraft:

    def __init__(self, registration, model, num_rows, num_seats_per_row):
        self._registration = registration
        self._model = model
        self._num_rows = num_rows
        self._num_seats_per_row = num_seats_per_row

    def registration(self):
        return self._registration

    def model(self):
        return self._model

    def seating_plan(self):  # returning a tuple with range iterator and rows. for ex 6 rows will return ABCDEF
        return range(1, self._num_rows + 1), "ABCDEFGHJK"[:self._num_seats_per_row]

def main():
    f = Flight()
    print(f.number())
    print(Flight.number(f))

if __name__ == '__main__':
    main()



