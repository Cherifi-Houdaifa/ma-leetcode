def main(events: list[list[int]]) -> int:
    day = 0
    maxDay = getMaxDay(events)
    maxEvents = 0
    while day < maxDay + 1:
        currentEvents = searchEvents(events, day + 1)
        print(currentEvents)
        if len(currentEvents) > 0:
            events.remove(currentEvents[0])
            maxEvents += 1

        day += 1
    print(maxEvents)
    return maxEvents


def searchEvents(events: list[list[int]], d: int):
    result = []
    for e in events:
        if e[0] <= d <= e[1]:
            result.append(e)
    result.sort(key=lambda e: e[1])
    return result


def getMaxDay(events: list[list[int]]):
    maxDay = 0
    for i in events:
        if max(i) > maxDay:
            maxDay = max(i)
    return maxDay

# main([[27,27],[8,10],[9,11],[20,21],[25,29],[17,20],[12,12],[12,12],[10,14],[7,7],[6,10],[7,7],[4,8],[30,31],[23,25],[4,6],[17,17],[13,14],[6,9],[13,14]])


def main2(events: list[list[int]]):
    events.sort(key=lambda e: (e[1], e[0]))
    print(events)
    day = 1
    maxEvents = 0
    while len(events) > 0:
        i = 0
        event = events[i]
        # this is for solving two edge cases (it could be better)
        while i < len(events):
            event = events[i]
            if event[0] <= day <= event[1]:
                maxEvents += 1
                events.remove(event)
                break
            elif day > event[1]:
                events.remove(event)
                break
            i += 1
        day += 1
    print(maxEvents)
    return maxEvents


main2([[27,27],[8,10],[9,11],[20,21],[25,29],[17,20],[12,12],[12,12],[10,14],[7,7],[6,10],[7,7],[4,8],[30,31],[23,25],[4,6],[17,17],[13,14],[6,9],[13,14]])

# pseudo-code
# first set day to n
# then search the events for all events that satisfy (startDay <= n <= endDay)
# sort them based on the ones that have the endDay as n
# choose the first one and increment day and and delete it and repeat


# [[2, 3], [3, 4]]

"""
i = 0
        event = events[i]
        while i < len(events):
            event = events[i]
            if event[0] <= day <= event[1]:
                maxEvents += 1
                break
            i += 1
"""
