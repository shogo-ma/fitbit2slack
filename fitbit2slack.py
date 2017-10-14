#!/usr/bin/env python3
# coding: utf-8

import config
import fitbit
import datetime


def getYesterday():
    return datetime.datetime.now() - datetime.timedelta(days=1)


# fitbitからデータを取得する
def getDailyWeight():
    authd_client = fitbit.Fitbit(
        config.CLIENT_ID,
        config.CLIENT_SECRET,
        access_token=config.ACCESS_TOKEN,
        refresh_token=config.REFRESH_TOKEN,
        system=""
    )

    weight_data = authd_client.get_bodyweight(getYesterday())["weight"][0]

    return (
        weight_data["date"],
        weight_data["bmi"],
        weight_data["weight"]
    )


# slackに投稿する
def postSlack():
    pass


def main():
    date, bmi, weight = getDailyWeight()
    print(date, bmi, weight)


if __name__ == "__main__":
    main()
