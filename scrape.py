import json
from bs4 import BeautifulSoup
from bs4.element import Doctype, NavigableString

from load import parent
job_dict=dict()
with open('/mnt/c/Users/jacob/jh2/jobapptracker/job.json','r') as file:
    jobs_data=json.load(file)
    
    
  

file.close()

jl=1
for i in range(10):
    job_dict[str(i)]={}
    job_dict[str(i)]['link']=jobs_data['children'][0]['children'][jl]['children'][4]['children'][1]['children'][1]['children'][3]['children'][1]['children'][1]['children'][1]['children'][1]['children'][1]['children'][1]['attrs']['href']
    job_dict[str(i)]['company']=jobs_data['children'][0]['children'][jl]['children'][4]['children'][1]['children'][1]['children'][3]['children'][1]['children'][3]['children'][2]
    job_dict[str(i)]['title']=jobs_data['children'][0]['children'][jl]['children'][4]['children'][1]['children'][1]['children'][3]['children'][1]['children'][1]['children'][1]['children'][1]['children'][1]['children'][1]['children'][2]
    job_dict[str(i)]['location']=jobs_data['children'][0]['children'][jl]['children'][4]['children'][1]['children'][1]['children'][3]['children'][1]['children'][5]['children'][2]
    job_dict[str(i)]['date']=jobs_data['children'][0]['children'][jl]['children'][4]['children'][1]['children'][1]['children'][3]['children'][7]['children'][1]['children'][3]['children'][3]['children'][1]['children'][2]
    #children[0].children[1].children[4].children[1].children[1].children[3].children[1].children[1].children[1].children[1].children[1].children[1].children[2]
    #jchildren[0].children[1].children[4].children[1].children[1].children[3].children[1].children[3].children[2]
    #jchildren[0].children[5].children[4].children[1].children[1].children[3].children[1].children[3].children[2]
    jl+=4
#print(job_dict)


json_data=[]
for i in range(len(job_dict)):
    json_data.append(job_dict[str(i)])
with open('/mnt/c/Users/jacob/jh2/jobapptracker/in.json','w') as file:
    json.dump(json_data,file,indent=4)
    
    
  

file.close()