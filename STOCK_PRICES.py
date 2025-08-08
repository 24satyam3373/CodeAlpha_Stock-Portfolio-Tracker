# Predefined stock prices
STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 130,
    "MSFT": 320,
    "INFY": 1450
}

def get_user_portfolio():  # Function to get user's stock portfolio
    portfolio = {}
    print(" Welcome to the Stock Portfolio Tracker!")
    print("Available Stocks:", ', '.join(STOCK_PRICES.keys()))

    while True:                
        stock = input("\nEnter stock symbol (or type 'done' to finish): ").upper()
        if stock == "DONE":
            break
        if stock not in STOCK_PRICES:
            print(" Invalid stock symbol. Please try again.")
            continue
        try:
            qty = int(input(f"Enter quantity for {stock}: "))
            if qty <= 0:
                print(" Quantity must be greater than zero.")
                continue
            portfolio[stock] = portfolio.get(stock, 0) + qty
        except ValueError:
            print(" Please enter a valid number.")
    
    return portfolio 

def display_portfolio(portfolio): # Function to display the user's portfolio
    total = 0
    summary = "\n Investment Summary\n"
    summary += "-" * 40 + "\n"
    summary += "{:<10} {:<10} {:<10}\n".format("Stock", "Qty", "Value")
    summary += "-" * 40 + "\n"

    for stock, qty in portfolio.items():
        price = STOCK_PRICES[stock]
        value = price * qty
        total += value
        summary += "{:<10} {:<10} {:<10}\n".format(stock, qty, value)

    summary += "-" * 40 + "\n"
    summary += f"Total Investment: ₹{total}\n"
    print(summary)
    return summary

def save_to_txt(content, filename="portfolio_summary.txt"):
    with open(filename, "w", encoding="utf-8") as file:
        file.write(content)
    print(f"Portfolio saved to '{filename}'")


def main():                            # Main function to run the portfolio tracker
    portfolio = get_user_portfolio()
    if not portfolio:
        print(" No stocks entered. Exiting.")
        return
    summary = display_portfolio(portfolio)

    save = input("\nDo you want to save the summary to a text file? (yes/no): ").lower()
    if save == 'yes':
        save_to_txt(summary)

if __name__ == "__main__":
    main()

