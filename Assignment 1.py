mobile_data = {
    'status': True,
    'data': [
          {'name': 'Xiaomi Note 5', 'price': '300 USD', 'made': 'China'},
          {'name': 'Samsung Note 6', 'price': '200 USD', 'made': 'USA'},
          {'name': 'Iphone 5', 'price': '180.5 USD', 'made': 'Japan'},
          {'name': 'Pixel 5', 'price': '89.60 USD', 'made': 'Rusia'},
          {'name': 'Techno 5', 'price': '110 USD', 'made': 'Uk'},
          {'name': 'Huawei 5', 'price': '350 USD', 'made': 'Malaysia'},
            ],
    'exchnage_rate': 107.25
            }
# Xiaomi Note 5 is made in China. The price is 300 USD which is almost equal to 30975 BDT
# print(type(mobile_data))
# print(mobile_data.keys())
name = mobile_data.get('data')
brand_name=name[0]['name']
country = mobile_data.get('data')
made=country[0]['made']
pricedata = mobile_data.get('data')
price=pricedata[0]['price']
exchange = mobile_data.get('exchnage_rate')
tk = exchange * int(price[:3])
print(f'{brand_name} is made in {made}. The price is {price} which is almost equal to {tk}')
name1 = mobile_data.get('data')
brand_name1=name1[1]['name']
country1 = mobile_data.get('data')
made1=country1[1]['made']
pricedata1 = mobile_data.get('data')
price1=pricedata1[1]['price']
exchange1 = mobile_data.get('exchnage_rate')
tk1 = exchange1 * int(price1[:3])
print(f'{brand_name1} is made in {made1}. The price is {price1} which is almost equal to {tk1}')
name2 = mobile_data.get('data')
brand_name2=name2[2]['name']
country2 = mobile_data.get('data')
made2=country2[2]['made']
pricedata2 = mobile_data.get('data')
price2=pricedata[2]['price']
exchange2 = mobile_data.get('exchnage_rate')
tk2 = exchange2 * float(price2[:5])
print(f'{brand_name2} is made in {made2}. The price is {price2} which is almost equal to {tk2}')
name3 = mobile_data.get('data')
brand_name3=name3[3]['name']
country3 = mobile_data.get('data')
made3=country3[3]['made']
pricedata3 = mobile_data.get('data')
price3=pricedata3[3]['price']
exchange3 = mobile_data.get('exchnage_rate')
tk3 = exchange3 *float(price3[:5])
print(f'{brand_name3} is made in {made3}. The price is {price3} which is almost equal to {tk3}')
name4 = mobile_data.get('data')
brand_name4=name4[4]['name']
country4 = mobile_data.get('data')
made4=country4[4]['made']
pricedata4 = mobile_data.get('data')
price4=pricedata4[4]['price']
exchange4 = mobile_data.get('exchnage_rate')
tk4 = exchange4 * int(price4[:3])
print(f'{brand_name4} is made in {made4}. The price is {price4} which is almost equal to {tk4}')
name5 = mobile_data.get('data')
brand_name5=name5[5]['name']
country5 = mobile_data.get('data')
made5=country5[5]['made']
pricedata5 = mobile_data.get('data')
price5=pricedata5[5]['price']
exchange5 = mobile_data.get('exchnage_rate')
tk5 = exchange5 * int(price5[:3])
print(f'{brand_name5} is made in {made5}. The price is {price5} which is almost equal to {tk5}')