scores = [32,21,19,30,90,100]

def passed(score):
    with_bonus = score + 10
    return with_bonus > 90

passing_scores = [passed(scores) for scores in scores]
print(passing_scores)


prices = [132,221,219,130,90,149]

apply_taxes = [price for price in prices if price > 150]
print(apply_taxes)


sscores = [32,21,19,30,90,100]
latest = sscores[-1]
print(latest)