import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile
from std_msgs.msg import String


class HelloworldPublisher(Node):
    """
    - publish_helloworld_msg : member callback f (member f, lambda f, local f 중 member f)
    """

    def __init__(self):
        super().__init__('helloworld_publisher')
        qos_profile = QoSProfile(depth=10)  # Data Buffer of 10 Size
        self.helloworld_publisher = self.create_publisher(String, 'helloworld', qos_profile)
        self.timer = self.create_timer(1, self.publish_helloworld_msg)  # Execute callback function 1 time per 1 second
        self.count = 0  # callback function counter

    def publish_helloworld_msg(self):
        msg = String()  # String Message interface
        msg.data = 'Hello World: {0}'.format(self.count)
        self.helloworld_publisher.publish(msg)
        self.get_logger().info('Published message: {0}'.format(msg.data))  # debug, info, warning, error, fatal
        self.count += 1


def main(args=None):
    rclpy.init(args=args)
    node = HelloworldPublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('Keyboard Interrupt (SIGINT)')
    finally:
        node.destory_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
