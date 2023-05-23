from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
from tqdm import tqdm

def crawl_url(keyword='',pages=1):
    driver = webdriver.Chrome()
    url='https://www.a-ha.io/search/'+keyword
    driver.get(url)

    button=driver.find_element(By.CLASS_NAME, 'more10')
    i=0
    while i<pages:
        try:
            time.sleep(1)
            button.click()

            print(i)
            i+=1
        except:
            print('error')
            break

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    link = soup.find_all("a", "questionListCard__titleLink")
    print(len(link))
    url2=[]
    for i in range(len(link)):
        href=link[i].attrs['href']
        url2.append('https://www.a-ha.io'+href.split('?')[0]+'?aha_term='+href.split('aha_term=')[1])
    df = pd.DataFrame(data=url2, columns=['url'])
    df.to_csv('data/'+keyword+'_'+str(pages)+'.csv')

    driver.quit()


def crawl_text(file_name):
    qa_urls=pd.read_csv('data/'+file_name)['url']
    driver = webdriver.Chrome()
    df=pd.DataFrame(columns=['date','text','author','url'])
    f=0
    for url in tqdm(qa_urls):
        driver.get(url)

        try:
            html = driver.page_source
            soup = BeautifulSoup(html, 'html.parser')
            question = soup.find_all("h1", "a-card__headerTitle")
            question_title=question[0].get_text()

            res = soup.find_all("div", "editor__content")
            question_detail=res[0].get_text()
        
            author=soup.find_all("a", "tw-text-main-1 tw-text-base tw-mr-1 userName__nickname")
            date=soup.find_all("span", "author-info")
            for i in range(min(len(res)-1,len(author))):
                text=question_title+question_detail+res[i+1].get_text()
                df.loc[f]=([date[i].get_text(),
                            text,
                            author[i].get_text(),
                            url])
                f+=1
        except:
            print('Error Passed in url '+url)
            pass

    df.to_csv('data/'+'input_'+file_name,encoding='utf-8')

    driver.quit()


#crawl_url('기저귀',100)
crawl_text('기저귀_100.csv')

# 생리대, 기저귀
#생리30,이유식, 임신, 아기,