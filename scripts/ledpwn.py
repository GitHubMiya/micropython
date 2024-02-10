from machine import Pin, PWM

pin = 0 #number for pin number

pwm_pin = 0 

pwm_pin = PWM(Pin(pin)) #frequency is cycles per send (Hertz, Hz)

pwm_pin.freq(200)#hz

percent = 0

pwm_pin.duty_u16(percent*655)