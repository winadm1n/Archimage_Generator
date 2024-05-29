
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

    urlretrieve(get_image_urls("icon of azure cloud functions in AZURE"), "/home/runner/work/Archimage_Generator/Archimage_Generator/Architecture_images/temp_src_imagesazure_cloud_functions_icon.png")
    azure_cloud_functions_ = Custom("azure cloud \nfunctions ", "/home/runner/work/Archimage_Generator/Archimage_Generator/Architecture_images/temp_src_imagesazure_cloud_functions_icon.png")

    urlretrieve(get_image_urls("icon of Azure Cognitive Services in AZURE"), "/home/runner/work/Archimage_Generator/Archimage_Generator/Architecture_images/temp_src_imagesAzure_Cognitive_Services_icon.png")
    Azure_Cognitive_Services_ = Custom("Azure Cognitive \nServices ", "/home/runner/work/Archimage_Generator/Archimage_Generator/Architecture_images/temp_src_imagesAzure_Cognitive_Services_icon.png")

    urlretrieve(get_image_urls("icon of Positive/Negative Result in AZURE"), "/home/runner/work/Archimage_Generator/Archimage_Generator/Architecture_images/temp_src_imagesPositive_Negative_Result_icon.png")
    Positive_Negative_Result_ = Custom("Positive/Negative Result \n", "/home/runner/work/Archimage_Generator/Archimage_Generator/Architecture_images/temp_src_imagesPositive_Negative_Result_icon.png")

    urlretrieve(get_image_urls("icon of Sentiment Score in AZURE"), "/home/runner/work/Archimage_Generator/Archimage_Generator/Architecture_images/temp_src_imagesSentiment_Score_icon.png")
    Sentiment_Score_ = Custom("Sentiment Score \n", "/home/runner/work/Archimage_Generator/Archimage_Generator/Architecture_images/temp_src_imagesSentiment_Score_icon.png")

    urlretrieve(get_image_urls("icon of Sentiment Analysis in AZURE"), "/home/runner/work/Archimage_Generator/Archimage_Generator/Architecture_images/temp_src_imagesSentiment_Analysis_icon.png")
    Sentiment_Analysis_ = Custom("Sentiment Analysis \n", "/home/runner/work/Archimage_Generator/Archimage_Generator/Architecture_images/temp_src_imagesSentiment_Analysis_icon.png")


    azure_cloud_functions_ >> Azure_Cognitive_Services_
    Azure_Cognitive_Services_ >> Sentiment_Analysis_
    Sentiment_Analysis_ >> Sentiment_Score_
    Sentiment_Score_ >> Positive_Negative_Result_