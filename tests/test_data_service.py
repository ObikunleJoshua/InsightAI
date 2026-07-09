import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )
)

from services.data_service import DataService

import pandas as pd


df = pd.DataFrame(
    {
        "Sales": [100, 200],
        "Profit": [20, 50],
        "Region": ["West", "East"],
    }
)


profile = DataService.profile_dataset(df)

print(profile)