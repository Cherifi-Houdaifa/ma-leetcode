def main(events: list[list[int]]):
    events.sort(key=lambda e: e[0])
    day = 1
    maxEvents = 0

main([[1,2],[2,3],[3,4],[1,2]])