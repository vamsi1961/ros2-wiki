#include "rclcpp/rclcpp.hpp"


int main( int argc , char **argv)
{
    rclcpp::init(argc,argv);

    auto node =std::make_shared<rclcpp::Node>("cpp_test");
    // auto node is a shared pointer

    // logger function
    RCLCPP_INFO(node -> get_logger() , "Hello cpp node");

    rclcpp::spin(node);
    // keeps function alive


    rclcpp::shutdown();
    return 0;
}