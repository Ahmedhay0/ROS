#! /usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Pose2D
from std_msgs.msg import Int32,String
from traffic_manager import manage

class robot(Node):
    def __init__(self,name,x,y,theta,priorety):
        super().__init__(name)
        self.name=name
        self.danger=False
        self.pub_1 = self.create_publisher(Pose2D,"locations",10)
        self.pub_2 = self.create_publisher(Int32,"priorities",10)
        self.pub_3 = self.create_publisher(String,"state",10)

        self.sub_1 = self.create_subscription(Pose2D,"locations",self.get_data,10)
        self.sub_2 = self.create_subscription(Int32,"priorities",self.get_data,10)

        self.pose=Pose2D()
        self.pose.x=x
        self.pose.y=y
        self.pose.theta=theta
        self.state=String()
        self.prio=Int32()
        self.prio.data=priorety

        self.timer = self.create_timer(0.1, self.publish)
    def get_data(self,msg):
        self.state.data = manage(self,msg)

    def publish(self):

        self.pub_1.publish(self.pose)

        self.pub_2.publish(self.prio)

        self.pub_3.publish(self.state)

def main(args=None):
    rclpy.init(args=args)

    robots = [
        robot("robot_1", 0.0, 0.0, 0.0, 1),
        robot("robot_2", 8.0, 5.0, 0.0, 3),
        robot("robot_3", -1.5, 1.0, 0.0, 2)
    ]
    exe = rclpy.executors.MultiThreadedExecutor()
    
    for i in robots :
        exe.add_node(i)
    exe.spin()




    rclpy.shutdown()

main()