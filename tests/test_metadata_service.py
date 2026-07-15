import pandas as pd

from services.metadata_service import MetadataService


def test_metadata_service():

    df = pd.DataFrame(
        {
            "Sales": [100, 200],
            "Profit": [20, 50],
            "Region": ["West", "East"],
        }
    )

    metadata = MetadataService.build(df)

    assert metadata["dataset_info"]["rows"] == 2
    assert metadata["dataset_info"]["columns"] == 3
    assert metadata["quality"]["score"] == 100
    assert len(metadata["capabilities"]["numeric_columns"]) == 2