import Adafruit_BBIO.GPIO as GPIO
import random
import time
import os
from led import LED
class Button():
    """ Button Class """
    pin             = None
    unpressed_value = None
    pressed_value   = None
    sleep_time      = None
    
        
    def __init__(self, pin=None):
        """ Initialize variables and set up the button """
        if (pin == None):
            raise ValueError("Pin not provided for Button()")
        else:
            self.pin = pin
        
        # By default the unpressed_value is "1" and the pressed
        # value is "0".  This is done to make it easier to change
        # in the future
        self.unpressed_value = 1
        self.pressed_value   = 0
        
        # By default sleep time is "0.1" seconds
        self.sleep_time      = 0.1

        # Initialize the hardware components        
        self._setup()
    
    # End def
    
    
    def _setup(self):
        """ Setup the hardware components. """
        # Initialize Button
        # HW#4 TODO: (one line of code)
        #   Remove "pass" and use the Adafruit_BBIO.GPIO library to set up the button
        GPIO.setup(self.pin, GPIO.IN, pull_up_down = GPIO.PUD_UP)

    # End def


    def is_pressed(self):
        """ Is the Button pressed?
        
           Returns:  True  - Button is pressed
                     False - Button is not pressed
        """

        return (GPIO.input(self.pin) == self.pressed_value)

    # End def
    
    def got_pressed(self):
        if GPIO.input(self.pin) == 0:
            if self.pin == "P1_36":
                led = LED("P2_2")
                led.on()
                time.sleep(0.3)
                led.off()
                return 1 
            elif self.pin == "P1_34":
                led = LED("P2_4")
                led.on()
                time.sleep(0.3)
                led.off()
                return 2
            elif self.pin == "P1_35":
                led = LED("P2_6")
                led.on()
                time.sleep(0.3)
                led.off()
                return 3
            elif self.pin == "P1_33":
                led = LED("P2_8")
                led.on()
                time.sleep(0.3)
                led.off()
                return 4
            elif self.pin == "P2_34":
                print("Start Button")

            
            # Wait for the button to be released
            while GPIO.input(self.pin) == 0:
                pass # Wait for the button to be released
            
            print("Button released")
        
        time.sleep(0.05)  # Add a small delay to avoid rapid polling



    def wait_for_press(self, function=None):
        """ Wait for the button to be pressed.  This function will 
           wait for the button to be pressed and released so there
           are no race conditions.
        
           Arguments:
               function - Optional argument that is the functon to 
                          executed while waiting for the button to 
                          be pressed
        
           Returns:
               tuple - [0] Time button was pressed
                     - [1] Data returned by the "function" argument
        """
        function_return_value = None
        button_press_time     = None
        
        # Execute function if it is not None
        #   - This covers the case that the button is pressed prior 
        #     to entering this function
        if function is not None:
            function_return_value = function()
        
        # Wait for button press
        #   If the function is not None, execute the function
        #   Sleep for a short amount of time to reduce the CPU load
        #
        # HW#4 TODO: (one line of code)
        #   Update while loop condition to compare the input value of the  
        #   GPIO pin of the buton (i.e. self.pin) to the "unpressed value" 
        #   of the class (i.e. we are executing the while loop while the 
        #   button is not being pressed)
        while(GPIO.input(self.pin) == 1):
        
            if function is not None:
                function_return_value = function()
                
            time.sleep(self.sleep_time)
        
        # Record time
        button_press_time = time.time()
        
        # Wait for button release
        #   Sleep for a short amount of time to reduce the CPU load
        #
        # HW#4 TODO: (one line of code)
        #   Update while loop condition to compare the input value of the  
        #   GPIO pin of the buton (i.e. self.pin) to the "pressed value" 
        #   of the class (i.e. we are executing the while loop while the 
        #   button is being pressed)
        while(GPIO.input(self.pin) == 0):
            time.sleep(self.sleep_time)
        
        # Compute the button_press_time
        button_press_time = time.time() - button_press_time

        # Return a tuple:  (button press time, function return value)        
        return (button_press_time, function_return_value)
        
    # End def
    def start_game(self):
        if GPIO.input(self.pin) == 0:
            if self.pin == "P2_34":
                return 1
        
        
    def next_round(self):
        if GPIO.input(self.pin) == 0:
            if self.pin == "P1_31":
                return 1
        time.sleep(0.05)
    
        
        
            