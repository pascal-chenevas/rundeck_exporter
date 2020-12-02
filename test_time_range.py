#!/usr/bin/python3
import datetime_range

if __name__ == "__main__":
    t = datetime_range.DateTimeRange()
    dtr = "2020-01-10 10:10:30,2020-01-10 10:10:30,"

    print(dtr + " == " , t.range_to_timestamp(dtr))

    dtr = "2022-01-10 09:10:30,2020-01-10 10:10:30,"
    t_from, t_to = t.range_to_timestamp(dtr)
 
    print(dtr + " == " , t.range_to_timestamp(dtr))
