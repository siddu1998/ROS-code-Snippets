import rospy
from geometry_msgs.msg import Twist

def move():
    speed_publisher = rospy.Publisher('turtle1/cmd_vel',Twist,queue_size=10)
    rospy.init_node('move',anonymous=True)
    rate=rospy.Rate(1)

    while not rospy.is_shutdown():
        twist=Twist()
        twist.linear.x=1.0




    if __name__ == '__main__':
        try:
            move()
        except rospy.ROSInterruptExpectation:
            pass
        