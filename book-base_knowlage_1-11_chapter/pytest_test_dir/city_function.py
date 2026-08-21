def city_function(city,country,population=""):
    
    if population:
        result=f"{city},{country} - population {population}"
    else:
        result=f"{city},{country}"

        
    return result.title()



