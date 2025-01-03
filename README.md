Instagram Bot

This Python script automates actions on Instagram, such as logging into an account, searching for a user, and blocking (ignoring) a user automatically. The bot uses Selenium WebDriver to interact with Instagram’s web interface.

Prerequisites System Requirements Python 3.8+ Google Chrome (latest version)

Required Libraries:

selenium
chromedriver-autoinstaller
Features Login to Instagram: Automates the login process using the username and password from profil_data.py. Search for a User: The bot searches for the username you wish to block. Block User: Automates blocking the searched user by interacting with Instagram's interface.

Troubleshooting Driver Issues: Ensure your Chrome browser is updated. chromedriver_autoinstaller automatically installs the correct driver. Selector Errors: If Instagram’s interface changes, update the CSS or XPath selectors used to identify elements.
