
from diagrams import Diagram
from diagrams.custom import Custom
from urllib.request import urlretrieve

import shutil,os

folder_path = "temp_src_images"
shutil.rmtree(folder_path)
os.mkdir(folder_path)

import requests
from bs4 import BeautifulSoup
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def get_image_urls(query):
    url = f"https://www.google.com/search?q={query}&tbm=isch"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    try:
        response = requests.get(url, headers=headers, verify = False)
    except:
        pass
    soup = BeautifulSoup(response.content, "html.parser")
    image_urls = []
    for img in soup.find_all("img"):
        img_url = img.get("src")
        if img_url:
            image_urls.append(img_url)
    return image_urls[1]

with Diagram("architecture_diagram", show=False):

    urlretrieve(get_image_urls("icon of Positive/Negative Result in AZURE"), "/content/sample_data/image_src/Positive_Negative_Result_icon.png")
    Positive_Negative_Result_ = Custom("Positive/Negative Result \n", "/content/sample_data/image_src/Positive_Negative_Result_icon.png")

    urlretrieve(get_image_urls("icon of Text Data in AZURE"), "/content/sample_data/image_src/Text_Data_icon.png")
    Text_Data_ = Custom("Text Data \n", "/content/sample_data/image_src/Text_Data_icon.png")

    urlretrieve(get_image_urls("icon of Azure Cognitive Services in AZURE"), "/content/sample_data/image_src/Azure_Cognitive_Services_icon.png")
    Azure_Cognitive_Services_ = Custom("Azure Cognitive \nServices ", "/content/sample_data/image_src/Azure_Cognitive_Services_icon.png")

    urlretrieve(get_image_urls("icon of Sentiment Score in AZURE"), "/content/sample_data/image_src/Sentiment_Score_icon.png")
    Sentiment_Score_ = Custom("Sentiment Score \n", "/content/sample_data/image_src/Sentiment_Score_icon.png")

    urlretrieve(get_image_urls("icon of Sentiment Analysis in AZURE"), "/content/sample_data/image_src/Sentiment_Analysis_icon.png")
    Sentiment_Analysis_ = Custom("Sentiment Analysis \n", "/content/sample_data/image_src/Sentiment_Analysis_icon.png")


    Text_Data_ >> Azure_Cognitive_Services_
    Azure_Cognitive_Services_ >> Sentiment_Analysis_
    Sentiment_Analysis_ >> Sentiment_Score_
    Sentiment_Score_ >> Positive_Negative_Result_
