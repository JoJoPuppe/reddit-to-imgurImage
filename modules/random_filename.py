import string
import re
from random import choices
from datetime import datetime


def generate_file_name(title):
    now = datetime.now()
    time_string = datetime.strftime(now, "%y%m%d%H%M%S")
    short_title = title[:8]
    short_title_without_spaces = "".join(short_title.split())
    cleaned_title = re.sub(r"[^a-zA-Z0-9]", "", short_title_without_spaces)
    return "_".join([time_string, cleaned_title])

def delete_ltp(ltp_text):
    if len(ltp_text) >= 8:
        chunk = ltp_text[:8].lower()
    else:
        chunk = ltp_text.lower()

    if "ltp" not in chunk:
        return ltp_text
    ltp_index = chunk.find("ltp")
    for i in range(ltp_index + 3, len(chunk)):
        if chunk[i].isalpha():
            break
    print(ltp_text[i:])
    return ltp_text[i:]
