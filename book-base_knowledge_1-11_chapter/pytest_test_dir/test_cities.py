from city_function import city_function



def test_ciyt_country():
    formatted_str=city_function('dalian','china')
    assert formatted_str=='Dalian,China'

def test_city_country_population():
    formatted_str=city_function('dalian','china','700million')
    assert formatted_str=='Dalian,China - Population 700Million'