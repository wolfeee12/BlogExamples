import requests
import json

def GetIssuesForCurrentNewHire(): 

	#This api call will return a json file with information based on the jql query
        
	url = "https://andrewWolfe.atlassian.net/rest/api/3/search"

        headers =
                {
                "Authorization": "Basic YXdvbGZlQGNyaXRpY2FsZGVzaWduLm5ldDpaMG5OR0szSHAyTVZ3ZHpHWUZ5NzI2RTU=",
                "Accept": "application/json",
                "Content-Type": "application/json"
                }

	
	#This jql statment looks for issues that are in the current project and have 'Text Example' as a substring. 
	query = {
                'jql': 'project = DEX AND text ~ "Text Example",
                 "fields": ["summary"]
                #This limits the information returned and makes it a lot easier to parse. it focuses on the summary (aka the name) of each issue
                }


	response = requests.request("GET",url,headers=headers,params=query) #GET 
	
	data = json.loads(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))) 
	
	listOfIssues = []
	#This loop gets the key of every issue from the json file that was returned using the api call
	for i in data["issues"]:
		listOfIssues.append(i["key"])
	
        return ListOfIssues




