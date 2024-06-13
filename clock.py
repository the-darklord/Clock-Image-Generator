import cv2
import numpy as np
import math
import random

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
    
    cv2.circle(clock_image, center, radius, (0, 0, 0), 8)
    
    for i in range(12):
        angle = i * 30
        x_inner = int(center[0] + (radius - 40) * math.sin(math.radians(angle)))
        y_inner = int(center[1] - (radius - 40) * math.cos(math.radians(angle)))
        x_outer = int(center[0] + radius * math.sin(math.radians(angle)))
        y_outer = int(center[1] - radius * math.cos(math.radians(angle)))
        cv2.line(clock_image, (x_inner, y_inner), (x_outer, y_outer), (0, 0, 0), 5)

        label_angle = angle
        label_radius = radius - 70
        label_x = int(center[0] + label_radius * math.sin(math.radians(label_angle)))
        label_y = int(center[1] - label_radius * math.cos(math.radians(label_angle)))
        cv2.putText(clock_image, str(i if i != 0 else 12), (label_x - 25, label_y + 20), 
                    cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 0), 5, cv2.LINE_AA)

    hour_angle = (hour % 12 + minute / 60) * 30
    minute_angle = minute * 6

    draw_hand(clock_image, center, hour_angle, radius * 0.4, (0, 0, 255), 12)
    draw_hand(clock_image, center, minute_angle, radius * 0.7, (0, 255, 0), 10)
    
    label_position = (width // 2 - 300, height - 50)
    cv2.putText(clock_image, f"Current Time: {current_time_str}", label_position, 
                cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 0), 5, cv2.LINE_AA)

    return clock_image


if __name__ == '__main__':
    number_of_images = int(input("Enter Number of Clock Images to generate : "))
    for i in range(1,number_of_images+1):
        hour = random.randint(1,12)
        minute = random.randint(0,59)
        current_time_str = f'{hour}:{minute if minute>=10 else '0'+str(minute)}'
        clock_image = draw_clock(hour, minute, current_time_str)
        cv2.imwrite(f'images/clock_{i}.png', clock_image)
    print(f"Successfully generated {number_of_images} images")