import logging
from flask import Flask
from flask_restful import Resource, reqparse, inputs
from gpiozero import PWMLED, Device
from gpiozero.pins.pigpio import PiGPIOFactory

# GPIO setup
Device.pin_factory = PiGPIOFactory()

# RGB LED pins
pins = {
    "r": PWMLED(16),
    "g": PWMLED(20),
    "b": PWMLED(21),
}


# Resource class
class LED(Resource):
    def __init__(self):
        self.args_parser = reqparse.RequestParser()
        self.args_parser.add_argument(name='r', type=inputs.int_range(0, 255))
        self.args_parser.add_argument(name='g', type=inputs.int_range(0, 255))
        self.args_parser.add_argument(name='b', type=inputs.int_range(0, 255))

    def get(self):
        return {color: int(pin['value']*255) for color, pin in pins.items()}

    def post(self):
        args = self.args_parser.parse_args()
        if args['r'] != None:
            pins['r'].value = args['r'] / 255.0
        if args['g'] != None:
            pins['g'].value = args['g'] / 255.0
        if args['b'] != None:
            pins['b'].value = args['b'] / 255.0
        logging.info(f'Color changed to {self.get()}')
        return self.get()
