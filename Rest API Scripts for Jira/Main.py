import assignTasks as task
import getIssues as issue

#'MAIN' this is an a example. Most everything is hard coded. So when it runs it will assign all of the returned tasks to me 
if __name__ == "__main__":
        UserID = "5f45g9b6fdc3f5203t5e087c" #Andrew Wolfe
        ListOfIssues = issue.GetIssuesForCurrentNewHire()
        task.assingIssuesForNewHires(ListOfIssues,UserID)
