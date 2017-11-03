#/usr/bin/python
# -*- coding: utf-8 -*-

from math import floor
def clock_angle(time):
    hour, minute = time.split(":")
    ang_hour = int(hour) % 12 * 30 + int(minute) * 0.5
    ang_minute = int(minute) * 6
    angle = abs(ang_hour - ang_minute)
    if( angle > 180.0):
        angle = 360.0 - angle
    if angle - floor(angle) < 0.1:
        angle = int(angle)
    return angle


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert clock_angle("02:30") == 105, "02:30"
    assert clock_angle("13:42") == 159, "13:42"
    assert clock_angle("01:42") == 159, "01:42"
    assert clock_angle("01:43") == 153.5, "01:43"
    assert clock_angle("00:00") == 0, "Zero"
    assert clock_angle("12:01") == 5.5, "Little later"
    assert clock_angle("18:00") == 180, "Opposite"

    print("Now that you're finished, hit the 'Check' button to review your code and earn sweet rewards!")

