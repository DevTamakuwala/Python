import re
text = "Loving #Python and #AI with @user1 and @user2!"
hashtags = re.findall(r'#\w+', text)
mentions = re.findall(r'@\w+', text)
no_spaces = re.sub(r'\s+', '_', text)
print("Hashtags:", hashtags)
print("Mentions:", mentions)
print("No spaces:", no_spaces)
