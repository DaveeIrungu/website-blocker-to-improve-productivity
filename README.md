This website blocker is a python script that prevents users from accessing certain predefined websites during specified hours.
The script runs in the background.
It can improve productivity by allowing access to sites only during 'leisure hours'

# Running web_blocker script on Windows 7, 8, 10 #
1. Install python on Windows
2. Disable antivirus because they generally don't allow programs to modify the hosts file
3. Alternatively, allow permission to execute if antivirus prompts you
4. Double click web_blocker.pw to run as a background process
5. This script blocks Facebook and Instagram from 0800 hours to 1700 hours
6. Modify the hours in 'If' statement
7. Modify the website in the website_list while listing the URLs inside the kali braces [] 

# Automate script to run every time Windows starts #
1. Open task scheduler
2. On the General Option, find the 'Actions' tab and choose 'Create basic task' and name it 'Website Blocker'
3. Run with highest priviledges (IMPORTANT) as hosts file cannot be modified without admin priviledges
4. On 'Configure for' choose your current version of Windows (e.g. Windows 7)
5. On the Trigger Option, create new Trigger and Begin the task At Startup
6. On the Actions Option, choose 'Start a program' and browse to where 'web_blocker.pyw' is located and select the script
7. On the Conditions Option, uncheck 'Start the task only if the computer is on AC power'
8. Click OK and run the task you have just created
