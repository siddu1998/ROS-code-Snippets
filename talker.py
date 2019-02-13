import rospy
from std_msgs import String
from geometry_msgs.msg import Twist
def talker():
    pub = rospy.Publisher('chatter',String,queue_size=10)
    rospy.init_node('talker',anonymous=True)
    rate=rospy.Rate(1)
    i=0
    while not rospy.is_shutdown():
        hello_str="Hello world {}".format(rospy.get_time())
        rospy.loginfo(hello_str)
        pub.publisher(hello_str)
        rate.sleep()
        i=i+1

    if __name__ == '__main__':
        try:
            talker()
        except rospy.ROSInterruptExpectation:
            pass
        