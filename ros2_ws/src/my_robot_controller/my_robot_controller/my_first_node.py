#!/usr/bin/env python3

# ROS Client Library
import rclpy
from rclpy.node import Node

class MyNode(Node):
    def __init__(self):
        # ros2 run  my_robot_controller test_node
        super().__init__('first_node') # name seen on rqt_graph
        self.get_logger().info('ROS2')
        self.create_timer(1.0, self.timer_callback)
        self.counter = 0

    def timer_callback(self):
        self.get_logger().info('callback ' + str(self.counter) )
        self.counter += 1

def main(args=None):
    rclpy.init(args=args)
    node = MyNode()

    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()