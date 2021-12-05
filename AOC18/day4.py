import datetime
import re
from collections import defaultdict
from collections import Counter

TEST_DATA = [
    '[1518-11-01 00:00] Guard #10 begins shift',
    '[1518-11-01 00:05] falls asleep',
    '[1518-11-01 00:25] wakes up',
    '[1518-11-01 00:30] falls asleep',
    '[1518-11-01 00:55] wakes up',
    '[1518-11-01 23:58] Guard #99 begins shift',
    '[1518-11-02 00:40] falls asleep',
    '[1518-11-02 00:50] wakes up',
    '[1518-11-03 00:05] Guard #10 begins shift',
    '[1518-11-03 00:24] falls asleep',
    '[1518-11-03 00:29] wakes up',
    '[1518-11-04 00:02] Guard #99 begins shift',
    '[1518-11-04 00:36] falls asleep',
    '[1518-11-04 00:46] wakes up',
    '[1518-11-05 00:03] Guard #99 begins shift',
    '[1518-11-05 00:45] falls asleep',
    '[1518-11-05 00:55] wakes up'
]


def parse_data(record_data):
    records = sorted(record_data)
    minutes_slept_by_guard = defaultdict(list)
    guard = 0
    sleep_min = -1
    wake_min = -1

    for record in records:
        if 'begins shift' in record:
            match = re.search(r'#(\d+)', record)  # find ID num
            guard = int(match.group(1))
            sleep_min = 0
            wake_min = 0

        elif 'falls asleep' in record:
            match = re.search(r':(\d+)', record)  # find sleep minute
            sleep_min = int(match.group(1))

        elif 'wakes up' in record:
            match = re.search(r':(\d+)', record)  # find waking minute
            wake_min = int(match.group(1))
            minutes_slept_by_guard[guard] += list(range(sleep_min, wake_min))

    return minutes_slept_by_guard


def find_guard_most_asleep(sleep_data):
    sleepiest_guard = 0
    largest_amount_asleep = 0

    for guard in sleep_data.keys():
        sleeping = sleep_data[guard]
        if len(sleeping) > largest_amount_asleep:
            largest_amount_asleep = len(sleeping)
            sleepiest_guard = guard

    counted_minutes = Counter(sleep_data[sleepiest_guard])

    most_common_minute = counted_minutes.most_common(1)[0][0]

    print('Guard ' + str(sleepiest_guard) +
          ' X minute ' + str(most_common_minute)+':')
    print(str(sleepiest_guard * most_common_minute))


def find_minute_most_asleep(sleep_data):
    minute_asleep_frequency = defaultdict(list)

    for minute in range(60):
        for guard, minutes in sleep_data.items():
            if minute in minutes:
                minute_asleep_frequency[minute] += [guard] * \
                    minutes.count(minute)

    most_common_minute = 0
    most_common_guard = 0
    largest_freq = 0

    for minute, guard_freq in minute_asleep_frequency.items():
        count = Counter(guard_freq)
        most_common = count.most_common(1)[0]  # tuple of (gaurd, frequency)

        if most_common[1] > largest_freq:
            largest_freq = most_common[1]
            most_common_minute = minute
            most_common_guard = most_common[0]

    print('Guard ' + str(most_common_guard) +
          ' X minute ' + str(most_common_minute)+':')
    print(str(most_common_guard * most_common_minute))


if __name__ == "__main__":
    # record_data = [line.strip('\n') for line in TEST_DATA]
    record_data = [line.strip('\n')
                   for line in open('InputData/day4Input.txt', 'r')]

    guards_sleep_data = parse_data(record_data)
    find_minute_most_asleep(guards_sleep_data)
