import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
from ultralytics import YOLO

class YoloDetector(Node):
    def __init__(self):
        super().__init__('yolo_detector')
        
        # 1. Load the AI Model
        # We use 'yolov8n.pt' which is the "Nano" (fastest) version
        self.model = YOLO('yolov8n.pt') 
        
        # 2. Create a Subscriber
        # This listens to the camera topic
        self.subscription = self.create_subscription(
            Image,
            '/camera/image_raw',
            self.image_callback,
            10)
        
        self.br = CvBridge()
        self.get_logger().info("YOLO Detector Node Started! Waiting for camera...")

    def image_callback(self, data):
        # 3. Convert ROS Image -> OpenCV Image
        # We need to turn the robot message into a standard picture format
        current_frame = self.br.imgmsg_to_cv2(data, "bgr8")

        # 4. Run the AI
        results = self.model(current_frame, verbose=False)

        # 5. Draw the results
        # .plot() draws the boxes on the image for us
        annotated_frame = results[0].plot()

        # 6. Show the video on your screen
        cv2.imshow("Robot View", annotated_frame)
        cv2.waitKey(1)

def main(args=None):
    rclpy.init(args=args)
    node = YoloDetector()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
