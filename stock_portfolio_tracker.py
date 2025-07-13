# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 2800,
    "MSFT": 350,
    "AMZN": 140
}

# Dictionary to store user portfolio
portfolio = {}

print("📊 Welcome to the Stock Portfolio Tracker 📊")
print("Available stocks:", ", ".join(stock_prices.keys()))

# User input loop
while True:
    stock = input("\nEnter stock symbol (or type 'done' to finish): ").upper()
    
    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("⚠️ Stock not found. Please choose from the available list.")
        continue

    try:
        quantity = int(input(f"Enter quantity of {stock} shares: "))
        if quantity < 0:
            raise ValueError
        portfolio[stock] = portfolio.get(stock, 0) + quantity
    except ValueError:
        print("⚠️ Please enter a valid positive integer for quantity.")

# Calculate total investment
total_value = 0
print("\n📈 Portfolio Summary:")
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    value = price * qty
    total_value += value
    print(f"{stock}: {qty} shares × ${price} = ${value}")

print(f"\n💰 Total Investment Value: ${total_value}")

# Optional: Save to a file
save = input("Do you want to save the result to a file? (y/n): ").lower()
if save == 'y':
    with open("portfolio_summary.txt", "w") as file:
        file.write("Stock Portfolio Summary\n")
        file.write("------------------------\n")
        for stock, qty in portfolio.items():
            price = stock_prices[stock]
            value = price * qty
            file.write(f"{stock}: {qty} shares × ${price} = ${value}\n")
        file.write(f"\nTotal Investment Value: ${total_value}\n")
    print("📁 Portfolio saved to 'portfolio_summary.txt'")
