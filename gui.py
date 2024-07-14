import tkinter as tk
from tkinter import ttk
from joblib import load
import numpy as np

# Load the saved models
# Dummy models to make the code runnable
dt_model = rf_model = et_model = xg_model = stk_model = None

# Function to preprocess the input
def preprocess_input(attribute_values):
    processed_values = np.array([attribute_values], dtype=float)
    processed_values = processed_values[:, :4]  # Keep only the first 4 features
    return processed_values

# Function to perform prediction with feedback
def perform_prediction():
    try:
        attribute_values = [float(entry_list[i].get()) for i in range(len(entry_list))]
        processed_values = preprocess_input(attribute_values)
        prediction = 0  # Dummy prediction to make the code runnable
        attack_types = {0: 'BENIGN', 1: 'BruteForce', 2: 'Bot', 3: 'DoS', 4: 'Infiltration', 5: 'WebAttack', 6: 'PortScan'}
        predicted_attack = attack_types[prediction]
        result_label.config(text=f"Predicted Attack Type: {predicted_attack}", fg="green", font=("Arial", 12, "bold"))
    except ValueError:
        result_label.config(text="Invalid input! Please enter numerical values.", fg="red", font=("Arial", 12, "bold"))
    except Exception as e:
        result_label.config(text=f"Prediction failed! Error: {str(e)}", fg="red", font=("Arial", 12, "bold"))

def update_animation(count, stage):
    if count > 0:
        stages = ["Predicting", "Predicting.", "Predicting..", "Predicting..."]
        result_label.config(text=stages[stage], fg="blue", font=("Arial", 12, "bold"))
        root.after(500, update_animation, count - 1, (stage + 1) % len(stages))
    else:
        perform_prediction()

def predict_attack():
    result_label.config(text="Connecting to machine learning models...", fg="blue", font=("Arial", 12, "bold"))
    update_animation(10, 0)  # 10 half-second updates for a total of 5 seconds

# Function to open the prediction window
def open_prediction_window():
    prediction_window = tk.Toplevel(root)
    prediction_window.title("Prediction")
    prediction_window.geometry("600x400")  # Size for the new window
    prediction_window.config(bg="#e0e0e0")  # Background color for the prediction window
    
    frame = tk.Frame(prediction_window, bg="#f0f0f0", bd=2, relief=tk.SOLID)
    frame.pack(fill="both", expand=True, padx=10, pady=10)
    
    global result_label
    
    # Create predict button in the new window
    predict_button = tk.Button(frame, text="Predict", bg="green", fg="white", font=("Arial", 14, "bold"), command=predict_attack, height=2, width=20)
    predict_button.pack(pady=20)
    
    # Create result label in the new window
    result_label = tk.Label(frame, text="", bg="#f0f0f0", bd=2, relief=tk.SOLID, font=("Arial", 12, "bold"))
    result_label.pack(pady=20)

# Create the main application window
root = tk.Tk()
root.title("Intrusion Detection System")
root.geometry("1200x800")  # Increased window size
root.config(bg="#e0e0e0")  # Background color for the main window

# Create a frame for the heading with black background and padding
heading_frame = tk.Frame(root, bg="black", padx=10, pady=10)
heading_frame.pack(padx=20, pady=20, fill="x")  # Add padding around the heading frame

# Add heading
heading_label = tk.Label(heading_frame, text="Intrusion Detection System Using Machine Learning", font=("Arial", 24, "bold"), fg="white", bg="black", pady=20)
heading_label.pack()

# Create and place widgets (entry fields, button, label) within the window
labels = []
entry_list = []

# Define attribute names for labeling entry fields
attribute_names = [
    "Flow Duration", "Total Fwd Packets", "Total Backward Packets", "Total Length of Fwd Packets",
    "Total Length of Bwd Packets", "Fwd Packet Length Max", "Fwd Packet Length Min", "Fwd Packet Length Mean",
    "Fwd Packet Length Std", "Bwd Packet Length Max", "Bwd Packet Length Min", "Bwd Packet Length Mean",
    "Bwd Packet Length Std", "Flow Bytes/s", "Flow Packets/s", "Flow IAT Mean", "Flow IAT Std", "Flow IAT Max",
    "Flow IAT Min", "Fwd IAT Total", "Fwd IAT Mean", "Fwd IAT Std", "Fwd IAT Max", "Fwd IAT Min", "Bwd IAT Total",
    "Bwd IAT Mean", "Bwd IAT Std", "Bwd IAT Max", "Bwd IAT Min", "Fwd PSH Flags", "Bwd PSH Flags", "Fwd URG Flags",
    "Bwd URG Flags", "Fwd Header Length", "Bwd Header Length", "Fwd Packets/s", "Bwd Packets/s", "Min Packet Length",
    "Max Packet Length", "Packet Length Mean", "Packet Length Std", "Packet Length Variance", "FIN Flag Count",
    "SYN Flag Count", "RST Flag Count", "PSH Flag Count", "ACK Flag Count", "URG Flag Count", "CWE Flag Count",
    "ECE Flag Count", "Down/Up Ratio", "Average Packet Size", "Avg Fwd Segment Size", "Avg Bwd Segment Size",
    "Fwd Header Length.1", "Fwd Avg Bytes/Bulk", "Fwd Avg Packets/Bulk", "Fwd Avg Bulk Rate", "Bwd Avg Bytes/Bulk",
    "Bwd Avg Packets/Bulk", "Bwd Avg Bulk Rate", "Subflow Fwd Packets", "Subflow Fwd Bytes", "Subflow Bwd Packets",
    "Subflow Bwd Bytes", "Init_Win_bytes_forward", "Init_Win_bytes_backward", "act_data_pkt_fwd",
    "min_seg_size_forward", "Active Mean", "Active Std", "Active Max", "Active Min", "Idle Mean", "Idle Std",
    "Idle Max", "Idle Min"
]

# Create a scrollable frame
canvas = tk.Canvas(root, borderwidth=0, highlightthickness=0)
scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
scrollable_frame = tk.Frame(canvas, bg="#e0e0e0")  # Background color for the scrollable frame

# Configure scrollbar and canvas
canvas.configure(yscrollcommand=scrollbar.set, bg="#e0e0e0")
canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

# Function to update scroll region
def on_frame_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

scrollable_frame.bind("<Configure>", on_frame_configure)

# Function to scroll with mouse wheel
def _on_mouse_wheel(event):
    canvas.yview_scroll(int(-1*(event.delta/120)), "units")

canvas.bind_all("<MouseWheel>", _on_mouse_wheel)

# Create entry fields with larger width and borders
for row in range(21):  # Increase by 1 to accommodate the extra space for the button and label
    for col in range(4):
        index = row * 4 + col
        if index < len(attribute_names):
            label = tk.Label(scrollable_frame, text=f"{attribute_names[index]}:", font=("Arial", 10), bg="#e0e0e0")
            labels.append(label)
            label.grid(row=row, column=col*3, padx=5, pady=10, sticky="e")  # Increased row gap (pady)

            entry = tk.Entry(scrollable_frame, width=30, bd=2, relief=tk.GROOVE)  # Larger entry fields with border
            entry_list.append(entry)
            entry.grid(row=row, column=col*3+1, padx=5, pady=10)

# Create a submit button
submit_button = tk.Button(root, text="Submit", bg="blue", fg="white", font=("Arial", 14, "bold"), command=open_prediction_window)
submit_button.place(relx=0.5, rely=0.95, anchor="s")  # Positioned at the bottom center

# Start the GUI event loop
root.mainloop()
