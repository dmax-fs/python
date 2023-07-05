hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

total_price = 0
for i in prices:
  total_price += i

average_price = (total_price/len(prices))
print("Average Haircut Price: " + str(average_price))

new_prices = [j - 5 for j in prices]
print(new_prices)

total_revenue = 0
for k in range(len(hairstyles)):
  total_revenue += prices[k] * last_week[k]
  print("Total Revenue: " + str(total_revenue))

average_daily_revenue = [total_revenue/7]
print("Average Daily Revenue: " + str(average_daily_revenue))

cuts_under_30 = [hairstyles[m] for m in range(len(new_prices) - 1) if new_prices[m] < 30]
print(cuts_under_30)