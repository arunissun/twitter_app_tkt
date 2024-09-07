#!/usr/bin/env python3

import tkinter as tk
from ui_functions import create_ui
import tweet_functions  # Import tweet_function to ensure the module is available

# Initialize the app
if __name__ == "__main__":
    app = tk.Tk()
    app.title("Twitter Bulk Tweet App")
    app.geometry("600x800")  # Set a size for the UI window

    # Pass the post_all_tweets function to create_ui
    create_ui(app)

    app.mainloop()

