import Adafruit_BBIO.GPIO as GPIO
import random
import time
import os

class LED():
    """ LED Class """
    pin             = None
    on_value        = None
    off_value       = None
    
    def __init__(self, pin=None, active_high=True):
        """ Initialize variables and set up the LED """
        if (pin == None):
            raise ValueError("Pin not provided for LED()")
        else:
            self.pin = pin
        
        # By default the values are determined by the active_high variable
        if active_high:
            self.on_value  = GPIO.HIGH
            self.off_value = GPIO.LOW
        else:
            self.on_value  = GPIO.LOW
            self.off_value = GPIO.HIGH  
        
            

        # Initialize the hardware components        
        self._setup()
    
    # End def
    
    
    def _setup(self):
        """ Setup the hardware components. """
        # Initialize LED
        GPIO.setup(self.pin, GPIO.OUT)
        
        
        self.off()

    # End def


    def is_on(self):
        """ Is the LED on?
        
           Returns:  True  - LED is ON
                     False - LED is OFF
        """
        
        # !!! NEED TO IMPLEMENT !!! #
        return GPIO.input(self.pin) == self.on_value 
        # !!! NEED TO IMPLEMENT !!! #

    # End def

    
    def on(self):
        """ Turn the LED ON """

        GPIO.output(self.pin, self.on_value)
    
    # End def
    
    
    def off(self):
        """ Turn the LED OFF """

        GPIO.output(self.pin, self.off_value)
    
    # End def


    def cleanup(self):
        """ Cleanup the hardware components. """
        # Turn LED off 
        self.off()
        


