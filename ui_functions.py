import tkinter as tk
from tkinter import filedialog
import threading
import tweet_functions  # Ensure you import the correct tweet_function module

# Create the variables for user credentials
consumer_key_var = None
consumer_secret_var = None
access_token_var = None
access_token_secret_var = None

def browse_images(entry_field):
    """Function to browse and select an image path."""
    file_paths = filedialog.askopenfilenames()  # Allow multiple file selection
    if file_paths:
        entry_field.delete("1.0", tk.END)  # Clear existing text
        entry_field.insert("1.0", '\n'.join(file_paths))  # Insert new file paths separated by new lines

def post_tweets_thread():
    """Function to run the posting tweets function in a separate thread."""
    tweet_functions.post_all_tweets(
        tweet_text_vars,
        [image_path_var.get("1.0", "end").strip() for image_path_var in image_path_vars],
        (
            consumer_key_var.get().strip(),
            consumer_secret_var.get().strip(),
            access_token_var.get().strip(),
            access_token_secret_var.get().strip()
        )
    )

def create_ui(app):
    """Function to create the UI interface."""
    global consumer_key_var, consumer_secret_var, access_token_var, access_token_secret_var
    global tweet_text_vars, image_path_vars

    # Initialize StringVar for credentials after the root window is created
    consumer_key_var = tk.StringVar(app)
    consumer_secret_var = tk.StringVar(app)
    access_token_var = tk.StringVar(app)
    access_token_secret_var = tk.StringVar(app)

    # Create a canvas with a scrollbar
    canvas = tk.Canvas(app)
    scrollbar = tk.Scrollbar(app, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)

    scrollbar.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)

    content_frame = tk.Frame(canvas)
    canvas.create_window((0, 0), window=content_frame, anchor="nw")

    # Add credential input fields
    tk.Label(content_frame, text="Consumer Key").pack()
    tk.Entry(content_frame, textvariable=consumer_key_var).pack()

    tk.Label(content_frame, text="Consumer Secret").pack()
    tk.Entry(content_frame, textvariable=consumer_secret_var).pack()

    tk.Label(content_frame, text="Access Token").pack()
    tk.Entry(content_frame, textvariable=access_token_var).pack()

    tk.Label(content_frame, text="Access Token Secret").pack()
    tk.Entry(content_frame, textvariable=access_token_secret_var).pack()

    # Add text boxes for multiple tweets (up to 10 tweets)
    tweet_text_vars = []
    image_path_vars = []
    for i in range(10):
        tk.Label(content_frame, text=f"Tweet {i+1}").pack()
        tweet_text_var = tk.Text(content_frame, height=3, width=50)
        tweet_text_var.pack()
        tweet_text_vars.append(tweet_text_var)

        image_label = tk.Label(content_frame, text="Image Paths (one per line)")
        image_label.pack()
        image_path_var = tk.Text(content_frame, height=2, width=60)  # Changed to Text widget
        image_path_var.pack()
        browse_button = tk.Button(content_frame, text="Browse", command=lambda e=image_path_var: browse_images(e))
        browse_button.pack()
        image_path_vars.append(image_path_var)

    # Add buttons for posting tweets
    post_button = tk.Button(content_frame, text="Post Tweets", command=lambda: threading.Thread(target=post_tweets_thread).start())
    post_button.pack(pady=10)

    content_frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

    # Configure scrollbar appearance
    scrollbar.config(bg='#333333', troughcolor='#2e2e2e')

