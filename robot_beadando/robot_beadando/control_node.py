import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
from std_msgs.msg import String


class ControlNode(Node):

    def __init__(self):
        super().__init__('control_node')

        self.subscription = self.create_subscription(
            Float32,
            '/distance',
            self.distance_callback,
            10
        )

        self.publisher = self.create_publisher(
            String,
            '/robot_command',
            10
        )

    def distance_callback(self, msg):
        distance = msg.data

        if distance > 2.0:
            command = 'MEHET'
        else:
            command = 'ALLJ'

        output = String()
        output.data = command

        self.publisher.publish(output)

        self.get_logger().info(
            f'Distance: {distance:.1f} m -> {command}'
        )


def main(args=None):
    rclpy.init(args=args)

    node = ControlNode()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
