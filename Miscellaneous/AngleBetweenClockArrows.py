# Get the absolute angle (deg) between clock hour and minute arrows #


def get_hourAngle(hour):
    return hour*30


def get_minuteAngle(minute):
    return minute*6


def get_angle_between_arrows(hour, minute):
    return print(abs(get_hourAngle(hour) - get_minuteAngle(minute)), "degrees")


hour = 2
minute = 15
get_angle_between_arrows(hour, minute)
