#include "rclcpp/rclcpp.hpp"
#include "example_interfaces/srv/add_two_ints.hpp"


class AddTwoIntsClientNode : public rclcpp::Node 
{


public:
    AddTwoIntsClientNode(): Node("add_two_ints_client") 
    {
        
        // thread1_ = std::thread(std::bind(&AddTwoIntsClientNode::callAddTwoIntsService,this,1,4 ));

        threads_.push_back(std::thread(std::bind(&AddTwoIntsClientNode::callAddTwoIntsService,this,1,4 )));
        threads_.push_back(std::thread(std::bind(&AddTwoIntsClientNode::callAddTwoIntsService,this,9,4 )));



    }


    void callAddTwoIntsService(int a , int b)
    {
        auto client = this->create_client<example_interfaces::srv::AddTwoInts>("add_two_ints");
        
        while (!client->wait_for_service(std::chrono::seconds(1)))
        {
            RCLCPP_WARN(this->get_logger(), " WAiting for server to be up");
        }
        
        auto request = std:: make_shared<example_interfaces::srv::AddTwoInts::Request>();
        
        request->a = a;
        request->b = b;
        
        auto future = client->async_send_request(request);

        
        try
        {
            auto response = future.get();
            RCLCPP_INFO(this->get_logger(), " %d + %d = %d " , a , b, (int)response->sum);
        }
        catch(const std::exception& e)
        {
            RCLCPP_ERROR(this->get_logger() , "Service call failed");
        }
        
        // future.get() will wait until we have a response for the future
        // It can also throw exception if there is any error

    }

private:

    // std::thread thread1_;
    std::vector<std::thread> threads_;
    

};

int main(int argc , char **argv)
{
    rclcpp::init(argc, argv);
    auto node = std::make_shared<AddTwoIntsClientNode>(); 
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}







// we start the node, it creates client, starts service, creates request, 
// we wait for response, future will get. This will br=lock the thread here and that means that the function will not exist











