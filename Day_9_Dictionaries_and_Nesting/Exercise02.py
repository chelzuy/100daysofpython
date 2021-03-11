
travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇

def add_new_country(name,visits_count,cities_visit):
    new_travel = {}
    new_travel["country"] = name,
    new_travel["visits"]  = visits_count,
    new_travel["cities"]  = cities_visit 
    travel_log.append(new_travel)


#🚨 Do not change the code below

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)

