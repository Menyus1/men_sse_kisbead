import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32


class SensorNode(Node):

    def __init__(self):
        super().__init__('sensor_node')

        self.publisher = self.create_publisher(
            Float32,
            '/distance',
            10
        )

        self.timer = self.create_timer(
            1.0,
            self.publish_distance
        )

        self.distance = 5.0

    def publish_distance(self):
        msg = Float32()
        msg.data = self.distance

        self.publisher.publish(msg)

        self.get_logger().info(
            f'Distance: {self.distance:.1f} m'
        )

        self.distance -= 0.5

        if self.distance < 0.5:
            self.distance = 5.0


def main(args=None):
    rclpy.init(args=args)

    node = SensorNode()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
