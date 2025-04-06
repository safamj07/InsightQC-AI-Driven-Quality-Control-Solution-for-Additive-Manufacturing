import time
import pandas as pd
from ultralytics import YOLO

# Load the YOLO model
model = YOLO('IQ_best.pt')

# Define CSV file path
output_csv = "C:/Users/Safa/OneDrive/Desktop/runs/detect/yolo_predictions.csv"

# Function to run YOLO model and store results
def record_predictions():
    results = model.predict(source=0, imgsz=640, conf=0.6, save=True, show=True)
    
    # Extract results
    data = []
    for result in results:
        for box in result.boxes.data:
            x1, y1, x2, y2, conf, cls = box.tolist()
            data.append([x1, y1, x2, y2, conf, result.names[int(cls)]])
    
    # Convert to DataFrame
    df = pd.DataFrame(data, columns=['x1', 'y1', 'x2', 'y2', 'confidence', 'class'])
    
    # Append to CSV file
    df.to_csv(output_csv, mode='a', header=not pd.io.common.file_exists(output_csv), index=False)
    print(f"Predictions saved at {time.strftime('%Y-%m-%d %H:%M:%S')}")

# Run model every 5 minutes
while True:
    record_predictions()
    time.sleep(300)  # Sleep for 5 minutes (300 seconds)
