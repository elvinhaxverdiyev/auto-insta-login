from instabot import InstagramBot
from constants import username, password

app = InstagramBot(username, password)
app.open_link()
app.login(username, password)
app.click_login_button()
app.not_now()
app.click_search()
app.write_name()
app.ignore_user()
app.ignore()
app.is_sure()