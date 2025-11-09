#import requests
#import time
#
#data = {"collection":[]}
#
#for i in range(6):
#    r = requests.get(url="http://api.open-notify.org/iss-now.json")# count params due to pagination. This works
#    print(r.status_code)
#    time.sleep(2)
#    
#    data['collection'].extend(r.json().get('collection', []))
#
#print(data)

import json

# Function to append new data to JSON file
def write_json(new_data, filename='iss.json'):
    with open(filename, 'r+') as file:
        # Load existing data into a dictionary
        file_data = json.load(file)
        
        # Append new data to the 'emp_details' list
        file_data["iss_position"].append(new_data)
        
        # Move the cursor to the beginning of the file
        file.seek(0)
        
        # Write the updated data back to the file
        json.dump(file_data, file, indent=4)

# New data to append
new_employee = {
    data
}

# Call the function to append data
write_json(new_employee)