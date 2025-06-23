#!/usr/bin/python3
def multiple_returns(sentence):
    #print(sentence[:1])
    if sentence is None or len(sentence) < 1 or sentence == "":
        return((0, None))
    else:
        res = (len(sentence),sentence[:1])
        return(res)
