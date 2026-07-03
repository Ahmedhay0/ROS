#! /usr/bin/env python3
from math import hypot
import sys
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Pose2D
from std_msgs.msg import Int32, String
from fleet_emulation.traffic_manager import manage

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
    if len(sys.argv) < 6:
        raise ValueError('The input format is:<name>,<priority>,<x>,<y>,<theta>')

    name = sys.argv[1]
    priority = int(sys.argv[2])
    x = float(sys.argv[3])
    y = float(sys.argv[4])
    theta = float(sys.argv[5])

    r = robot(name, priority, x, y, theta)

    rclpy.spin(r)
    rclpy.shutdown()
 
 
if __name__ == "__main__":
    main()

