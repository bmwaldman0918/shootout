from shootout import Shootout

hockey = {
    "goal_prob": 33,
    "rounds": 3,
}
soccer = {
    "goal_prob": 75,
    "rounds": 5,
}


def test_sport(sport: {}, length: int):
    results = {}

    for i in range(length):
        test_case = Shootout(sport["goal_prob"], sport["rounds"])
        test_case.run()
        results[test_case.length] = results.get(test_case.length, 0) + 1

    return results


def print_results(res: {}):
    for i in sorted(res.keys()):
        print("Length: " + str(i) + ", Instances: " + str(res[i]))


def splits(res: {}, split: int):
    greater, less = 0, 0
    for i in sorted(res.keys()):
        if i > split:
            greater += res[i]
        elif i < split:
            less += res[i]
    return {
        'split': split,
        'greater': greater,
        'less': less,
        'even': 0 if res.get(split) is None else res[split],
    }


def print_splits(s: {}):
    length = s['less'] + s['greater'] + s['even']
    print(str(s['less'] / length * 100) + "% of shootouts were of a length less than "
          + str(s['split']) + ".")
    print(str(s['even'] / length * 100) + "% of shootouts were of length "
          + str(s['split']) + ".")
    print(str(s['greater'] / length * 100) + "% of shootouts were of a length greater than "
          + str(s['split']) + ".")


times = 100000
hockey_results = test_sport(hockey, times)
soccer_results = test_sport(soccer, times)

print("---Soccer---")
print_splits(splits(hockey_results, 11))
print("---Ice Hockey (NHL Rules)---")
print_splits(splits(hockey_results, 18))
