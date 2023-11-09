from ht16k33 import HT16K33 
from button_test import Button
from led import LED

import Adafruit_BBIO.GPIO as GPIO
import random
import time
import os

# ------------------------------------------------------------------------
# Main script
# ------------------------------------------------------------------------

if __name__ == '__main__':
    
    try:
        while True:
            red_button = Button("P1_36")
            green_button = Button("P1_35")
            yellow_button = Button("P1_34")
            blue_button = Button("P1_33")
            start_button = Button("P2_34")
            next_button = Button("P1_31")
            display = HT16K33(1, 0x70)

    
            if start_button.start_game() == 1:
                display.text('Play')
                time.sleep(1)
                            
            
                pattern = []
                rounds = 5
                score = 0
                lost = False
                
                while lost == False:
                
                    button_pattern = []
                    num = random.randint(1, 4)
                    pattern.append(num)
                    score = score+1;
                    time.sleep(1)
                    for j in range(len(pattern)):
                        if pattern[j] == 1:
                            led = LED("P2_2")
                            led.on()
                            time.sleep(0.3)
                            led.off()
                        elif pattern[j] == 2:
                            led = LED("P2_4")
                            led.on()
                            time.sleep(0.3)
                            led.off()
                        elif pattern[j] == 3:
                            led = LED("P2_6")
                            led.on()
                            time.sleep(0.3)
                            led.off()
                        else:
                            led = LED("P2_8")
                            led.on()
                            time.sleep(0.3)
                            led.off()
                        
                    while next_button.next_round() != 1:
                        button_pattern.append(red_button.got_pressed())
                        time.sleep(0.05)
                        button_pattern.append(yellow_button.got_pressed())
                        time.sleep(0.05)
                        button_pattern.append(green_button.got_pressed())
                        time.sleep(0.05)
                        button_pattern.append(blue_button.got_pressed())
                        time.sleep(0.05)
                        button_pattern2 = [x for x in button_pattern if x is not None]
                    print(button_pattern2)
                    print(pattern)
                        
                    if button_pattern2 != pattern:
                        lost = True
                print("You Lost! Your score is: " + str(score-1))
                display.text('Lost')
                time.sleep(2)
                display.text(str(score-1))
                pass
                




            
    except KeyboardInterrupt:
        pass


    
    

