from random import randint

sales_data = {
    "hours": [
        "6am",
        "7am",
        "8am",
        "9am",
        "10am",
        "11am",
        "12pm",
        "1pm",
        "2pm",
        "3pm",
        "4pm",
        "5pm",
        "6pm",
        "7pm",
    ],
    "stands": [
        {
            "id": 1,
            "location": "Seattle",
            "totalDailyCookies": 654,
            "cookiesEachHour": [
                6,
                7,
                8,
                9,
                10,
                11,
                12,
                1,
                2,
                3,
                4,
                5,
                6,
                7,
            ],
        },
        {
            "id": 2,
            "location": "Amman",
            "totalDailyCookies": 654,
            "cookiesEachHour": [
                6,
                7,
                8,
                9,
                10,
                11,
                12,
                1,
                2,
                3,
                4,
                5,
                6,
                7,
            ],
        },
        {
            "id": 3,
            "location": "Portland",
            "totalDailyCookies": 654,
            "cookiesEachHour": [
                6,
                7,
                8,
                9,
                10,
                11,
                12,
                1,
                2,
                3,
                4,
                5,
                6,
                7,
            ],
        },
    ],
}


def calculate_hourly_totals(stands):
    totals = []
    for index, _ in enumerate(sales_data["hours"]):
        cross_stand_hourly_sales = 0
        for stand in stands:
            cross_stand_hourly_sales += stand["cookiesEachHour"][index]

        totals.append(cross_stand_hourly_sales)

    return totals + [sum(totals)]
