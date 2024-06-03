
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
with Diagram("Architecture_images/architecture", show=False):
    urlretrieve(get_image_urls("icon of Logic App in AZURE"), "/home/runner/work/Archimage_Generator/Archimage_Generator/dynamically_generated_stuff/temp_src_images/Logic_App_icon.png")
    Logic_App_ = Custom("Logic App \n", "/home/runner/work/Archimage_Generator/Archimage_Generator/dynamically_generated_stuff/temp_src_images/Logic_App_icon.png")

    urlretrieve(get_image_urls("icon of Appointment Booking in AZURE"), "/home/runner/work/Archimage_Generator/Archimage_Generator/dynamically_generated_stuff/temp_src_images/Appointment_Booking_icon.png")
    Appointment_Booking_ = Custom("Appointment Booking \n", "/home/runner/work/Archimage_Generator/Archimage_Generator/dynamically_generated_stuff/temp_src_images/Appointment_Booking_icon.png")

    urlretrieve(get_image_urls("icon of Chatbot in AZURE"), "/home/runner/work/Archimage_Generator/Archimage_Generator/dynamically_generated_stuff/temp_src_images/Chatbot_icon.png")
    Chatbot_ = Custom("Chatbot ", "/home/runner/work/Archimage_Generator/Archimage_Generator/dynamically_generated_stuff/temp_src_images/Chatbot_icon.png")

    urlretrieve(get_image_urls("icon of Dataset Storage in AZURE"), "/home/runner/work/Archimage_Generator/Archimage_Generator/dynamically_generated_stuff/temp_src_images/Dataset_Storage_icon.png")
    Dataset_Storage_ = Custom("Dataset Storage \n", "/home/runner/work/Archimage_Generator/Archimage_Generator/dynamically_generated_stuff/temp_src_images/Dataset_Storage_icon.png")

    urlretrieve(get_image_urls("icon of App Service in AZURE"), "/home/runner/work/Archimage_Generator/Archimage_Generator/dynamically_generated_stuff/temp_src_images/App_Service_icon.png")
    App_Service_ = Custom("App Service \n", "/home/runner/work/Archimage_Generator/Archimage_Generator/dynamically_generated_stuff/temp_src_images/App_Service_icon.png")

    urlretrieve(get_image_urls("icon of Functions in AZURE"), "/home/runner/work/Archimage_Generator/Archimage_Generator/dynamically_generated_stuff/temp_src_images/Functions_icon.png")
    Functions_ = Custom("Functions ", "/home/runner/work/Archimage_Generator/Archimage_Generator/dynamically_generated_stuff/temp_src_images/Functions_icon.png")

    urlretrieve(get_image_urls("icon of Web App in AZURE"), "/home/runner/work/Archimage_Generator/Archimage_Generator/dynamically_generated_stuff/temp_src_images/Web_App_icon.png")
    Web_App_ = Custom("Web App \n", "/home/runner/work/Archimage_Generator/Archimage_Generator/dynamically_generated_stuff/temp_src_images/Web_App_icon.png")

    urlretrieve(get_image_urls("icon of Storage Account in AZURE"), "/home/runner/work/Archimage_Generator/Archimage_Generator/dynamically_generated_stuff/temp_src_images/Storage_Account_icon.png")
    Storage_Account_ = Custom("Storage Account \n", "/home/runner/work/Archimage_Generator/Archimage_Generator/dynamically_generated_stuff/temp_src_images/Storage_Account_icon.png")

    urlretrieve(get_image_urls("icon of SQL Database in AZURE"), "/home/runner/work/Archimage_Generator/Archimage_Generator/dynamically_generated_stuff/temp_src_images/SQL_Database_icon.png")
    SQL_Database_ = Custom("SQL Database \n", "/home/runner/work/Archimage_Generator/Archimage_Generator/dynamically_generated_stuff/temp_src_images/SQL_Database_icon.png")

    urlretrieve(get_image_urls("icon of API Management in AZURE"), "/home/runner/work/Archimage_Generator/Archimage_Generator/dynamically_generated_stuff/temp_src_images/API_Management_icon.png")
    API_Management_ = Custom("API Management \n", "/home/runner/work/Archimage_Generator/Archimage_Generator/dynamically_generated_stuff/temp_src_images/API_Management_icon.png")

    urlretrieve(get_image_urls("icon of Remote Care Services in AZURE"), "/home/runner/work/Archimage_Generator/Archimage_Generator/dynamically_generated_stuff/temp_src_images/Remote_Care_Services_icon.png")
    Remote_Care_Services_ = Custom("Remote Care \nServices ", "/home/runner/work/Archimage_Generator/Archimage_Generator/dynamically_generated_stuff/temp_src_images/Remote_Care_Services_icon.png")

    urlretrieve(get_image_urls("icon of Data Transfer in AZURE"), "/home/runner/work/Archimage_Generator/Archimage_Generator/dynamically_generated_stuff/temp_src_images/Data_Transfer_icon.png")
    Data_Transfer_ = Custom("Data Transfer \n", "/home/runner/work/Archimage_Generator/Archimage_Generator/dynamically_generated_stuff/temp_src_images/Data_Transfer_icon.png")


    Web_App_ >> API_Management_
    App_Service_ >> Logic_App_
    App_Service_ >> Functions_
    App_Service_ >> Storage_Account_
    App_Service_ >> SQL_Database_
    Remote_Care_Services_ >> Logic_App_
    Appointment_Booking_ >> Functions_
    Dataset_Storage_ >> Storage_Account_
    Data_Transfer_ >> Storage_Account_
    Chatbot_ >> SQL_Database_
    API_Management_ >> App_Service_