def tracePath(city_map):
    # Step 1: Identify the starting city
    departures = set(city_map.keys())
    arrivals = set(city_map.values())
    
    # The start city is the one that is not an arrival city
    start_city = (departures - arrivals).pop()
    
    # Step 2: Trace the complete path
    path = []
    current_city = start_city
    
    while current_city in city_map:
        next_city = city_map[current_city]
        path.append(f"{current_city}-{next_city}")
        current_city = next_city
    
    # Step 3: Return the complete path as a string
    return ', '.join(path)

# Example usage:
city_map = {
    "NewYork": "Chicago",
    "Boston": "Texas",
    "Texas": "Missouri",
    "Missouri": "NewYork"
}

print(tracePath(city_map))  # Output: "Boston-Texas, Texas-Missouri, Missouri-NewYork, NewYork-Chicago"
