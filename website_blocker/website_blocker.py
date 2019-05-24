'''
This Python script disable the access to the webistes of your preferences
for an interval of time (through the hosts file), increasing in this way your productivity at work
avoiding the distractions.
'''
import time
from datetime import datetime as dt

# Setting the hosts file path
hosts_path = "hosts"
hosts_path = "/etc/hosts"


# Setting the IP address where the browser will be redirected
# when we'll try to access the websites to avoid
redirect = "127.0.0.1"

# List of websites to block
website_list = ["www.facebook.com", "facebook.com"]

# Adding the website list into the hosts file at 08.00
# and them will be removed at 17.00
while True:
    '''Checking the current time against 08.00 and 16.00 to modify the hosts file'''
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 17):
        print("Working hours...")

        ''' Checking if the website list is present in the hosts temp file.
            If not, add it.'''
        with open(hosts_path, "r+") as hosts_tmp_file:
            content = hosts_tmp_file.read()
            print(content)

            for website in website_list:
                if website in content:
                    pass
                else:
                    hosts_tmp_file.write("\n")
                    hosts_tmp_file.write("{}   {}".format(redirect, website))
                    print(content)
    else:
        print("Fun hours...")

        '''Removing from the hosts temp file the websites blocked'''
        with open(hosts_path, "r+") as hosts_tmp_file:
            content = hosts_tmp_file.readlines()
            hosts_tmp_file.seek(0)
            hosts_tmp_file.truncate()
            print(content)

            for line in content:
                if not any (website in line for website in website_list):
                    hosts_tmp_file.write(line)

    time.sleep(5) # 60 seconds = 1 minute