import argparse
import re
import requests
from bs4 import BeautifulSoup
import urllib3

parser = argparse.ArgumentParser(description="A script to take mermaid script as input and generate architecture image")
parser.add_argument('-m', '--mermaid', type=str, required=True, help='mermaid scriprt')
parser.add_argument('-o', '--output', type=str, help='Output file to save the image.')
# parser.add_argument('-v', '--verbose', action='store_true', help='Enable verbose output.')
args = parser.parse_args()
content = args.mermaid


print(content)
mermaid_edges_text = re.findall(r'<div class=\\"mermaid\\">.*graph LR(.*?)</div>',content,re.DOTALL)
fullforms_dict = {}
fullforms = re.findall(r'(\D)\[(.*?)\]',mermaid_edges_text[0],re.MULTILINE)
for i in fullforms:
  fullforms_dict[i[0]] = i[1]
edges_text = ''
connections = re.findall(r'(\w)(?:\[.*?\])*\s-->\s(\w)',mermaid_edges_text[0],re.MULTILINE)
for i in connections:
  edges_text = edges_text + f"'{fullforms_dict[i[0]]}': '{fullforms_dict[i[1]]}',"
print(edges_text)




urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
folder_path = "/content/sample_data/image_src/"

if edges_text.strip()[-1]==',':
  edges_text = edges_text.strip()[:-1]
python_code = """
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
"""
services = re.findall(r"(['\"])(.*?)\1", edges_text)
services = list(set([match[1] for match in services]))
print(services)


cloud_platform = "AZURE"
prompt = f"""
From the following array of services, list out the services belonging to {cloud_platform}. Return only if it exactly matches against the {cloud_platform} services and list out the services, not belonging to {cloud_platform}.

{services}

Output lists should be strictly on python list format. List with the services belonging to {cloud_platform} must be returned with Variable name cloud and the other list to be returned with variable name noncloud

output example :
cloud = [Services belonging to {cloud_platform}]
noncloud = [Services not belonging to {cloud_platform}]
"""

response = get_completion(prompt)
print(response)
lists = re.findall(r'\[([^]]*)\]', response)
cloud = [item.strip().replace("'","") for item in lists[0].split(',')]
non_cloud = [item.strip().replace("'","") for item in lists[1].split(',')]
print(cloud)
print(non_cloud)


declarations = ''
for service in services:
    service_file_name = re.sub(r'[^a-zA-Z0-9]', '_', service)
    formatted_sname = r'' + ''.join([word + (' \\n' if i % 2 == 1 else ' ') for i, word in enumerate(service.split())])
    if service in cloud:
      img_srch_query = f"""{"icon of " + service + ' in ' + cloud_platform }"""
    else:
      img_srch_query = f"""{"transparent icon " + service }"""
    declarations += f"""\n    urlretrieve(get_image_urls("{img_srch_query}"), "{ folder_path + service_file_name +"_icon.png"}")\n{"    "}{service_file_name+"_"} = Custom("{formatted_sname}", "{ folder_path + service_file_name +"_icon.png"}")\n"""

python_code += declarations
# print(declarations)
# Split by comma followed by space, but not inside square brackets
connections = re.split(r',\s*(?![^\[]*\])', edges_text)
connections = [connection.replace("'","") for connection in connections]
connections = [connection.replace('"',"") for connection in connections]
connections = [connection.strip() for connection in connections]
connections = [connection.replace(", ",",") for connection in connections]
connections = [connection.replace(": ",":") for connection in connections]
connections = [connection.replace(" ","_") for connection in connections]
connections = [connection.replace(":","_ >> ") for connection in connections]
connections = [re.sub(r'[^a-zA-Z0-9_ >\[\],]', '_', connection) for connection in connections]
connections = [re.sub(r'\[([^\]]+)\]', lambda x: '[' + ', '.join([word.strip() + '_' for word in x.group(1).split(',')]) + ']', connection) for connection in connections]
connections = [connection + '_' for connection in connections]
connections = [connection.replace("]_","]") for connection in connections]
connections = [connection for connection in connections if "[]" and "none" not in connection]
arrows = "\n"
for connection in connections:
    arrows += "\n    " + connection

python_code += arrows
print(python_code)
