import json

script_dir = os.path.dirname(os.path.abspath(__file__))
json_file_path = os.path.join(script_dir, 'hotel_data.json')
with open(json_file_path, 'r') as f:
    hotel_data = json.load(f)


def find_cheapest_price(hotel_data):
    lowest_price = float('inf')
    
    
    for room_type, price in hotel_data['assignment_results'][0]["shown_price"].items():
        
        price_float = float(price)
        
      
        if price_float < lowest_price:
            
            lowest_price = price_float
            cheapest_room_type = room_type
    
    
    return cheapest_room_type, lowest_price

def find_cheapest_room(hotel_data):
    cheapest_room_type, cheapest_price = find_cheapest_price(hotel_data)
    
    
    for room_type, price in hotel_data['assignment_results'][0]['shown_price'].items():
        if float(price) == cheapest_price:
            
            return room_type, hotel_data['assignment_results'][0]['number_of_guests']

def calculate_total_price(hotel_data):
    total_price = 0.0
    
    
    for price in hotel_data['assignment_results'][0]['net_price'].values():
        total_price += float(price)
    
    
    taxes = json.loads(hotel_data['assignment_results'][0]['ext_data']['taxes'])
    
    
    for tax_value in taxes.values():
        total_price += float(tax_value)
    
    return total_price


with open('hotel_data.json', 'r') as f:
    hotel_data = json.load(f)

# cheapest price and room type
cheapest_room_type, cheapest_price = find_cheapest_price(hotel_data)
print(f'The cheapest price is ${cheapest_price:.2f} for the {cheapest_room_type} room type.')
# answer is $90.00 for the King Studio Suite-Non smoking type

# Find the room type and number of guests with the cheapest price
cheapest_room, num_guests = find_cheapest_room(hotel_data)
print(f'The cheapest room is the {cheapest_room} room, which accommodates {num_guests} guests.')
# answer is king Studio Suite-Non Smoking which accomodates 4 guests

# Calculate the total price (net price + taxes) for all rooms
total_price = calculate_total_price(hotel_data)
print(f'The total price (net price + taxes) for all rooms is ${total_price:.2f}.')
#total price is $430.86. N.B net  prices + taxes


# Output the results to a text file
with open('hotel_data_analysis.txt', 'w') as f:
    f.write(f'The cheapest price is ${cheapest_price:.2f} for the {cheapest_room_type} room type.' + '\n')
    f.write(f'The cheapest room is the {cheapest_room} room, which accommodates {num_guests} guests.' + '\n')
    f.write(f'The total price (net price + taxes) for all rooms is ${total_price:.2f}.' + '\n')
