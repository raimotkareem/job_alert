import requests
import bs4
def get_job():
    total_page = 3 #the real total_page is round(total_page) i use 3 to reduse terminal run
    for page in range(1,total_page+1): 

        url = 'https://www.myjobmag.com/search/jobs?location=Abuja&currentpage='+str(page)
        response = requests.get(url)
        soup = bs4.BeautifulSoup(response.text,'html.parser')
        # total_search = soup.find('div',class_="mag-b bp-bt-25").h3.text
        # total_search = total_search.split(' ')
        # total_search = total_search[0]
        # total_search = int(total_search)
        # each_page = 18 #jobs per page
        # total_page = (total_search/18)
        # total_page = round(total_page)

        jobs = soup.find_all('li',class_="job-list-li")
        for i in jobs:
            try:
                name = i.find(class_='mag-b').a['href']
                name = name.split('/')
                name = name[2]
                #return name
                print(name)
                # desc = i.find(class_='job-desc').text
                # print(desc)
            except:
                pass
                       
get_job()

















# print(jobs)
# links_with_text = []
# for a in jobs.find_all('a', href=True): 
#     if a.text: 
#         links_with_text.append(a['href'])
#         print(a)



