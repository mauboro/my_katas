from datetime import timedelta
from statistics import median

def stat(strg):
    if not strg: return ""
    word = [w.split("|") for w in strg.split(", ")]
    times = [timedelta(hours=int(s[0]), minutes=int(s[1]), seconds=int(s[2])) for s in word] 
    rang = str((max(times) - min(times))).replace(":", "|")
    average = str(timedelta(seconds=(sum([time.seconds for time in times]) // len(times)))).replace(":", "|")
    media = str(median(times)).replace(":", "|")
    media = media.split(".")[0]
    
    res = []
    res.append(rang)
    res.append(average)
    res.append(media)
    another_res = []
    for time in res:
        if len(time) == 7:
            another_res.append("0" + time)
        else:
            another_res.append(time)
    print(another_res)
        
    return f"Range: {another_res[0]} Average: {another_res[1]} Median: {another_res[2]}"
    
