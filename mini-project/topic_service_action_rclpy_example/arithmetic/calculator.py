import rclpy
from rclpy.node import Node

from rclpy.qos import QoSProfile
from rclpy.qos import QoSReliabilityPolicy
from rclpy.qos import QoSHistoryPolicy
from rclpy.qos import QoSDurabilityPolicy


class Calculator(Node):

    def __init__(self):
        super().__init__('calculator')
        self.argument_a = 0.0
        self.argument_b = 0.0
        self.callback_group = ReeentrantCallbackGroup()

        """
        Service server()
        Action server()
        """

        QOS_RKL10V = QoSProfile(
            reliability=QoSReliabilityPolicy.RELIABLE,
            history=QoSHistoryPolicy.KEEP_LAST,
            depth=qos_depth,
            durability=QoSDurabilityPolicy.VOLATILE
        )

        self.arithmetic_argument_subscriber = self.create_subscription(
            ArithmeticArgument,
            'arithmentic_argument',
            self.get_arithmetic_argument,
            QOS_RKL10V,
            callback_group=self.callback_group
        )

    def get_arithmetic_argument(self, msg):
        self.argument_a = msg.argument_a
        self.argument_b = msg.argument_b
        self.get_logger().info('Timestamp of the message : {0}'.format(msg.stamp))
        self.get_logger().info('Subscribed argument a : {0}'.format(self.argument_a))
        self.get_logger().info('Subscribed argument b : {0}'.format(self.argument_b))
