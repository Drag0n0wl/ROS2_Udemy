#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

from example_interfaces.msg import String


class RobotNewsStationNode(Node):  # MODIFY NAME
    def __init__(self):
        super().__init__("robot_news_station")  # MODIFY NAME

        self.robot_name = "C3PO"
        self.publisher = self.create_publisher(String, "robot_news", 10)
        self.timer_ = self.create_timer(0.5, self.publish_news)
        self.get_logger().info("Robot News Station has been started")

    def publish_news(self):
        msg = String()
        msg.data = "Hi, this is " + \
            str(self.robot_name) + " from the robot news station."
        self.publisher.publish(msg)


def main(args=None):
    # Initialize ROS2 communication
    rclpy.init(args=args)
    # Create the node
    node = RobotNewsStationNode()  # MODIFY NAME
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
