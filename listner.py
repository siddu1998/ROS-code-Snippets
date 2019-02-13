import rospy
from std_msgs import String


def callback(data):
    rospy.loginfo(rospy.get_caller_id() + " I heard this :" + data.data)

def listener():
    rospy.init_node('listener',anonymous=True)
    rospy.Subscriber('chatter',String,callback)
    rospy.spin()

if __name__=='__main__':
    listener()