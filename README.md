# InsightQC-AI-Driven-Quality-Control-Solution-for-Additive-Manufacturing
InsightQC is an innovative quality control solution designed for the additive manufacturing industry, focusing on defect detection and maintenance scheduling using machine learning and computer vision technologies. The platform helps detect surface defects, predict maintenance needs, and streamline the quality control process.

Key Features
Defect Detection: Uses YOLOv8, a state-of-the-art computer vision algorithm, to detect defects on product surfaces with high accuracy.
Impact Damage Detection: Integrates Pulse-Echo Ultrasonic testing to detect barely visible impact damage that may affect the structural integrity of 3D-printed materials.
Dynamic Maintenance Scheduling: An RPA bot analyzes defect frequencies and generates dynamic maintenance schedules, alerting stakeholders and maintenance teams about the status of the machinery and products.
Data-Driven Insights: Aggregates data from visual and ultrasonic inspections, creating quality control charts and detailed maintenance reports.
Cloud-Based Model: The initial version is cloud-based, ensuring easy access to model updates and seamless integration into existing production workflows.

Technologies Used
YOLOv8: A cutting-edge computer vision algorithm for defect detection on the product surfaces.
Pulse-Echo Ultrasonic Testing: For detecting internal or barely visible defects.
Roboflow: Used for managing the dataset and training the computer vision model.
RPA (Robotic Process Automation): For automating defect frequency tracking, maintenance scheduling, and stakeholder notifications.
Python: The core programming language for implementing the machine learning and computer vision models.
Cloud Computing: For hosting and accessing the model remotely, ensuring scalability and accessibility.
