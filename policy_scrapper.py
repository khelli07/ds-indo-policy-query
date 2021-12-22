import os
import requests, json
from bs4 import BeautifulSoup

clear = lambda: os.system('cls')

page_ctr = 1
policy_database = {}

while (page_ctr <= 2703):
    print(f"Processing page {page_ctr}...")
    url = f"https://peraturan.go.id/peraturan/index.html?PeraturanSearch%5Bjenis_peraturan_id%5D=&PeraturanSearch%5Bnomor%5D=&PeraturanSearch%5Btahun%5D=&PeraturanSearch%5Btentang%5D=&page={page_ctr}"
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')

    table = soup.find_all("tr")[1:]
    for content in table:
        component = content.find_all("td")
        used_content = component[1:3]
        
        policy_name = used_content[0].text.strip()
        policy_topic = used_content[1].text.strip()

        policy_database.update({ policy_name: policy_topic })

    page_ctr += 1
    clear()

print("Retrieving data successful!")

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(policy_database, f, ensure_ascii=False, indent=4)