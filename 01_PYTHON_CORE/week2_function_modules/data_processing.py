def filter_by_city(dealer_list, city_name):
  filtered_list = [
    dealer for dealer in dealer_list
    if dealer["city"] == city_name
  ]
  
  return filtered_list