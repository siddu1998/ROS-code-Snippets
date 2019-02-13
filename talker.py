import rospy
from std_msgs import String

def talket():
    pub = rospy.Publisher('chatter',String,queue_size=10)
    rospy.init_node('talker',anonymous=True)
    rate=rospy.Rate(1)

    while not rospy.is_shutdown():
        hello_str="Hello world {}".format(rospy.get_time())
        rospy.loginfo(hello_str)
        pub.publisher(hello_str)
        rate.sleep()

    if __name__ == '__main__':
        try:
            talker()
        except rospy.ROSInterruptExpectation:
            pass
        