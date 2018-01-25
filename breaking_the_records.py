'''
Maria plays n games of college basketball in a season. Because she wants to go pro, she tracks her points scored per game sequentially in an array defined as score = [s0, s1, ...., sn-1]. After each game i, she checks to see if score si breaks her record for most or least points scored so far during that season.

Given Maria's array of scores for a season of n games, find and print the number of times she breaks her record for most and least points scored during the season.
'''


def breakingRecords(score):
    highest = score[0]
    lowest = score[0]
    H = 0
    L = 0

    for i in score[1:]:
        if i > highest:
            highest = i
            H += 1
        elif i == highest and i == lowest:
            pass
        elif i < lowest:
            lowest = i
            L += 1
    return(H, L)


if __name__ == "__main__":
    n = int(input().strip())
    score = list(map(int, input().strip().split(' ')))
    result = breakingRecords(score)
    print (" ".join(map(str, result)))
