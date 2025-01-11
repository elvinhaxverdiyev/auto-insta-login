# Instagram Bot - README

## Overview
This application is a bot designed to perform automated tasks on Instagram. The bot logs into the user account, searches for a specific profile, and automatically blocks the user.

## Key Features
1. **Login**: Logs into an Instagram account using the specified username and password.
2. **Profile Search**: Searches for a specific user profile by entering a username in the search field.
3. **Blocking**: Blocks the identified user and confirms the action.

## Installation and Execution
1. Install the required Python libraries:
   ```bash
   pip install selenium chromedriver-autoinstaller
   ```
2. Create the `constants.py` and `base_url.py` files and add the following information:
   - `constants.py`: Define variables for username (`username`), password (`password`), and the username to search and block (`ignore_name`).
   - `base_url.py`: Define the URL for the Instagram login page (`url`).
3. Run the application with the following command:
   ```bash
   python instagram_bot.py
   ```

## Usage
1. Update the `username`, `password`, and `ignore_name` variables in the code with your credentials and target username.
2. The bot will open the Instagram login page, log in, search for the user in the search field, and block them.

## Notes
- Keep your login credentials secure and do not share them with others.
- Ensure that the ChromeDriver used by Selenium is compatible with your browser version.
- Make sure your internet connection is stable for the bot to operate smoothly.

