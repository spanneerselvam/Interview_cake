def consolidate_meetings(meetings):
    output = []
    for pair in meetings:
        max_item = max(pair)
        min_item = min(pair)
        output.append(min_item)
        for i in range(min_item+1, max_item):
            output.append(i)
        output.append(max_item)
    output = sorted(output)
    output = set(output)
    meetings = []
    meetings, consecutive_numbers = [], []
    i = min(output)
    for item in output:
        if item == i:
            consecutive_numbers.append(item)
        else:
            consecutive_numbers = []
            consecutive_numbers.append(item)
            i = item
        i += 1
        meetings.append(consecutive_numbers)
        
    meetings = list(meetings for meetings,_ in itertools.groupby(a))
    output = list()
    
    for item in meetings:
        pair = ()
        pair = list(pair)
        pair.append(min(item))
        pair.append(max(item))
        pair = tuple(pair)
        output.append(pair)
    return output
