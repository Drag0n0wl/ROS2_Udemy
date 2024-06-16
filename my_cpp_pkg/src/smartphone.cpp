#include "rclcpp/rclcpp.hpp"
#include "example_interfaces/msg/string.hpp"

class SmartphoneNode : public rclcpp::Node // MODIFY NAME
{
public:
    SmartphoneNode() : Node("smartphone") // MODIFY NAME
    {
        // initialize subscriber
        subscriber_ = this->create_subscription<example_interfaces::msg::String>("robot_news", 10, std::bind(&SmartphoneNode::callbackRobotNews, this, std::placeholders::_1));
        RCLCPP_INFO(this->get_logger(), "Smartphone has been started. ");
    }

private:
    // subscriber will be created with the callback function
    void callbackRobotNews(const example_interfaces::msg::String::SharedPtr msg)
    {
        // print the message as RCLCPP INFO and print a string as shared pointer
        RCLCPP_INFO(this->get_logger(), "%s", msg->data.c_str());
    }

    // declare subscriber
    rclcpp::Subscription<example_interfaces::msg::String>::SharedPtr subscriber_;
};

int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);
    auto node = std::make_shared<SmartphoneNode>(); // MODIFY NAME
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}