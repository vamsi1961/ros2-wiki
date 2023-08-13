#include "rclcpp/rclcpp.hpp"


class MyNode: public rclcpp::Node 
{

public:
    MyNode() : Node("cpp_class_test"), counter_(0)
    // along with initializing node, counter_ is also initialized
    {
        RCLCPP_INFO(this->get_logger() , "Hello Cpp Class Node");
        // constructor
        timer_ = this ->create_wall_timer(std::chrono::seconds(1),
        std::bind(&MyNode::timerCallback, this));

        // to create a timer there are 2 arguments duration and call function
        // function to bind node to this.
            

    }


private:


    // timer call back function
    void timerCallback()
    {
        counter_++;
        RCLCPP_INFO(this->get_logger() , "Hello %d" , counter_);
    }

    rclcpp::TimerBase::SharedPtr timer_;
    // declaring a shared pointer
    int counter_;
    // declaring counter

};

int main( int argc , char **argv)
{
    rclcpp::init(argc,argv);

    auto node =std::make_shared<MyNode>();
    // auto node is a shared pointer


    rclcpp::spin(node);
    // keeps function alive


    rclcpp::shutdown();
    return 0;
}