import time
from datetime import datetime

# get the seconds            since Jan 1 1970
current_time_seconds = time.time()

# format the sring  
formatted_time = "Seconds since January 1, 1970: {:.4f} or {:.2e} in scientific notation".format(current_time_seconds, current_time_seconds)

#get the date
current_date = datetime.now().strftime("%b %d %Y")

# print the text
print(formatted_time)
print(current_date)
