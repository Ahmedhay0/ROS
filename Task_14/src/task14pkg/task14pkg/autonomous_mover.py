import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist




class mover(Node):
    def __init__(self):
        super().__init__("Mover")
        self.vel_pub = self.create_publisher(Twist, "cmd_vel", 10)
        self.counter = -3
        self.speeds= {0:[1.2,0.0,0.0,0.0,0.0,0.45],1:[1.2,0.0,0.0,0.0,0.0,-0.6],2:[1.2,0.0,0.0,0.0,0.0,-0.8],3:[1.2,0.0,0.0,0.0,0.0,-1.2],4:[0.0,0.0,0.0,0.0,0.0,0.0]}
        self.timer = self.create_timer(1.8, self.timer_callback)
    def timer_callback(self):
        if self.counter<0:
            self.counter+=1
            return
        elif self.counter>4:
            return
        msg=Twist()
        cur_spd= self.speeds[self.counter]
        self.counter+=1
        msg.linear.x = cur_spd[0]
        msg.linear.y = cur_spd[1]
        msg.linear.z = cur_spd[2]
        msg.angular.x = cur_spd[3]
        msg.angular.y = cur_spd[4]
        msg.angular.z = cur_spd[5]
        self.vel_pub.publish(msg)
def main(args=None):
    rclpy.init(args=args)
    n = mover()
    rclpy.spin(n)
    rclpy.shutdown()

if __name__ == "__main__":
    main()