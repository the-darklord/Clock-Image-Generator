import cv2
import numpy as np
import math
import random
import os
import csv

def draw_hand(image, center, angle, length, color, thickness):
    angle_rad = math.radians(angle)
    end_x = int(center[0] + length * math.sin(angle_rad))
    end_y = int(center[1] - length * math.cos(angle_rad))
    cv2.line(image, center, (end_x, end_y), color, thickness)

def draw_clock(hour, minute, current_time_str):
    width, height = 1920, 1080
    clock_image = np.ones((height, width, 3), dtype=np.uint8) * 255
    center = (width // 2, height // 2 - 50)
    radius = min(center) - 70

    hour_angle = (hour % 12 + minute / 60) * 30
    minute_angle = minute * 6

    hour_length = radius * random.uniform(0.4,0.7)
    minute_length = radius * random.uniform(0.7,1)
    
    draw_hand(clock_image, center, hour_angle, hour_length, (0, 0, 0), 12)
    draw_hand(clock_image, center, minute_angle, minute_length, (0, 0, 0), 10)

    return clock_image

if __name__ == '__main__':
    if not os.path.exists('images'):
        os.makedirs('images')
    number_of_images = int(input("Enter Number of Clock Images to generate : "))
    with open('labels.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['File Name', 'Hour', 'Minute'])
        for i in range(1,number_of_images+1):
            hour = random.randint(1,12)
            minute = random.randint(0,59)
            current_time_str = f'{hour}:{minute if minute>=10 else '0'+str(minute)}'
            clock_image = draw_clock(hour, minute, current_time_str)
            cv2.imwrite(f'images/clock_{i}.png', clock_image)
            writer.writerow([f'clock_{i}.png', hour, minute])
    print(f"Successfully generated {number_of_images} images")