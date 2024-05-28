#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

class MyNode(Node):

    def __init__(self):
        super().__init__("py_test")
        self.counter_ = 0
        self.get_logger().info("Hello ROS2")
        self.create_timer(0.5, self.timer_callback)
    
    def timer_callback(self):
        self.counter_ += 1
        self.get_logger().info("Hello " + str(self.counter_))

def main(args=None):
    # initilize ROS2 comm.
    rclpy.init(args=args)
    # create your node
    node = MyNode()
    # print a message
    node.get_logger().info("Hello ROS2")
    # spin pauses the program and allow your node to be alive
    rclpy.spin(node)
    # shutdown ROS2 comm.
    rclpy.shutdown()

if __name__ == "__main__":
    main()