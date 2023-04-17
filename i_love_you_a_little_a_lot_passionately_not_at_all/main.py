def how_much_i_love_you(n):
    outcomes = ["I love you", "a little", "a lot", "passionately", "madly", "not at all"]
    return outcomes[(n-1) % len(outcomes)]
