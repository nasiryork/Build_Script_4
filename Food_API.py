#!"C:\Users\Nasir York\AppData\Local\Programs\Python\Python39\python.exe"
#Script only works for US Resturants

import requests
import csv

food_choice = str(input("What type of food are you in the mood for?: "))
city = str(input("What city in the United States would you like to search?: "))

bearer_t = "mJuGey_iBLNN43Em9qVDBUo3wtrdHg8dDit9cOxlEHP58ao3PfCvqZhoMokWp86f4imhoI9UTLOdwg2Kae2Fm_o1BYqMXs8C8E4C3OFq3TfJOyae7PySVHJidaMcY3Yx"
endpoint = "https://api.yelp.com/v3/businesses/search?location="+city+"&categories="+str.lower(food_choice)
#endpoint = "https://api.yelp.com/v3/businesses/search?location="+city+"&categories="+str.lower(food_choice)
key = {'Authorization': 'bearer %s' % bearer_t}

response = requests.request("GET", endpoint,headers=key,data={})
yelp_data = response.json()
#print(response)
#print(yelp_data)
build_script_data = []
csvheader = ['Name','Price','Rating','Phone Number','Review Count','Closed?','Website']

#testpath = 'C:/Users/Nasir York/Desktop/Kura Scripts/Python Scripts/API/Testyelp'+'_'+city+'_'+food_choice+'.txt'
#testpath2 = 'C:/Users/Nasir York/Desktop/Kura Scripts/Python Scripts/API/Testyelp2'+'_'+city+'_'+food_choice+'.txt'
csvpath = 'C:/Users/Nasir York/Desktop/Kura Scripts/Python Scripts/API/yelp'+'_'+city+'_'+food_choice+'.csv'

#f = open(testpath, 'w')
#f.write(json.dumps(yelp_data, indent = 3))
#f.close()

for x in yelp_data['businesses']:
  restaurant = [x['name'],x['price'],x['rating'],x['display_phone'],x['review_count'],x['is_closed'],x['url']]
  build_script_data.append(restaurant)

#f = open(testpath2, 'w')
#f.write(json.dumps(build_script_data, indent = 3))
#f.close()

with open(csvpath, 'w', newline='') as f:
  write = csv.writer(f)

  write.writerow(csvheader)
  write.writerows(build_script_data)  

print('Csv Created')
