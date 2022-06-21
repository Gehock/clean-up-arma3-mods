import os
from pathlib import Path
import shutil

from bs4 import BeautifulSoup
import requests

from secret import COOKIE, STEAM_USERNAME, WORKSHOP_PATH

URL = 'https://steamcommunity.com/id/{0}/myworkshopfiles/?appid=107410&browsefilter=mysubscriptions&numperpage=30&p={1}'
WORKSHOP_PATH = Path(WORKSHOP_PATH)

def get_page(page: int) -> str:
    url = URL.format(STEAM_USERNAME, page)
    print(f"Fetching {url}")
    r = requests.get(url, cookies=COOKIE)
    print(f"Status code: {r.status_code}")
    data = r.text
    return data


def get_ids() -> list[str]:
    data = get_page(1)
    soup = BeautifulSoup(data, 'html.parser')

    paging = soup.find('div', {'class': 'workshopBrowsePagingControls'})
    pagelink: str = paging.find_all('a', {'class': 'pagelink'})[-1]['href']
    pages = pagelink.split('=')[-1]
    print(f"Total pages: {pages}")


    for i in range(2, int(pages) + 1):
        print(f"Fetching page {i}/{pages}")
        data += get_page(i)

    soup = BeautifulSoup(data, 'html.parser')
    items = soup.find_all('div', {'class': 'workshopItemSubscriptionDetails'})
    urls = [item.find('a')['href'] for item in items]
    ids = [url.split('=')[-1] for url in urls]
    return ids

def move_dirs():
    ids = get_ids()
    target_path = WORKSHOP_PATH / '../to_be_removed'
    try:
        os.mkdir(target_path)
    except FileExistsError:
        pass

    for item in os.scandir(WORKSHOP_PATH):
        if not item.is_dir:
            continue
        if item.name not in ids:
            shutil.move(item.path, target_path)

    print(f"Moved extra items to {target_path}")

def main():
    move_dirs()

if __name__ == '__main__':
    main()
