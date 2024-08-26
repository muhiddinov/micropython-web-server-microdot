from machine import PWM, Pin

class LEDModule:
    """This will represent our LED"""
    
    def __init__(self, pinNumber):
        self.pinNumber = pinNumber
        self.led_pin = Pin(self.pinNumber, Pin.OUT)
        self.pwm = PWM(Pin(2, Pin.OUT), 100, duty_u16=512)
        
    def get_value(self):
        return self.led_pin.value()
    
    def toggle(self):
        self.led_pin.value(not self.get_value())
    
    def set_pwm(self, duty):
        self.pwm.duty_u16(duty)