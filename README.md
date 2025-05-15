# ADVANCED WEAPON IDENTIFICATION VIA AI-POWERED DETECTION MODULE

## Project Description

This project implements an advanced weapon identification system using an AI-powered detection module.  It leverages the YOLO (You Only Look Once) object detection model to identify weapons in real-time from a webcam feed and transmits corresponding signals via serial communication.  The system is designed to detect Grenades, Knives, Pistols, Rifles, and Shotguns.

## Features and Functionality

*   **Real-time Weapon Detection:** Utilizes YOLOv8 to detect weapons in real-time from a webcam feed.
*   **Object Classification:**  Classifies detected objects into one of five categories: Grenade, Knife, Pistol, Rifle, or Shotgun.
*   **Confidence Level:**  Provides a confidence score for each detected object.
*   **Bounding Box Visualization:** Draws bounding boxes around detected objects with class labels and confidence scores.
*   **Serial Communication:**  Transmits a specific character via serial communication based on the detected weapon type. (A for Grenade, B for Knife, C for Pistol, D for Rifle, E for Shotgun).
*   **Coordinate Logging:** Prints the coordinates of the bounding boxes for each detected weapon.

## Technology Stack

*   **Python:**  Primary programming language.
*   **Ultralytics YOLO:**  Object detection framework.
*   **cvzone:**  Computer vision library for easy drawing and text display.
*   **cv2 (OpenCV):**  Computer vision library for image and video processing.
*   **PySerial:**  Library for serial communication.
*   **YOLOv8:** Object detection model architecture.

## Prerequisites

Before running the project, ensure you have the following installed:

*   **Python:**  (Version 3.6 or higher is recommended)
*   **Pip:** Python package installer
*   **Required Python Packages:**
    *   `ultralytics`
    *   `cvzone`
    *   `opencv-python`
    *   `pyserial`

    Install the required packages using pip:

    ```bash
    pip install ultralytics cvzone opencv-python pyserial
    ```

## Installation Instructions

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/sriman-dev/-ADVANCED-WEAPON-IDENTIFICATION-VIA-AI-POWERED-DETECTION-MODULE.git
    cd -ADVANCED-WEAPON-IDENTIFICATION-VIA-AI-POWERED-DETECTION-MODULE
    ```

2.  **Download the YOLOv8 model:**  While the `final.py` script uses a model at `C:/Users/Dell/Downloads/WEAPON/best.pt`, you will need to train your own model or download a pre-trained weapon detection model.  Place the model file (e.g., `best.pt`) in a suitable location and update the path in `final.py`.

3.  **Optional: Training a Custom Model (Based on model.py):**

    The `model.py` file contains code for training a YOLOv8 model.

    1.  Ensure you have a `data.yaml` file that defines the paths to your training and validation datasets, the number of classes, and the class names. The example path used is `C:/Users/SPIRO-PYTHON1/Desktop/bioooo_YOLO/data.yaml`.  **Modify this path to point to your own dataset configuration file.**

    2.  Run the `model.py` script to train the model:

        ```bash
        python model.py
        ```

        This will train a YOLOv8n model for 10 epochs.  You can adjust the number of epochs and other training parameters as needed.

## Usage Guide

1.  **Configure Serial Port:**

    *   In `final.py`, modify the serial port `'COM15'` to match the correct port for your Arduino or other serial device:

        ```python
        ser=serial.Serial('COM15',115200) #Change COM15 to the port connected to your device
        ```
    *   Ensure the baud rate (115200) matches the configuration of your serial device.

2.  **Run the `final.py` script:**

    ```bash
    python final.py
    ```

    This will start the webcam feed and begin detecting weapons.

3.  **View the output:**

    *   A window will display the webcam feed with bounding boxes around detected weapons, along with class labels and confidence scores.
    *   The script will print the detected class, confidence, and bounding box coordinates to the console.
    *   The script will send a character via serial communication corresponding to the detected weapon.

## API Documentation (Not Applicable)

This project does not expose a formal API.  However, you can interact with the system by:

*   **Modifying the `final.py` script:** Customize the weapon detection logic, serial communication behavior, and display settings.
*   **Using the serial output:**  Receive weapon detection events via the serial port and integrate them into other systems.

## Contributing Guidelines

Contributions are welcome!  To contribute:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Make your changes.
4.  Submit a pull request.

Please ensure your code adheres to the following guidelines:

*   Use clear and concise code.
*   Add comments to explain complex logic.
*   Test your changes thoroughly.

## License Information

No license is specified for this project. All rights are reserved by the author.

## Contact/Support Information

For questions, bug reports, or feature requests, please contact sriman-dev through GitHub.