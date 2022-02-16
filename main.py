import re
import requests
html_text = requests.get("https://www.google.com")
html_text.raise_for_status()
stat_code = html_text.status_code
if stat_code == 200:
    print("Yaay!, We have connected to the Server")
else:
    print("Connection lost, Please try again later.")
print("\nThe End")