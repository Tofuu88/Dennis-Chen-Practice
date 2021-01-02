import argparse
import os
import re
from collections import deque
import requests
from bs4 import BeautifulSoup

def ny_times_request():
    r_nytimes = requests.get("https://nytimes.com")
    nytimes_text = r_nytimes.text
    with open("web_content.html", "w", encoding="utf-8") as web_content:
        web_content.write(nytimes_text)
    with open("web_content.html", "r", encoding="utf-8") as web_content:
        print(web_content.read())

def bloom_request():
    r_bloom = requests.get("https://bloomberg.com")
    bloom_text = r_bloom.text
    with open("web_content.html", "w") as web_content:
        web_content.write(bloom_text)
    with open("web_content.html", "r") as web_content:
        print(web_content.read())

def url_validate(inp):
    count = 0
    valid_url_set = set([".com", ".net", ".org"])
    for i in inp:
        if i == ".":
            count += 1
    if count != 1:
        return False
    else:
        url_valid = None
        for j in valid_url_set:
            reg_exp_obj = re.compile(j)
            if reg_exp_obj.search(inp) != None:
                url_valid = True
        if url_valid:
            return True
        else:
            return False

def enter_url():
    url_set = set(["nytimes.com", "bloomberg.com"])
    command_deque_current = deque()  # same as list but more memory efficient
    command_deque_past = deque()

    while True:
        user_inp = input()
        bloom_pat = "bloomberg.com"
        nytimes_pat = "nytimes.com"
        if user_inp == "exit":
            break
        elif user_inp == "back":
            try:
                if command_deque_past[-1] == "nytimes":
                    ny_times_request()
                elif command_deque_past[-1] == "bloomberg":
                    bloom_request()
            except IndexError:
                pass
        elif not url_validate(user_inp):
            print("url error")
            continue
        elif user_inp not in url_set:
            print("error! URL not in the current list")
        
        elif re.search(nytimes_pat, user_inp) != None:
            command_deque_current.append("nytimes")
            ny_times_request()
            try:
                command_deque_past.append(command_deque_current[-2])
            except IndexError:
                pass

        elif re.search(bloom_pat, user_inp) != None:
            command_deque_current.append("bloomberg")
            bloom_request()
            try:
                command_deque_past.append(command_deque_current[-2])
            except IndexError:
                pass

def main():
    parser = argparse.ArgumentParser(description="directory to save data")
    parser.add_argument("--dir", help="create the directory to store data")
    args = parser.parse_args()
    directory = args.dir
    # directory = r"C:\Users\denni\PycharmProjects\Text-Based Browser\Text-Based Browser\task\tb_tabs"

    try:
        os.mkdir(directory)
    except FileExistsError:
        print("folder already exists")
    enter_url()

if __name__ == "__main__":
    main()