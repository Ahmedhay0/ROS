#! /usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Pose2D
from std_msgs.msg import Int32,String
from traffic_manager import manage

class robot(Node):
    def __init__(self, name, priorety, x, y, theta):
        super().__init__(name)
        self.name = name
        self.danger = False
        self.state = String()
        self.state_pub = self.create_publisher(String, "States", 10)
        self.prio_pub = self.create_publisher(Int32, "Priorities", 10)
        self.prio = Int32()
        self.prio.data = priorety
        self.pose_pub = self.create_publisher(Pose2D, "Positions", 10)
        self.pose = Pose2D()
        self.pose.x = x
        self.pose.y = y
        self.pose.theta = theta
        self.pub_prio = self.create_timer(0.1, self.publish)
        self.sub_pose = self.create_subscription(Pose2D, "Positions", self.get_state, 10)
        self.sub_prio = self.create_subscription(Int32, "Priorities", self.get_state, 10)

    def publish(self):
        self.prio_pub.publish(self.prio)
        self.pose_pub.publish(self.pose)
        self.state_pub.publish(self.state)

    def get_state(self, msg):
        self.state.data = manage(self, msg)

def main(args=None):
    rclpy.init(args=args)

    robots = [
        robot("robot_1", 5, 4.6, 2.0, 0.0),
        robot("robot_2", 6, 7.3, 0.0, 3.1),
        robot("robot_3", 20, 10.3, 5.0, 1.5)
    ]
    exe = rclpy.executors.MultiThreadedExecutor()
    
    for r in robots :
        exe.add_node(r)
    exe.spin()




    rclpy.shutdown()

main()