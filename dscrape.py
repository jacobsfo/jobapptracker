import json
from bs4 import BeautifulSoup
from bs4.element import Doctype, NavigableString

from load import parent
job_dict=dict()

with open('/mnt/c/Users/jacob/jh2/jobapptracker/dice.json','r') as file:
    jobs_data=json.load(file)
    
file.close()    
#children[0].children[14].children[1].children[1].children[8].children[2].text
test_path="children[0].children[12].children[1].children[1].children[8].children[9].text"
#company=get_value_from_json(comp_path)
test_child=test_path.replace('children',"['children']")
py=test_child.replace('.','')
pys=py.replace('text',"['text']")
print(pys)
#children[0].children[0].children[0].children[0].children[0].children[0].children[0].children[1].children[1].children[1]
#convert children to ['children']
#remove periods
jl=12
for i in range(10):
    #children[0].children[12].children[1].children[1].children[8].children[6].text
    job_dict[str(i)]={}
    #print(jobs_data['children'][0]['children'][jl]['children'][1]['children'][1]['children'][8]['children'][9]['text'])

    job_dict[str(i)]['link']='dice'
    job_dict[str(i)]['company']=jobs_data['children'][0]['children'][jl]['children'][1]['children'][1]['children'][8]['children'][2]['text']
    job_dict[str(i)]['title']=jobs_data['children'][0]['children'][jl]['children'][1]['children'][1]['children'][2]['text']
    job_dict[str(i)]['location']=jobs_data['children'][0]['children'][jl]['children'][1]['children'][1]['children'][8]['children'][6]['text']
    job_dict[str(i)]['date']=jobs_data['children'][0]['children'][jl]['children'][1]['children'][1]['children'][8]['children'][9]['text']
    #children[0].children[1].children[4].children[1].children[1].children[3].children[1].children[1].children[1].children[1].children[1].children[1].children[2]
    #jchildren[0].children[1].children[4].children[1].children[1].children[3].children[1].children[3].children[2]
    #jchildren[0].children[5].children[4].children[1].children[1].children[3].children[1].children[3].children[2]
    jl+=2
print(job_dict)


json_data=[]
for i in range(len(job_dict)):
    json_data.append(job_dict[str(i)])
with open('/mnt/c/Users/jacob/jh2/jobapptracker/dice_in.json','w') as file1:
    json.dump(json_data,file1,indent=4)
    
    
  

# file1.close()
