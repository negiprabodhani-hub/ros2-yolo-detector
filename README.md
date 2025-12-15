# AI Object Detection Node for ROS 2 Jazzy

## Project Overview
This project implements a real-time object detection system using **ROS 2 Jazzy** and **YOLOv8** (You Only Look Once). It is designed to identify objects from a robot's camera feed and publish detection data for autonomous decision-making.

**Key Feature: Headless Optimization**
The simulation and detection pipeline are optimized to run in **Headless Mode** (no GUI). This allows the computer vision system to run efficiently on low-resource hardware, CI/CD pipelines, or edge devices without dedicated GPUs.

## Tech Stack
* **Framework:** ROS 2 Jazzy Jalisco
* **Language:** Python 3.10
* **Computer Vision:** Ultralytics YOLOv8, OpenCV
* **Simulation:** Gazebo Harmonic
* **OS:** Ubuntu 24.04 LTS

## Architecture
1.  **Simulation:** A Gazebo world publishes video data to `/camera/image_raw`.
2.  **Bridge:** `ros_gz_bridge` converts Gazebo images to ROS 2 topics.
3.  **Detector Node:** A custom Python node subscribes to the image topic, processes frames through the YOLOv8 model, and draws bounding boxes around detected objects.

## Challenges Solved
* **Dependency Management:** Resolved critical version conflicts between ROS 2 NumPy requirements and system-level Python packages in Ubuntu 24.04.
* **Resource Constraints:** Configured the simulation for software rendering (`LIBGL_ALWAYS_SOFTWARE=1`) to bypass hardware acceleration limits in virtualized environments.
