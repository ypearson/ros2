#!/usr/bin/env python3

# ROS Client Library
import rclpy
from rclpy.node import Node

class MyNode(Node):
    def __init__(self):
        super().__init__('first_node') # name seen on rqt_graph
        self.get_logger().info('ROS2')
        self.create_timer(1.0, self.timer_callback)
        self.counter = 0

    def timer_callback(self):
        self.get_logger().info('callback ' + str(self.counter) )
        self.counter += 1

# https://docs.ros2.org/foxy/api/rclpy/api/init_shutdown.html

def main(args=None):
    # Initialize ROS communications for a given context.
    rclpy.init(args=args)

    # Create node
    node = MyNode()

    # Execute work and block until the context associated with the executor is shutdown.
    rclpy.spin(node)

    # Shutdown a previously initialized context
    # This will also shutdown the global executor
    rclpy.shutdown()

if __name__ == '__main__':
    main()