from datetime import datetime, timezone
import matplotlib.pyplot as plt
import numpy as np
import os

# Initialization, define some constants
path = os.path.dirname(os.path.abspath(__file__))
filename = r"C:\Users\ianch\OneDrive\Documents\ROAR-Academy\samples\airplane.bmp"
background = plt.imread(filename)

second_hand_length = 200
second_hand_width = 2
minute_hand_length = 150
minute_hand_width = 6
hour_hand_length = 100
hour_hand_width = 10
gmt_hand_length = 180
gmt_hand_width = 2
center = np.array([256, 256])

def clock_hand_vector(angle, length):
    return np.array([length * np.sin(angle), -length * np.cos(angle)])

# Draw an image background
fig, ax = plt.subplots()

# Remove axes
ax.axis('off')

# Run for a short time instead of infinitely for testing purposes
for _ in range(100):
    plt.imshow(background)

    # First retrieve the time
    now_time = datetime.now()
    hour = now_time.hour
    if hour > 12: hour = hour - 12
    minute = now_time.minute
    second = now_time.second

    # Calculate end points of hour, minute, second
    hour_vector = clock_hand_vector((hour + minute / 60 + second / 3600) / 12 * 2 * np.pi, hour_hand_length)
    minute_vector = clock_hand_vector((minute + second / 60) / 60 * 2 * np.pi, minute_hand_length)
    second_vector = clock_hand_vector(second / 60 * 2 * np.pi, second_hand_length)

    # Calculate GMT hour hand
    gmt_time = datetime.now(timezone.utc)
    gmt_hour = gmt_time.hour
    gmt_vector = clock_hand_vector(gmt_hour / 24 * 2 * np.pi, gmt_hand_length)

    plt.arrow(center[0], center[1], hour_vector[0], hour_vector[1], head_length=3, linewidth=hour_hand_width, color='black')
    plt.arrow(center[0], center[1], minute_vector[0], minute_vector[1], linewidth=minute_hand_width, color='black')
    plt.arrow(center[0], center[1], second_vector[0], second_vector[1], linewidth=second_hand_width, color='red')
    plt.arrow(center[0], center[1], gmt_vector[0], gmt_vector[1], head_length=3, linewidth=gmt_hand_width, color='yellow')

    plt.pause(0.1)
    plt.clf()
