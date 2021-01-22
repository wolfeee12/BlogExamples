import requests
import json


#This project takes the list of tasks and the ID of the someone and assigns the tasks to them	
def assingIssuesForNewHires(listOfTasks, UserID):

        headers =
        {
        "Authorization": "Basic YXdvbGZlQGNyaXRpY2FsZGVzaWduLm5ldDpaMG5OR0szSHAyTVZ3ZHpHWUZ5NzI2RTU=",
        "Accept": "application/json",
        "Content-Type": "application/json"
        }

	payload = json.dumps( {
	  "accountId": UserID
	} )
	
	#For each task assign it to the new hire
	for task in listOfTasks:
		url = "https://andrewWolfe.atlassian.net/rest/api/3/issue/{}/assignee".format(task)
		response = requests.request("PUT",url,data=payload,headers=headers,) #PUT
	
