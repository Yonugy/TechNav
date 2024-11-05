import tkinter as tk
from tkinter import ttk
import requests
from bs4 import BeautifulSoup
import webbrowser

win= tk.Tk()
win.title('TechNav')
win.geometry('400x250')
win.config(bg="#6cade9")

languages={}

def openlink():
    current_lang=d_data.get()
    langurl=languages[current_lang]
    webbrowser.open(langurl)

languages1={}

def openlink1():
    current_lang=d_data2.get()
    langurl=languages1[current_lang]
    webbrowser.open(langurl)

languages3={}

def openlink3():
    current_lang=d_data3.get()
    langurl=languages3[current_lang]
    webbrowser.open(langurl)



def scrape_w3s():
    url = "https://www.w3schools.com/"
    avoid=['Tutorial','Reference','Overview','Create a Website HOT!','Create a Server NEW']
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            # Parsing the webpage content
            soup = BeautifulSoup(response.text, 'lxml')

            # Find all article links within the specific div class on W3Schools
            articles = soup.find('div', class_='w3-bar-block').find_all('a')

            if not articles:
                print("No articles found.")
                return

            for article in articles:
                title = article.text.strip()
                if "Learn" in title:
                    title=' '.join(title.split(' ')[1:]).strip()
                
                title=list((map(lambda x: x.strip(),title.split())))
                title=' '.join([i for i in title if i!=""])
                if title in avoid:
                    continue
                if title in languages:
                    continue
                link = article['href']
                full_link = f"https://www.w3schools.com{link}"
                #print(title)
                languages[title]=full_link
                #print(full_link)
        else:
            print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

    except Exception as e:
        print(f"An error occurred: {e}")

def scrape_geeks():
    url = "https://www.geeksforgeeks.org/"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            # Parsing the webpage content
            soup = BeautifulSoup(response.text, 'lxml')

            # Find all article links (you may need to adjust the selector based on the layout)
            
            #articles = soup.find('li', class_='containerSubheader').find_all('a')
            #articles = soup.find_all('a', class_='mainContainerSubheader')
            article_div = soup.find('div', class_='mainContainerSubheader').find("ul",class_="containerSubheader")
            articles = article_div.find_all('li')

            if not articles:
                print("No articles found.")
                return

            for article in articles:
                title = article.find('a',class_='link').get_text(strip=True)

                # Modify title if it contains "Learn"
                if "Learn" in title:
                    title = ' '.join(title.split(' ')[1:]).strip()
                
                # Clean up the title
                title = list(map(lambda x: x.strip(), title.split()))
                title = ' '.join([i for i in title if i != ""])

                # Skip titles already in languages1 dictionary
                if title in languages1:
                    continue
                
                link = article.find('a',class_='link')['href']
                
                # Check if the link is relative or absolute
                full_link = link if link.startswith("http") else f"https://www.geeksforgeeks.org{link}"
                
                # Store the title and link in the dictionary
                languages1[title] = full_link

                #print(title,full_link)

        else:
            print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

    except Exception as e:
        print(f"An error occurred: {e}")

def scrape_tp():
    url = "https://www.tutorialspoint.com/index.htm"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            # Parsing the webpage content
            soup = BeautifulSoup(response.text, 'lxml')

            # Find all article links (you may need to adjust the selector based on the layout)
            
            #articles = soup.find('li', class_='containerSubheader').find_all('a')
            #articles = soup.find_all('a', class_='mainContainerSubheader')
            article_div = soup.find('div', class_='library-nav__slider').find('ul')
            articles = article_div.find_all('li')

            if not articles:
                print("No articles found.")
                return

            for article in articles:
                title = article.find('a').get_text(strip=True)

                # Modify title if it contains "Learn"
                if "Learn" in title:
                    title = ' '.join(title.split(' ')[1:]).strip()
                
                # Clean up the title
                title = list(map(lambda x: x.strip(), title.split()))
                title = ' '.join([i for i in title if i != ""])


                # Skip titles already in languages1 dictionary
                if title in languages3:
                    continue
                
                link = article.find('a')['href']
                
                # Check if the link is relative or absolute
                full_link = link if link.startswith("http") else f"https://www.tutorialspoint.com/{link}"
                
                # Store the title and link in the dictionary
                languages3[title] = full_link

                #print(title,full_link)

        else:
            print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

    except Exception as e:
        print(f"An error occurred: {e}")


# Call the function to start scraping
scrape_w3s()
scrape_geeks()
scrape_tp()

win.columnconfigure(0, weight=1)
win.columnconfigure(1, weight=1)
win.columnconfigure(2, weight=1)

d_data=tk.StringVar(value='Select')
l1=tk.Label(text = 'Navigations of W3Schools',bg="#6cade9")
combo=ttk.Combobox(win,values=list(languages.keys()),textvariable=d_data)
l1.grid(row=1,column=1)
combo.grid(row=2,column=1)
linkbtn=tk.Button(text="Navigate",command=openlink,bg="#0f1d90",fg="white")
linkbtn.grid(row=3,column=1)

d_data2=tk.StringVar(value='Select')
l2=tk.Label(text = 'Navigations of GeeksforGeeks',bg="#6cade9")
combo2=ttk.Combobox(win,values=list(languages1.keys()),textvariable=d_data2)
l2.grid(row=4,column=1)
combo2.grid(row=5,column=1)
linkbtn2=tk.Button(text="Navigate",command=openlink1,bg="#0f1d90",fg="white")
linkbtn2.grid(row=6,column=1)

d_data3=tk.StringVar(value='Select')
l3=tk.Label(text = 'Navigations of Tutorials Point',bg="#6cade9")
combo3=ttk.Combobox(win,values=list(languages3.keys()),textvariable=d_data3)
l3.grid(row=7,column=1)
combo3.grid(row=8,column=1)
linkbtn3=tk.Button(text="Navigate",command=openlink3,bg="#0f1d90",fg="white")
linkbtn3.grid(row=9,column=1)

win.mainloop()