#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

from example_interfaces.msg import Int64


class NumberPublisherNode(Node):  # MODIFY NAME
    def __init__(self):
        super().__init__("number_publisher")  # MODIFY NAME

        self.publisher = self.create_publisher(Int64, "number", 10)
        self.counter_ = 0
        self.timer_ = self.create_timer(0.5, self.publish_news)
        self.get_logger().info("Pub publisher has been started")

    def publish_news(self):
        msg = Int64()
        self.counter_ += 1
        msg.data = self.counter
        self.publisher.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = NumberPublisherNode()  # MODIFY NAME
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
