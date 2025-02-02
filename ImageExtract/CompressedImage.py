                                                            extract.py                                                                         import rclpy
import cv2
import os
import numpy as np


from rclpy.node import Node
from sensor_msgs.msg import CompressedImage
from cv_bridge import CvBridge


class ImageExtractor(Node):
   def __init__(self):
       super().__init__('image_extractor')
       self.bridge = CvBridge()
       self.subs = []
       self.topic = '/image_color/compressed'
       os.makedirs('extracted', exist_ok=True)
       print("MADE DIR")
       sub = self.create_subscription(CompressedImage, self.topic, self.image_callback, 10)
       print("CREATED SUBSCRIPTION")
       self.subs.append(sub)
       self.image_counters = 0
       print("init END")


   def image_callback(self, msg):
       print("CALLBACK START")
       np_arr = np.frombuffer(msg.data, np.uint8)
       cv_image = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
       folder_name = 'extracted'
       filename = f"{folder_name}/frame_{self.image_counters}.jpg"


       # cv_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding="rgb8")
       cv2.imwrite(filename, cv_image)


       self.get_logger().info(f"Saved {filename}")
       self.image_counters += 1
       print("CALLBACK END")


def main(args=None):
   rclpy.init(args=args)
   node = ImageExtractor()
   rclpy.spin(node)
   print("Node is spinning")
   node.destroy_node()
   rclpy.shutdown()


if __name__ == '__main__':
   main()
