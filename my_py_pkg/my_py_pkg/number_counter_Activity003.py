#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

from example_interfaces.msg import Int64
from example_interfaces.srv import SetBool


class NumberCounterNode(Node):  # MODIFY NAME
    def __init__(self):
        super().__init__("number_counter")  # MODIFY NAME
        self.counter_ = 0
        # create publisher
        self.number_counter_publisher_ = self.create_publisher(
            Int64, "number_count", 10)
        self.number_subscriber_ = self.create_subscription(
            Int64, "number", self.callback_number, 10)
        self.get_logger().info("Number counter has been started.")

        super().__init__("reset_number_count")  # MODIFY NAME
        self.server_ = self.create_service(
            SetBool, "reset_counter", self.callback_reset_number_count)
        self.get_logger().info("Reset number counter server has been started.")

        def callback_reset_number_count(self, request, response):
            if request.data is response.success:
                self.counter_ = 0
            self.get_logger().info(str(response.success))

    def callback_number(self, msg):
        self.counter_ += msg.data
        new_msg = Int64()
        new_msg.data = self.counter_
        self.number_counter_publisher_.publish(new_msg)


def main(args=None):
    rclpy.init(args=args)
    node = NumberCounterNode()  # MODIFY NAME
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
