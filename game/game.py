"""
--------------------------------------------------------------------------
LED Driver
--------------------------------------------------------------------------
License:   
Copyright 2023 Ananya Lingineni

Redistribution and use in source and binary forms, with or without 
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this 
list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, 
this list of conditions and the following disclaimer in the documentation 
and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors 
may be used to endorse or promote products derived from this software without 
specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" 
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE 
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE 
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE 
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL 
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR 
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER 
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, 
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE 
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
--------------------------------------------------------------------------

LED Driver

  This driver is built for LEDs that are connected directly to the processor pin 
(i.e. the LED is ON when the output is "High"/"1" and OFF when the output is 
"Low" / "0")

Software API:

  LED(pin)
    - Provide pin that the LED is connected
    
    is_on()
      - Return a boolean value (i.e. True/False) if the LED is ON / OFF

    on()
      - Turn the LED on

    off()
      - Turn the LED off    

"""
import Adafruit_BBIO.GPIO as GPIO
import random
import time

# ------------------------------------------------------------------------
# Constants
# ------------------------------------------------------------------------

# None

# ------------------------------------------------------------------------
# Global variables
# ------------------------------------------------------------------------

# None

# ------------------------------------------------------------------------
# Functions / Classes
# ------------------------------------------------------------------------

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
        
    # End def



# ------------------------------------------------------------------------
# Constants
# ------------------------------------------------------------------------

# None

# ------------------------------------------------------------------------
# Global variables
# ------------------------------------------------------------------------

# None

# ------------------------------------------------------------------------
# Functions / Classes
# ------------------------------------------------------------------------

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
                print("Red Button")
                return 1 
            elif self.pin == "P1_34":
                print("Yellow Button")
                return 2
            elif self.pin == "P1_35":
                print("Green Button")
                return 3
            elif self.pin == "P1_33":
                print("Blue Button")
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
    
        
        
            

# End class



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

    
            if start_button.start_game() == 1:
                print("Game Started")
                time.sleep(1)
                                
                print("LED Test")
            
                pattern = []
                rounds = 5
                score = 0
                lost = False
                
                while lost == False:
                
                    button_pattern = []
                    num = random.randint(1, 4)
                    pattern.append(num)
                    print("Round")
                    score = score+1;
                    time.sleep(2)
                    for j in range(len(pattern)):
                        if pattern[j] == 1:
                            led = LED("P2_2")
                            led.on()
                            time.sleep(0.5)
                            led.off()
                        elif pattern[j] == 2:
                            led = LED("P2_4")
                            led.on()
                            time.sleep(0.5)
                            led.off()
                        elif pattern[j] == 3:
                            led = LED("P2_6")
                            led.on()
                            time.sleep(0.5)
                            led.off()
                        else:
                            led = LED("P2_8")
                            led.on()
                            time.sleep(0.5)
                            led.off()
                        
                    while next_button.next_round() != 1:
                        button_pattern.append(red_button.got_pressed())
                        button_pattern.append(yellow_button.got_pressed())
                        button_pattern.append(green_button.got_pressed())
                        button_pattern.append(blue_button.got_pressed())
                        button_pattern2 = [x for x in button_pattern if x is not None]
                    print(button_pattern2)
                    print(pattern)
                        
                    if button_pattern2 != pattern:
                        lost = True
                print("You Lost! Your score is: " + str(score-1))            
            
    except KeyboardInterrupt:
        pass


    
    

