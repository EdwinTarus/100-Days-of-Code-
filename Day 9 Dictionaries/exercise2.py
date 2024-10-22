travel_log = [
    {
        "country" : "France",
        "cities_visited" : ["Monaco", "Lille", "Strasbourg"],
        "total_visits" : 12
    },
    {
        "country" : "Germany",
        "cities_visited" : ["Munchen", "Nunberb", "Hamberg"],
        "total_visits": 10

    }
]

def vacation(nation, cities, visits):

    
    new_country = {"country" : nation,
               "cities_visited" : cities,
               "total_visits" : visits}
    travel_log.append(new_country)
    print(travel_log)

vacation("Russia", ["Moscow", "St. Petersburg"], 2)

for i in travel_log:
    print(i)
 