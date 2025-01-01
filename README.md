Instagram Bot README

This project is a Python-based bot that uses the Selenium library to automate logging into Instagram and navigating to a specific profile.

Requirements

To use this bot, you need:

Python 3.7+

The following Python libraries:

selenium

chromedriver_autoinstaller

Installation

Install the required libraries:
Run the following command in your terminal to install the necessary libraries:

pip install selenium chromedriver-autoinstaller

Create a profil_data.py file:
In the project directory, create a file named profil_data.py and add the following content:

username = "your_instagram_username"
password = "your_instagram_password"

Prepare the script:
Save the provided Python script in the same directory as profil_data.py.

Usage

Run the script:

python your_script_name.py

When the script runs:

It will navigate to the Instagram website.

Enter the username and password from profil_data.py.

After logging in, it will navigate to the specified profile URL (e.g., e_lv_n).

Code Structure Details

chromedriver_autoinstaller usage:

Automatically installs and configures ChromeDriver, eliminating the need for manual setup.

Login functionality:

Retrieves username and password from the profil_data.py file.

Profile navigation:

After logging in, it navigates to the target profile URL using driver.get().

Notes

Respect Instagram's terms of service:

Use the bot responsibly to avoid violating Instagram's policies.

Avoid excessive or rapid testing.

Security:

The script handles sensitive information (username and password). Ensure this information is stored securely.

Troubleshooting

ChromeDriver errors:

Update your Chrome browser to the latest version.

If chromedriver_autoinstaller fails, download and configure ChromeDriver manually.

Element not found errors:

Instagram's interface might have changed. Update the XPath values accordingly.

Delays in execution:

Increase the time.sleep() durations to handle slower loading times.

Future Plans

Extend functionalities (e.g., liking posts or leaving comments).

Implement more secure password management.
