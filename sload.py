from bs4 import BeautifulSoup
import json
from bs4.element import Doctype, NavigableString
parent='/mnt/c/Users/jacob/jh2/jobapptracker'
def html_to_json(tag):
    if not tag:
        return None
    if isinstance(tag, slice):
        return {
            
        }
    if isinstance(tag, Doctype):
        return {
            "type": "doctype",
            "name": tag.name,
        }
    if isinstance(tag, NavigableString):
        return str(tag)
    return {
        "tag": tag.name,
        "attrs": dict(tag.attrs),
        "text": tag.string,
        "children": [html_to_json(child) for child in tag.children]
    }

# Open and read the HTML file
with open('/mnt/c/Users/jacob/jh2/jobapptracker/simp.html', 'r') as file:
    html_content = file.read()

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')


# Convert the BeautifulSoup object to a JSON string
json_content = json.dumps(html_to_json(soup), indent=4)


file.close()

with open(parent +'/simp.json','w') as file:
    file.write(json_content)
    
    
  

file.close()