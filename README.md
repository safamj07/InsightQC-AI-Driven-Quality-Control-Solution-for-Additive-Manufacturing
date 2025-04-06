# InsightQC - Real-time Defect Analysis and Maintenance Prediction

InsightQC is an AI-powered visual inspection and quality control system designed to detect surface defects in 3D-printed parts. By leveraging state-of-the-art object detection (YOLOv8) and Robotic Process Automation (RPA) tools like UiPath, InsightQC automates the end-to-end defect tracking and maintenance reporting process, significantly improving production efficiency in additive manufacturing.

---

## 🎯 Key Highlights

- 🧠 **YOLOv8** for accurate real-time defect detection
- 📊 **Automated Excel Reports** to visualize defect frequency
- 🤖 **RPA Integration** with UiPath for dynamic maintenance scheduling
- 📂 **Roboflow** integration for dataset management and training
- 💡 Boosts quality assurance and reduces production downtime

---

## ⚙️ Project Workflow

1. **Input**: Capture or upload 3D-printed product images
2. **Detection**: YOLOv8 detects and classifies visible surface defects
3. **Data Logging**: Defect data is stored in an Excel file using Pandas
4. **Visualization**: Charts are generated to analyze defect trends
5. **Automation**: UiPath bot reads data and schedules maintenance based on frequency

![Flowchart - Frame 1 (3)](https://github.com/user-attachments/assets/3936b0d5-e45a-4e73-828b-666916c9b60e)

---

## 🧱 Tech Stack

| Layer           | Tools/Technologies           |
|----------------|------------------------------|
| Object Detection | YOLOv8 (Ultralytics), Roboflow |
| Data Processing | Python, Pandas, NumPy         |
| Visualization   | Matplotlib                    |
| Automation      | UiPath                        |
| IDEs/Tools      | VS Code                       |


