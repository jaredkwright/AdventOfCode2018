from datetime import datetime
import numpy as np

inputs = open('../input.txt', 'r')
data = inputs.readlines()

guards = dict()


class SleepSession:
    def __init__(self, falls_asleep_time):
        self.asleep_time = falls_asleep_time
        self.awake_time = None

    def wake(self, wakes_up_time):
        self.awake_time = wakes_up_time

    @property
    def sleep_minutes(self):
        session_minutes = (self.awake_time - self.asleep_time).seconds // 60
        return session_minutes

    @property
    def sleep_hour_array(self):
        hour = np.full(60, False, dtype=bool)
        start_index = self.asleep_time.minute if self.asleep_time else None
        end_index = self.awake_time.minute if self.awake_time else None
        if start_index and end_index:
            hour[start_index:end_index] = True
        return hour


class GuardShift:
    def __init__(self, start_datetime):
        self.shift_start = start_datetime
        self.sleep_sessions = []
        self.current_session = None

    def sleep(self, start_datetime):
        self.current_session = SleepSession(start_datetime)
        self.sleep_sessions.append(self.current_session)

    def wake(self, end_datetime):
        self.current_session.wake(end_datetime)
        self.current_session = None

    @staticmethod
    def start_shift(start_datetime):
        return GuardShift(start_datetime)

    @property
    def total_sleep_minutes(self):
        shift_minutes = sum([s.sleep_minutes for s in self.sleep_sessions])
        return shift_minutes

    @property
    def sleep_matrix(self):
        if len(self.sleep_sessions) <= 0:
            return np.array([np.full(60, False, dtype=bool)])
        return np.array([session.sleep_hour_array for session in self.sleep_sessions])


class Guard:
    def __init__(self, guard_id):
        self.id = guard_id
        self.shifts = []

    def record_shift(self, shift):
        self.shifts.append(shift)

    @property
    def total_sleep_minutes(self):
        return sum([s.total_sleep_minutes for s in self.shifts])

    @property
    def full_sleep_matrix(self):
        return np.concatenate([shift.sleep_matrix for shift in self.shifts])

    @property
    def total_days_slept_by_minute(self):
        return np.sum(self.full_sleep_matrix, axis=0)

    @property
    def sleepiest_minute(self):
        if self.total_days_slept_by_minute.size == 0:
            return None
        return np.argmax(self.total_days_slept_by_minute)

    @property
    def days_asleep_on_sleepiest_minute(self):
        if self.total_days_slept_by_minute.size == 0 or self.sleepiest_minute is None:
            return 0
        try:
            return self.total_days_slept_by_minute[self.sleepiest_minute]
        except Exception:
            print('Guard {}'.format(self.id))
            print('Shifts: {}'.format(self.shifts))


class ShiftProcessor:
    guards = dict()
    current_guard = None
    current_shift = None

    @staticmethod
    def parse_line(log_line):
        log_line = log_line.rstrip().lstrip()
        open_date_bracket = log_line.find('[')
        close_date_bracket = log_line.find(']')
        date_timestamp = datetime.fromisoformat(log_line[open_date_bracket+1:close_date_bracket])

        rest_of_line = log_line[close_date_bracket+1:].lstrip()

        line_type = 'shift'
        guard_number = None
        if rest_of_line == 'falls asleep':
            line_type = 'sleep'
        elif rest_of_line == 'wakes up':
            line_type = 'wake'

        if line_type == 'shift':
            guard_number = int(rest_of_line.split(' ')[1].lstrip('#'))

        return line_type, date_timestamp, guard_number

    def next_line(self, line):
        try:
            (log_type, timestamp, guard_number) = line
            if log_type == 'shift' and guard_number:
                self.current_shift = None
                if guard_number in self.guards:
                    self.current_guard = self.guards[guard_number]
                else:
                    self.current_guard = Guard(guard_number)
                    self.guards[guard_number] = self.current_guard
                self.current_shift = GuardShift.start_shift(timestamp)
                self.current_guard.record_shift(self.current_shift)
            elif log_type == 'sleep' and self.current_shift:
                self.current_shift.sleep(timestamp)
            elif log_type == 'wake' and self.current_shift:
                self.current_shift.wake(timestamp)
        except Exception:
            print(line)
            quit()


lines = map(ShiftProcessor.parse_line, data)
log = sorted(lines, key=lambda x: x[1])

processor = ShiftProcessor()
for line in log:
    processor.next_line(line)

guards_list = list(processor.guards.items())
guards_list = sorted(guards_list, key=lambda g: g[1].days_asleep_on_sleepiest_minute, reverse=True)
most_consistently_sleepy_guard = guards_list[0][1]

print('Guard {}: {} minutes'.format(most_consistently_sleepy_guard.id, most_consistently_sleepy_guard.total_sleep_minutes))
print('Sleepiest minute: {}'.format(most_consistently_sleepy_guard.sleepiest_minute))
print('Days asleep on sleepiest minute: {}'.format(most_consistently_sleepy_guard.days_asleep_on_sleepiest_minute))
print('Answer result: {}'.format(most_consistently_sleepy_guard.id * most_consistently_sleepy_guard.sleepiest_minute))