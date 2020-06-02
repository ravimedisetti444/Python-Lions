import json

data = '''
{
   "results" : [
      {
         "access_points" : [],
         "address_components" : [
            {
               "long_name" : "India",
               "short_name" : "IN",
               "types" : [ "country", "political" ]
            }
         ],
         "formatted_address" : "India",
         "geometry" : {
            "bounds" : {
               "northeast" : {
                  "lat" : 35.513327,
                  "lng" : 97.39535869999999
               },
               "southwest" : {
                  "lat" : 6.4626999,
                  "lng" : 68.1097
               }
            },
            "location" : {
               "lat" : 20.593684,
               "lng" : 78.96288
            },
            "location_type" : "APPROXIMATE",
            "viewport" : {
               "northeast" : {
                  "lat" : 35.513327,
                  "lng" : 97.39535869999999
               },
               "southwest" : {
                  "lat" : 6.4626999,
                  "lng" : 68.1097
               }
            }
         },
         "place_id" : "ChIJkbeSa_BfYzARphNChaFPjNc",
         "types" : [ "country", "political" ]
      }
   ],
   "status" : "OK"
}
'''

lst =list()
lst1=list()
info = json.loads(data)
#print('Name:', info["types"])
#print('Hide:', info["place_id"])
lst=info["results"]
#print(lst)
for item in lst:
    lst1=item.get('geometry',0)
    for k in lst1:
        if(k=='location'):
            print('latitude',lst1[k].get('lat',0))
            print('longitude',lst1[k].get('lng',0))
