#
#
# Company - > AMDARIS
# Link - > https://boards.eu.greenhouse.io/amdaris?t=234a6602teu
#

import requests
from bs4 import BeautifulSoup
from A_OO_get_post_soup_update_dec import update_peviitor_api, DEFAULT_HEADERS
from L_00_logo import update_logo
import uuid


def get_jobs():
    """
    This function collects data from the company site.
    """
    list_jobs = []

    response = requests.get('https://boards.eu.greenhouse.io/amdaris?t=234a6602teu', headers=DEFAULT_HEADERS)
    soup = BeautifulSoup(response.text, features='lxml')
    jobs = soup.find_all('div', class_='opening')

    for job in jobs:
        link = 'https://boards.eu.greenhouse.io/' + job.find('a')['href']
        title = job.find('a').text
        location = job.find('span', class_='location').text

        if 'Romania' in location or 'România' in location:
            try:
                city = location.split()[0].strip(',')
            except IndexError:
                continue

            list_jobs.append({
                "id": str(uuid.uuid4()),
                "job_title": title,
                "job_link": link,
                "company": "AMDARIS",
                "country": "Romania",
                "city": city
            })

    return list_jobs

@update_peviitor_api
def scrape_and_update_peviitor(company_name, data_list):
    """
    Update data on peviitor API!
    """

    return data_list


company_name = 'AMDARIS'
data_list = get_jobs()
scrape_and_update_peviitor(company_name, data_list)

print(update_logo('AMDARIS',
                  'https://s101-recruiting.cdn.greenhouse.io/external_greenhouse_job_boards/logos/400/015/610/original/Logo_white_on_blue.png?1638449935'
                  ))
