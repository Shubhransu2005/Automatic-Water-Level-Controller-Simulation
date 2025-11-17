import time
import random
# Constants
TANK_HEIGHT = 100  # in cm
LOWER_THRESHOLD = 30  # cm of water (motor ON)
UPPER_THRESHOLD = 90  # cm of water (motor OFF)

motor_status = "OFF"

print("Automatic Water Level Controller Simulation\n")

for i in range(15):  # Simulate 15 readings
    # Simulate distance from sensor (in cm)
    distance = random.randint(5, TANK_HEIGHT)
    water_level = TANK_HEIGHT - distance  # calculate water level

    # Motor control logic
    if water_level <= LOWER_THRESHOLD:
        motor_status = "ON"
    elif water_level >= UPPER_THRESHOLD:
        motor_status = "OFF"

    # Display output
    print(f"Reading {i+1}: Water Level = {water_level} cm | Motor = {motor_status}")

    time.sleep(1)

print("\nSimulation Ended.")



