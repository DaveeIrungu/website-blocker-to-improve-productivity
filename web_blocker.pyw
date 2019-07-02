import time
from datetime import datetime as dt

# Path to hosts file as a raw string with the 'r prefix'
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
# Path to temporal host, located on same directory
hosts_temp = "hosts"
redirect = "0.0.0.0"
website_list = ["facebook.com", "www.facebook.com", "instagram.com", "www.instagram.com"]
# Add/remove the websites to be blocked following this format, URL within quotes, separated by commas

while True:
    # Using the date time method, checks whether current time is between 8am and 4pm
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,
                                                                          17):
        # Check if lines already exist
        # 'r+' allows both reading and writing
        print("Working hours")
        with open(hosts_path, 'r+') as file:
            content = file.read()
            # Iterate through the website list
            for website in website_list:
                if website in content:
                    pass
                # If e.g. facebook.com is already in the website_list, it will pass
                # If website is present, it will write, as below:
                else:
                    file.write(redirect + " " + website + "\n")



    else:
        with open(hosts_path, 'r+') as file:
            # Use readline method instead that produces a list of all the lines in host file
            content = file.readlines()
            # file.seek(0) Places the cursor at the start of the line to enable truncate() method
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()

        print("Leisure hours")
    time.sleep(5)
# Update the time.sleep(x) where x is the number of second(s) intervals that the script will run in the background
