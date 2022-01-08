import datetime
import fitbit
import pandas as pd

FETCH_HEART_RATE_COUNT = 20


def get_latest_heart_rate(client: fitbit.Fitbit) -> pd.DataFrame:
    today = datetime.date.today()
    today_str = today.strftime("%Y-%m-%d")
    heart_rate = _get_heart_rate(client, date=today_str, detail_level="1sec")
    return heart_rate[-FETCH_HEART_RATE_COUNT:]


def _get_heart_rate(
    client: fitbit.Fitbit, date: str, detail_level: str
) -> pd.DataFrame:
    # heart rateを1[s]単位で取得してpandas DataFrameに変換する
    heart_rate_dict: dict = client.intraday_time_series(
        resource="activities/heart", base_date=date, detail_level=detail_level
    )["activities-heart-intraday"]["dataset"]
    heart_rate = pd.DataFrame.from_dict(heart_rate_dict)
    return heart_rate
