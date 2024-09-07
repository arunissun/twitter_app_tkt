# TweetBot

TweetBot is a Python application that allows you to interact with Twitter through various functionalities including posting tweets, replying to tweets, and quoting tweets. It utilizes the Tweepy library for Twitter API interactions and Tkinter for a user-friendly interface. The application supports bulk posting with intervals and comes with a ready-to-use executable for Windows.

## Features

- **Post Tweets**: Send individual tweets directly from the application.
- **Reply to Tweets**: Respond to existing tweets with ease.
- **Quote Tweets**: Quote other tweets with your own commentary.
- **Bulk Posting**: Send up to 10 tweets in one go, with intervals of 20 seconds between each tweet.
- **User Interface**: Simple and intuitive GUI built with Tkinter.
- **Executable File**: Pre-built executable available for Windows users.

## Installation

To use TweetBot, you need to install the required Python packages and set up your environment. Follow these steps:

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your-username/your-repository.git
   cd your-repository ```

2. Set Up a Virtual Environment (optional but recommended)

   ```bash
   python3.11 -m virtualenv venv source venv/bin/activate  
   On Windows, use venv\Scripts\activate 
   ```

3. Install Dependecies 

   Install the required python packages using pip
   This code uses Tweepy and it can only work with python>=3.10
   
4. Configure the Twitter API

  - Obtain your Twitter API credentials from the Twitter Developer Portal.
  - Set up your API keys and tokens for both API v1 (for media uploads) and API v2 (for text operations).
  - Input these credentials in the application UI or directly in the code (depending on the application's setup). 

## Usage

1.  Run the Application

- **Pre-built Executable**: To start the application, use the pre-built executable file for Windows by double-clicking `TweetBot.exe`.

- **From Source Code**: Alternatively, if running from source code, execute:

  ```bash
  python main.py 
  ```

2. Using the GUI
 - Compose Tweets: Enter tweet text and use the provided options to reply or quote tweets.
 - Upload Media: Use the media upload feature to attach images and other media to your tweets.
 - Bulk Posting: Utilize the bulk posting functionality to send multiple tweets at intervals.
 - Configure Settings: Enter your Twitter API credentials and adjust other settings through the UI.

## Executable File 

  A pre-built executable file for Windows is available in the dist directory. 
  This allows users to run TweetBot without needing to set up a Python environment.

## Contributing 
  Contributions are welcome! If you have any suggetions, improvements or bug reports
  please submit a pull request or open issue.

## Contact 
 
  For any questions or feedback, please contact arun.elte@gmail.com

