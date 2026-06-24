# CodeAlpha_Task2_StockPortfolioTracker

print("📊 Welcome to Stock Portfolio Tracker")

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 130,
    "MSFT": 320,
    "INFY": 150,
    "TCS": 360
}

portfolio = {}

while True:
    print("\nOptions:")
    print("1. Add Stock")
    print("2. View Portfolio")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        stock = input("Enter stock name: ").upper()

        if stock not in stock_prices:
            print("❌ Stock not available")
            continue

        try:
            qty = int(input("Enter quantity: "))
        except ValueError:
            print("⚠️ Invalid quantity")
            continue

        portfolio[stock] = portfolio.get(stock, 0) + qty
        print("✅ Stock added")

    elif choice == "2":
        total = 0
        print("\n📈 Portfolio Summary:")

        for stock, qty in portfolio.items():
            value = stock_prices[stock] * qty
            total += value
            print(f"{stock}: {qty} shares = ₹{value}")

        print("----------------------")
        print("💰 Total Investment:", total)

    elif choice == "3":
        print("👋 Exiting...")
        break

    else:
        print("❌ Invalid choice")