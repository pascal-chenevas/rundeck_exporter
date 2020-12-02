#!/usr/bin/python3
import time
import datetime
from datetime import datetime
import re

class DateTimeRange:

    def assert_format(self, datetime_range):
        "format checker 2020-01-10 hh:mm:ss,2020-01-10 hh:mm:ss"
        pattern = re.compile("^([0-9]{4}\-[0-9]{2}\-[0-9]{2} [0-9]{1,2}\:[0-9]{1,2}\:[0-9]{1,2},?){2}$")

        if not pattern.fullmatch(datetime_range):
                raise Exception("Invalid range format! Given: " + self.datetime_range + " , want: yyyy-mmm-dd hh:mm:ss,yyyy-mm-dd hh:mm:ss")

    def extract_range(self, datetime_range):
        range_values = datetime_range.split(",")
        from_dateTime = range_values[0]
        to_dateTime = range_values[1]

        return from_dateTime, to_dateTime

    def assert_datetime(self, dt):
        try:
            datetime.strptime(dt,"%Y-%m-%d %H:%M:%S")
        except ValueError as err:
            raise Exception(dt + " is invalid")

    def to_timestamp(self, dateTime):
        dt = datetime.strptime(dateTime, "%Y-%m-%d %H:%M:%S")
        return int(datetime.timestamp(dt))

    def assert_range(self, datetime_range):
        self.assert_format(datetime_range)
        dt_from, dt_to = self.extract_range(datetime_range)
        self.assert_datetime(dt_from)
        self.assert_datetime(dt_to)

    def get_last_24_hours_range(self):
        now = datetime.now()
        today = now.strftime("%Y-%m-%d %H:%M:%S")


    def range_to_timestamp(self, datetime_range):
        dtr = datetime_range.rstrip(",")
        self.assert_range(dtr)
        dt_from, dt_to = self.extract_range(dtr)

        timestamp_from = self.to_timestamp(dt_from)
        timestamp_to = self.to_timestamp(dt_to)

        dt_to_timestamp = dict()
        dt_to_timestamp['from'] = timestamp_from
        dt_to_timestamp['to'] = timestamp_to

        if timestamp_to < timestamp_from:
            dt_to_timestamp['from'] = timestamp_to
            dt_to_timestamp['to'] = timestamp_from

        return dt_to_timestamp
