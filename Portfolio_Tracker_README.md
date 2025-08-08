# 📈 Stock Portfolio Tracker (Python Version)

## 📌 Description
This is a simple **Stock Portfolio Tracker** developed in Python for beginners to practice dictionaries, loops, basic arithmetic, and optional file handling. 
The program allows users to enter stock names and quantities, calculates the total investment value based on hardcoded stock prices, and optionally saves the result to a file.

## ✅ Features
- Hardcoded dictionary with stock prices.
- User inputs stock names and quantities.
- Calculates total investment value.
- Displays portfolio summary.
- Option to save results in a `.txt` file.

## 🔧 Technologies Used
- Python 3
- Concepts: `dictionary`, `input/output`, `basic arithmetic`, `file handling`

## ▶️ How to Run
1. Make sure Python is installed on your system.
2. Save the code in a file named `portfolio_tracker.py`.
3. Open a terminal or command prompt.
4. Run the script:

```
python portfolio_tracker.py
```

## 🖼️ Example Run

```
📈 Stock Portfolio Tracker
Available stocks and prices:
AAPL: $180
TSLA: $250
GOOGL: $140
MSFT: $330
AMZN: $130

Enter stock name (or 'done' to finish): AAPL
Enter quantity: 5
Enter stock name (or 'done' to finish): TSLA
Enter quantity: 2
Enter stock name (or 'done' to finish): done

Your Portfolio:
AAPL: 5 shares @ $180 each
TSLA: 2 shares @ $250 each

💰 Total Investment Value: $1400

Do you want to save the result to a file? (y/n): y
✅ Portfolio saved to portfolio.txt
```

## 📁 File Structure

```
portfolio_tracker/
├── portfolio_tracker.py
└── README.md
```

## 📚 Learning Concepts
- Working with dictionaries
- Performing arithmetic calculations
- Looping with `while`
- Validating user input
- Writing to files

## 💡 Future Improvements (Optional)
- Fetch real-time stock prices using an API.
- Support CSV file output.
- Track portfolio changes over time.