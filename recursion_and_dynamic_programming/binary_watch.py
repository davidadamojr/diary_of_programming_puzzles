"""
A binary watch has 4 LEDs on the top which represent the hours (0-11), and the 6 LEDs on the bottom represent the
minutes (0-59).

Each LED represents a zero or one, with the least significant bit on the right.

Image: https://upload.wikimedia.org/wikipedia/commons/8/8b/Binary_clock_samui_moon.jpg

For example, the watch in the image reads "3:25".

Given a non-negative integer n which represents the number of LEDs that are currently on, return all possible times the
watch could represent.

Example:

Input: n = 1
Return:
"""


# @param num the number of LEDS that are currently on
# @return list all possible times the watch could representt
def read_binary_watch(num):
    """Given a number of LEDs, generate all combinations of that number of LEDs"""

    led_dict = {
        0: 8,
        1: 4,
        2: 2,
        3: 1,
        4: 32,
        5: 16,
        6: 8,
        7: 4,
        8: 2,
        9: 1
    }

    if num == 0:
        return ["0:00"]

    leds = "0123456789"
    combinations = []

    def make_combinations(combination, leds):
        if len(combination) == num:
            combinations.append(combination)
            return

        for i in range(0, len(leds)):
            combination = combination + leds[i]
            make_combinations(combination, leds[i + 1:])
            combination = combination[:-1]

    make_combinations("", leds)

    possible_times = []
    for combination in combinations:
        hours = 0
        minutes = 0
        for digit in combination:
            if int(digit) < 4:
                hours = hours + led_dict[int(digit)]
            else:
                minutes = minutes + led_dict[int(digit)]

        if hours < 12 and minutes < 60:
            possible_times.append("{}:{}".format(str(hours), str(minutes).zfill(2)))

    return possible_times


if __name__ == "__main__":
    assert read_binary_watch(0) == ["0:00"]
    assert read_binary_watch(2) == ["10:00", "9:00", "8:32", "8:16", "8:08", "8:04", "8:02", "8:01", "6:00", "5:00",
                                    "4:32", "4:16", "4:08", "4:04", "4:02", "4:01", "3:00", "2:32", "2:16", "2:08",
                                    "2:04", "2:02", "2:01", "1:32", "1:16", "1:08", "1:04", "1:02", "1:01", "0:48",
                                    "0:40", "0:36", "0:34", "0:33", "0:24", "0:20", "0:18", "0:17", "0:12", "0:10",
                                    "0:09", "0:06", "0:05", "0:03"]
    print("All test cases passed.")
