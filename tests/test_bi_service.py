import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

from services.bi_service import BusinessIntelligenceService
import pandas as pd

df = pd.DataFrame({
    "Sales": [100, 200, 300],
    "Profit": [20, 50, 70],
    "Region": ["West", "East", "West"],
    "Category": ["Tech", "Office", "Tech"]
})

kpis = BusinessIntelligenceService.generate_kpis(df)

print(kpis)