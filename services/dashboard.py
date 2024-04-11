from PIL import Image, ImageTk
import tkinter as tk
def my_dashboard():
# Function to calculate button position based on screen geometry
    def calculate_button_position(window_width, window_height, button_index):
        button_width = 200
        button_height = 30
        button_spacing = 70  # Increased spacing
        margin = 100  # Increased left margin
        
        x = margin
        y = (button_height + button_spacing) * button_index + margin
        
        return x, y

    # Function to handle end monitoring
    def end_monitoring():
        print("Monitoring ended")  # Placeholder for actual functionality

    # Create tkinter window
    root = tk.Tk()
    root.geometry("1200x700")  # Set window size
    root.configure(bg="#dc3545")  # Set background color

    # Create a container frame for buttons
    container = tk.Frame(root, bg="#dc3545")
    container.pack(padx=0, pady=0)

    monitoring_window = tk.Label(container, text="Screen monitoring will be displayed here", bg="grey",
                                pady=100, padx=50, bd=50, relief="groove", width=50, height=10)
    monitoring_window.grid(row=0, column=0, columnspan=6, padx=10, pady=(100, 30), sticky="nsew")

    # Play button
    btn_play = tk.Button(container, text="▶ Play", bg="#007bff", fg="white", padx=10, pady=5, bd=4)
    btn_play.grid(row=1, column=0, padx=5, pady=5, sticky="ew")

    # Pause button
    btn_pause = tk.Button(container, text="⏸ Pause", bg="#dc3545", fg="white", padx=10, pady=5, bd=4)
    btn_pause.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

    # Forward button
    btn_forward = tk.Button(container, text="⏩ Forward", bg="#28a745", fg="white", padx=10, pady=5, bd=4)
    btn_forward.grid(row=1, column=2, padx=5, pady=5, sticky="ew")

    # Backward button
    btn_backward = tk.Button(container, text="⏪ Backward", bg="#ffc107", fg="black", padx=10, pady=5, bd=4)
    btn_backward.grid(row=1, column=3, padx=5, pady=5, sticky="ew")

    # Buttons
    btn_alert = tk.Button(root, text="ALERT MONITORING", bg="red", fg="white", padx=20, pady=30, bd=5)
    btn_alert.place(relx=0.9, x=-10, y=200, anchor="ne")

    btn_end = tk.Button(root, text="END MONITORING", bg="#17a2b8", fg="white", padx=25, pady=30, bd=6, command=end_monitoring)
    btn_end.place(relx=0.9, x=-10, y=330, anchor="ne")

    btn_start = tk.Button(root, text="START MONITORING", bg="#17a2b8", fg="white", padx=30, pady=30, bd=5)
    btn_start.place(x=100, y=200)  # Adjust the coordinates as needed

    btn_stop = tk.Button(root, text="STOP MONITORING", bg="#17a2b8", fg="white", padx=30, pady=30, bd=5)
    btn_stop.place(x=100, y=330)  # Adjust the coordinates as needed

    btn_logout = tk.Button(root, text="Logout", bg="#17a2b8", fg="white", padx=10, pady=10, bd=5)
    btn_logout.place(relx=1.0, x=-15, y=0, anchor="ne")

    # Heading label
    heading_label = tk.Label(root, text="Exam Integrity Monitoring System", font=("Arial", 30, "bold"), fg="#333", bg="#f0f0f0")
    heading_label.place(relx=0.5, y=25, anchor="n")

# root.mainloop()
