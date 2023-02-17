import datetime


def is_report_range_valid(date_from: datetime.date, date_to: datetime.date) -> bool:
    return date_to <= date_from

if __name__ == "__main__":
    date_1 = datetime.date(2022,1,1)
    date_2 = datetime.date(2022,12,31)
    assert is_report_range_valid(date_2, date_1)
