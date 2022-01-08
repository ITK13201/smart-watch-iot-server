import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import dates as mdates

from django.core.management.base import BaseCommand
from django.conf import settings

from fitbit_client.apiclient import FitbitApiClient


class Command(BaseCommand):
    help = "update fitbit token"

    def handle(self, *args, **options):
        TODAY = "2022-01-09"
        hr = self.get_heart_rate(date=TODAY, detail_level="1sec")
        print(hr[-20:])

        # ここからグラフ描画-------------------------------------
        # フォントの種類とサイズを設定する。
        plt.rcParams["font.size"] = 14
        plt.rcParams["font.family"] = "DejaVu Sans"

        # 目盛を内側にする。
        plt.rcParams["xtick.direction"] = "in"
        plt.rcParams["ytick.direction"] = "in"

        # グラフの上下左右に目盛線を付ける。
        fig = plt.figure()
        ax1 = fig.add_subplot(111)
        ax1.yaxis.set_ticks_position("both")
        ax1.xaxis.set_ticks_position("both")

        # 軸のラベルを設定する。
        ax1.set_xlabel("Time [h]")
        ax1.set_ylabel("Heart Rate [bpm]")

        # スケールの設定をする。
        ax1.xaxis.set_major_locator(mdates.HourLocator(byhour=range(0, 24, 6)))
        ax1.xaxis.set_major_formatter(mdates.DateFormatter("%H"))

        # データプロットの準備とともに、ラベルと線の太さ、凡例の設置を行う。
        ax1.plot(pd.to_datetime(hr["time"]), hr["value"], label=TODAY, lw=1)
        ax1.legend()

        # レイアウト設定
        fig.tight_layout()

        # グラフを表示する。
        plt.show()
        plt.savefig("/etc/backend/a.png")
        plt.close()

    def get_heart_rate(self, date, detail_level):
        client = FitbitApiClient().initial()
        # heart rateを1[s]単位で取得してpandas DataFrameに変換する
        hr = client.intraday_time_series(
            resource="activities/heart", base_date=date, detail_level=detail_level
        )["activities-heart-intraday"]["dataset"]
        hr = pd.DataFrame.from_dict(hr)
        return hr
