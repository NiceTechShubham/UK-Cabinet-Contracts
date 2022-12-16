import requests
from bs4 import BeautifulSoup
from lxml import etree
import os
import pandas 


class Contracts:
    def __init__(self):
        os.system('cls')
        
        
    def Scraper(self):
        print("Please Wait....")
        value=1
        url=(f"https://www.contractsfinder.service.gov.uk/Search/Results?&page={value}#dashboard_notices")
        name,departmen,loc,voc,pr,pd,cd,ct,csd,ced,contract_type,pt=[],[],[],[],[],[],[],[],[],[],[],[]
        count=1
        n=requests.get(url).text
        soup=BeautifulSoup(n,'html.parser')
        l1=soup.find('span',class_='standard-paginate-detail').text
        a,b,c=l1.split(" ")
        c=int(c)
        os.system('cls')
        print(f"""The total number of pages are {c} how many pages you want to extract ?
            # Enter Custom Value from 1 to {c}
            # Enter 0 for all pages""")
        usr_input=int(input("Enter desired value: "))
        if usr_input>0 and usr_input<=c:
            c=usr_input
        elif usr_input==0:
            pass
        else:
            print("Invalid Input.")
            print("Extracting all pages....")
        for p in range(1,int(c)+1):
            value=p
            n1=requests.get(url).text
            soup1=BeautifulSoup(n1,'html.parser')
            for i in soup1.find_all('a',class_='govuk-link search-result-rwh break-word'):
                os.system('cls')
                print("Total Page is",c,"and total link is",int(c)*20)
                print(f'From page',value,end=" ")
                print(f"Scraping link {count}....")
                Page=requests.get(i.get('href')).text
                page_soup=BeautifulSoup(Page,'html.parser')
                xml=etree.HTML(str(page_soup))
                loop=page_soup.find('div',class_='content-block').find_all('strong')
                count+=1
                if len(loop)==13:
                    name.append(page_soup.find('h1',class_="govuk-heading-l break-word").text)
                    departmen.append(page_soup.find('h2',class_='breadcrumb-description').text)
                    loc.append(xml.xpath('//*[@id="content-holder-left"]/div[3]/p[2]/span')[0].text) 
                    voc.append(xml.xpath('//*[@id="content-holder-left"]/div[3]/p[3]')[0].text) 
                    pr.append(xml.xpath('//*[@id="content-holder-left"]/div[3]/p[4]')[0].text) 
                    pd.append(xml.xpath('//*[@id="content-holder-left"]/div[3]/p[5]')[0].text) 
                    cd.append(xml.xpath('//*[@id="content-holder-left"]/div[3]/p[6]')[0].text) 
                    ct.append(xml.xpath('//*[@id="content-holder-left"]/div[3]/p[7]')[0].text) 
                    csd.append(xml.xpath('//*[@id="content-holder-left"]/div[3]/p[8]')[0].text)
                    ced.append(xml.xpath('//*[@id="content-holder-left"]/div[3]/p[9]')[0].text)
                    contract_type.append(xml.xpath('//*[@id="content-holder-left"]/div[3]/p[10]')[0].text)
                    pt.append(xml.xpath('//*[@id="content-holder-left"]/div[3]/p[11]')[0].text)
                else:
                    continue
        data=pandas.DataFrame({"Name":name,"Department":departmen,"Location of contract":loc,"Value of contract":voc,"Procurement reference":pr,"Published date":pd,"Closing date":cd,"Closing time":ct,"Contract start date":csd,"Contract end date":ced,"Contract type":contract_type,"Procedure type":pt})
        data.to_csv(r'C:\Users\Public\UK_Cabinet_Contracts.csv',index=False)
        
        
        
        
Scrap=Contracts()
Scrap.Scraper()