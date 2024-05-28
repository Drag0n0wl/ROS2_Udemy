#include "rclcpp/rclcpp.hpp"

int main(int argc, char **argv)
{
    // Initialize ROS2 communication
    rclcpp::init(argc, argv);
    auto node = std::make_shared<rclcpp::Node>("cpp_test");
    RCLCPP_INFO(node->get_logger(), "Hello Cpp Node");
    rclcpp::shutdown();
    return 0;
}
