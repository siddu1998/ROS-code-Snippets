import rospy
import sys
import cv2
import cv2.cv as cv

from sensor_msgs.msg import Image,CameraInfo
from cv_bridge import CvBridge,CvBridgeError
import numpy as np


class cvBridgeDemo():
	def __init__(self):
		self.node_name="cv_bridge_demo"
		rospy.init_node(self.node_name)

		rospy.on_shutdown(self.cleanup)
		self.cv_window_name=self.node_name
		cv.NamedWindow(self.cv_window_name,cv.CV_WINDOW_NORMAL)
		cv.MoveWindow(self.cv_window_name,25,75)

		cv.NamedWindow("Depth Image",cv.CV_WINDOW_NORMAL)
		cv.MoveWindow("depth Image",25,350)

		self.bridge = CvBridge()

		self.image_sub=
		rospy.Subscriber("/camera/rgb/image_color",Image,self.image_callback)
		self.depth_sub=
		rospy.Subscriber("/camera/depth/image_raw",Image,self.depth_callback)
		rospy.loginfo("Waiting for image topic...")
	def image_callback(self, ros_image):
		try:
			frame = self.bridge.imgmsg_to_cv(ros_image, "bgr8")
		except CvBridgeError, e:
			print e
		frame = np.array(frame, dtype=np.uint8)
		display_image = self.process_image(frame)
		cv2.imshow(self.node_name, display_image)
		self.keystroke = cv.WaitKey(5)
		if 32 <= self.keystroke and self.keystroke < 128:
			cc = chr(self.keystroke).lower()
		if cc == 'q':
			rospy.signal_shutdown("User hit q key to quit.")
	def depth_callback(self, ros_image):
		try:
			depth_image = self.bridge.imgmsg_to_cv(ros_image,"32FC1")
		except CvBridgeError, e: print e
		depth_array = np.array(depth_image, dtype=np.float32)
		cv2.normalize(depth_array,depth_array, 0, 1, cv2.NORM_MINMAX)
		depth_display_image =self.process_depth_image(depth_array)
		cv2.imshow("Depth Image", depth_display_image)
	def process_image(self, frame):
		grey = cv2.cvtColor(frame, cv.CV_BGR2GRAY)
		grey = cv2.blur(grey, (7, 7))
		edges = cv2.Canny(grey, 15.0, 30.0)
		return edges
	def process_depth_image(self, frame):
		return frame
	def cleanup(self):
		print "Shutting down vision node."
		cv2.destroyAllWindows()
	def main(args):
		try:
			cvBridgeDemo()
			rospy.spin()
		except KeyboardInterrupt: print "Shutting down vision node."
		cv.DestroyAllWindows()

if __name__ == '__main__':
main(sys.argv)
