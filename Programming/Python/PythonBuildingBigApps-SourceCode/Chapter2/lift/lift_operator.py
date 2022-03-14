# lift_operator.py

import lift

# create a lift object
my_lift = lift.Lift()

# Find out what floor the lift is on
floor = my_lift.get_floor()
print("The lift is on floor", floor)

# move the lift to a new floor
my_lift.move_to_floor(5)

# Find out what floor the lift is on now
floor = my_lift.get_floor()
print("The lift has now moved to floor", floor)
