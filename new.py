import time

import requests
from bs4 import BeautifulSoup

# Get job roles list and link
url = 'https://www.linkedin.com/company/job-search'
response = requests.get(url)
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:104.0) Gecko/20100101 Firefox/104.0',
    'referer': 'https://www.google.com/',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,'
              'application/signed-exchange;v=b3;q=0.9',
    'cookie': 'bcookie="v=2&723d74fe-b429-429e-83dc-b7ee65d018bc"; li_sugr=2d79b512-d11c-421c-9980-e39ebb307576; bscookie="v=1&2022061504330805274252-f5fd-4e9c-8cb1-64391601da91AQEYzj4QwxDjMH7RcUB2z80tzeqjr5EP"; li_rm=AQHcFYROvt72mwAAAYOIEA-_MUZYI5Itx6aoE6rvFqDYfKIVZvvmTD1JMpo-ZuEqJlRch7t-xCnkiJXqyt88qJX24YlefAbP3g-jD1ycMTK_5JgnhdLbJvVS; G_ENABLED_IDPS=google; aam_uuid=21748031293479496931328068920960085902; _gcl_au=1.1.1931008031.1664865338; timezone=Asia/Calcutta; li_theme=light; li_theme_set=app; AnalyticsSyncHistory=AQKe7rfTx216GwAAAYOhtu6mEBE3qmGp8boQ-VCsAB89f5igvVOoxEbNCyjfZfJwUzAi8pruONMan8AGDzBjwA; _guid=0acd397f-9070-4585-af4c-071c9ebaa3c7; lms_ads=AQG0eJY_pYJj0wAAAYOhtu_Q6cVi2J5hZForD4AgC_ueJgmN9o7E-64iKYwZNQjFYeMtkaZKjFhssP9TOgOb_AkpQA0-Sbo_; lms_analytics=AQG0eJY_pYJj0wAAAYOhtu_Q6cVi2J5hZForD4AgC_ueJgmN9o7E-64iKYwZNQjFYeMtkaZKjFhssP9TOgOb_AkpQA0-Sbo_; visit=v=1&M; UserMatchHistory=AQK2fTvXmPXomQAAAYOs-ybMhcwcjGosUQY3iSSTzPGE7A-J6_vJpRaIHXwH_92xdUT05pzOyFHkH1hC_S5vX2psO0Ff9IxsmUu-ruvMyLD2JCv_jKZu1-_FiML9go94FVHZxsO9fSznthlcOmZQsdnGMBWIrN5U-7SCXBheDRvCUxbbsUHTTT7AnA2hWQlF3hWEJu8nB19m8VTCn4fVj6XbCjzLh-KXiRiUBbaXtGRmAnM-4inSEeegufaxbJb1k5KLL9HicZwoJFSrsjVZCE53qmkiCIdJGfyT-lQ; g_state={"i_l":2,"i_p":1665140896152}; lang=v=2&lang=en-us; JSESSIONID="ajax:0202520333063209757"; AMCVS_14215E3D5995C57C0A495C55%40AdobeOrg=1; AMCV_14215E3D5995C57C0A495C55%40AdobeOrg=-637568504%7CMCIDTS%7C19272%7CMCMID%7C22251617428399533341342372413584514117%7CMCAAMLH-1665730865%7C12%7CMCAAMB-1665730865%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1665133265s%7CNONE%7CvVersion%7C5.1.1%7CMCCIDH%7C1373552835; fid=AQHjHg1_-GGXzwAAAYOxRAat4v3MjXt7CYqkH5Ewgk7g7WqKlkyjxpDCibDZqkG9WL4AUnRhSIyreg; G_AUTHUSER_H=0; fcookie=AQE-rJyiB6RC_QAAAYOxRBRbceKO5fZz0BDzaj_a1pGlifPKq-WT9u8Y8iPjfUudUmyQx3h6HluyKsGnzW-A9Ys_Sqh7QTLyQyKdh4qTdq5XBgy_XG-yje2xKRY53IOyh1hNG6S2FESdbfiWXPv52H2aEzevvRZfFy8oRvpqtmSl8qYvkwvSPMku6t6hqaY9NDI3UNGEOmFWE3yOWVLj3iB4GvDUfh_t8hk2RxqIPyYtu9985mpmI5dlMlPlGHMuZB/Cp4yyagr/im40hirrxH27kr8DLOtNlbL1ScKGNJpqX3F62RzmYJBkhsQRYQvScPCu2UloYFSPhHMNAnkOsA==; lidc="b=VGST02:s=V:r=V:a=V:p=V:g=2731:u=1:x=1:i=1665127270:t=1665213670:v=2:sig=AQH1GeSrc88_q5alSUHB5oUKiqtDr1aH"; recent_history=AQEPdWBYUhmRwgAAAYOxU5IMKoTSxi9SSxC11Gpn6gi-SzeDRgVFNZdlfHJLhYKJFt-nHTbQGt70R9xSO1EYzkZDOiW5fxd7VF6JvgsNCmgtRd80ztH1kK-Qhcj4Of6lvwMhry9pNL3_r4iXDApQry8LRy1qFkqixP0sd0KeEPJx1xb_rEnSLPJe9_0tdqFWOp_xqQRwUuQaJd7YExTpeQXq_nNfBjOy23ZEMyI0GgPqZPWdku_c0C4SXzYm9sz07zolrorsP7QPk8cUFndrEnf8ckz8K3tkBjM_yo3dDY3LgAjtPoyhwD21OVfsQWsEUOE-og1AIe8Kqeuc344wP3TVVgvvU21NiSY2EE-QZalXgdg2HDUPsPKSg12F8OfJvnzteCnYyBJ_6npVj7Dpy_U8jtSjYX2eLAzlP3c1ukuyMfxpAKJugmGipjNz-reh7VUPsE2xDjMnpXQ75jcXCeVy41_Uc4aVZgcP6bCez1qALv4IiNZugihEnkhNH4OaqGaiw28TR_C0_Wz5fGJImcITrapRawdcUT3oUlQ8WQoVFUZzxg7hjaDAV6gUbaRXcem15s-dbuvYkLmeLlQNTXN6OS1EK1L48UpnaRQLzqAOyx57WV4w9XkxnWXH5oLconPTNlo8dsD3BwJF7vDF0G62mDzFxQHuJPeETX15bnglvq0ADIMt_99rPFrZkD6XFKdwQ3HNbJk-9SqmIK4'
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')
print(soup.prettify())
browse_section = soup.find('section', attrs={'data-test-id': 'browse-jobs'})
list_data = browse_section.find('ul', class_="show-more-less__list show-more-less__list--hide-after-10")
job_roles = []
for data in list_data.findAll('li'):
    job_roles.append(data.text.split()[:-3])

urls_to_get_data = []
for job_role in job_roles:
    job_role = '-'.join(job_role).lower()
    time.sleep(2)
    second_url = f'https://www.linkedin.com/jobs/{job_role}?trk=organization_guest-browse_jobs'
    urls_to_get_data.append(second_url)

print(urls_to_get_data)

headers['referer'] = url
#
# for url in urls_to_get_data:
#     second_response = requests.get('')