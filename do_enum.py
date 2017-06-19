from enum import Enum, unique


@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


print(Weekday(1))

print(Weekday(1).name)

print(Weekday.Tue)

print(Weekday.Tue.value)


for name, member in Weekday.__members__.items():
    print(name, member)
    print(name, member.value)
