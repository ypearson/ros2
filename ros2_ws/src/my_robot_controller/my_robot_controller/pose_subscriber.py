#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose

class PoseSubscriberNode(Node):
    def __init__(self):
        super().__init__("pose_subscriber")
        self.pose_subscriber_ = self.create_subscription(Pose,'/turtle1/pose', self.pose_callback, 10)
    def pose_callback(self, msg: Pose):
        # Process message, eg do something with the msg
        self.get_logger().info(f'x={str(msg.x)},y={str(msg.y)}')


def main(args=None):
    rclpy.init(args=args)

    node = PoseSubscriberNode()

    rclpy.spin(node)

    rclpy.shutdown()
