#include "rclcpp/rclcpp.hpp"
#include "example_interfaces/msg/string.hpp"


class SmartPhoneNode : public rclcpp::Node // Modify Name
{


public:
    SmartPhoneNode(): Node("smart_phone") // Modify Name
    {
        subscriber_ = this->create_subscription<example_interfaces::msg::String>(
            "robot_news",
            10,
            std::bind(&SmartPhoneNode::callbackRobotNews, this , std::placeholders::_1)
            // for callback function there is a parameter so extra argument is required
        );

        RCLCPP_INFO(this-> get_logger(),"%s","Subscriber started");

    }

private:

    void callbackRobotNews(const example_interfaces::msg::String::SharedPtr msg)
    {
        RCLCPP_INFO(this -> get_logger() , "%s" , msg->data.c_str());
    }
    rclcpp::Subscription<example_interfaces::msg::String>::SharedPtr subscriber_;



};

int main(int argc , char **argv)
{
    rclcpp::init(argc, argv);
    auto node = std::make_shared<SmartPhoneNode>();  // Modify Name
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}