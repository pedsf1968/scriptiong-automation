import json 
req_file="D:\\DATA-DEV\\python\\scripting-automation\\16-json\\example2.json"

# The Python dictionnary is the equivalent of JSON object
my_dict={
    'Name':'PEDSF',
    'skills':{
        'Cloud': ['AWS','Azure'],
        'Orchestration': ['Kubernetes','Swarm'],
        'Application Lifecycle Management': ['Jira','Trello'],
        'SCM/VCS': ['Git','GitHub','GitLab','Bitbucket'],
        'CI': ['Jenkins','Travis CI'],
        'Build': ['Maven'],
        'languages': ['Java','Python','shell','yaml'],
        'Provisionning': ['Ansible','Terraform','Vagrant'],
        'Artefact Management': ['DockerHub'],
        'Knowledge Sharing': ['Confluence','OpenAPI'],
        'Testing': ['Cucumber', 'JUnit'],
        'BI / Monitoring / Logging': ['Prometheus', 'Grafana','Elasticsearch']
        }
}

# Push data in file
fo=open(req_file,'w')
json.dump(my_dict,fo,indent=4)
fo.close()
