from agent import ask_agent

result = ask_agent(
    "What business insights can be drawn?",
    """
Rows: 9994
Columns: 21
Column Names:
Sales, Profit, Region, Category
"""
)

print(result)