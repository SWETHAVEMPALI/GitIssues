Solution:
Fetch user name and repository name from the input URL which is a link to a public github repository. 
Instantiate PyGithub(which is a python client for github api)
Using PyGithub invoke get_issues() with parameter state='open' for the given user and repository. This gives all open issues. In case of any github exception, display appropriate message. 
Use the 'since' parameter of get_issues() to get open issues updated in the last 24 hours. 
Similarly fetch the open issues updated in the last 7 days. 
Filter out the pull requests from the results of steps 3,4 and 5. This is because get_issues returns issues plus pull requests. 
Get the count of these 3 results. 
Subtraction of issues updated in the last 24 hours and last 7 days from the total open issues gives us the open issues updated before 7 days.
Render the results in an html table. 

Web application url:
https://swethawebapp2.herokuapp.com/

Improvements:
Add authentication mechanism while invoking github api
Cache the response
