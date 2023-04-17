def kooka_counter(laughing):
    diff = ""
    count = 0
    for c in laughing:
        if c == "h" and diff == "h":
            pass
        if c == "h" and diff != "h":
            count += 1
            diff = "h"
        if c == "H" and diff == "H":
            pass
        if c == "H" and diff != "H":
            count += 1
            diff = "H"
    return count

import re

def kooka_counter_refactored(laughing):
    return len(re.findall(r"(ha)+|(Ha)+", laughing))
