#include "rclcpp/rclcpp.hpp"

class MyNode : public rclcpp::Node
{
public:
    // write constructor, initialize the node and counter
    MyNode() : Node("cpp_test"), counter_(0)
    {
        RCLCPP_INFO(this->get_logger(), "Hello Cpp Node");

        // initilize the timer_
        timer_ = this->create_wall_timer(std::chrono::seconds(1),
                                         std::bind(&MyNode::timerCallback, this));
    }

private:
    void timerCallback()
    {
        counter_++;
        RCLCPP_INFO(this->get_logger(), "Hello %d", counter_);
    }

    // declare the timer
    rclcpp::TimerBase::SharedPtr timer_;
    // declare the counter
    int counter_;
};

int main(int argc, char **argv)
{
    // Initialize ROS2 communication
    rclcpp::init(argc, argv);
    auto node = std::make_shared<MyNode>();
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}
