import os
import math
import arcade
import rclpy 
import numpy as np
from enum import Enum
from threading import Thread
from rclpy.node import Node
from .lib.crane_sim import CraneSimulation
from std_msgs.msg import Float64, Int64
from geometry_msgs.msg import Point

class MotorX_Controller(Node):
    def __init__(self):
        super().__init__("motorx_controller")
        self.subscribe = self.create_subscription(Float64, '/controller_setpoint', 10)
        self.publish = self.create_publisher(Int64,'/motor_x', self.callback_motorx, 10)
        self.kp = 0.2

    def callback_motorx(self, msg):
        position = msg.data
        self.error = self.setpoint - position
        control = (self.kp * self.error)

        self.last_error = self.error

        velocity = self.get_motor_velocity(control)
        velocity_msg = Int64
        velocity_msg.data = velocity

        self.subscribe.subscribe(velocity_msg)

    def get_motor_velocity(self, control):
        velocity = control * 0.2
        return velocity

def main(args=None):
    rclpy.init(args=args)
    MotorXController = MotorX_Controller()
    rclpy.spin(MotorXController)
    MotorXController.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()    

