
from typing import List

def payments(values: List[float], choice_role) -> List[float]:

    check_choice,winners = choice_role(values),[0] * len(values)
    new_values = list(zip(values, check_choice))
    for i in range(0,len(values)):
        vaw = list(map(lambda x: [x[0], x[1]], values))
        if new_values[i][1]==True:
            while choice_role(vaw)[i]:
                vaw[i][0] -= 0.01 #neli_diff
            winners[i]=(vaw[i][0] + 0.01)
        else:
            pass
    return winners

def algo1(values: List[tuple], k): #gr
    sorted_values,c_values,winners = values.copy(),values.copy(),[False] * len(values)
    sorted_values.sort(key=k, reverse=True)
    w_sum,sum,max_weight,counter = 0,0,100,0
    for tup in sorted_values:
        index1 = c_values.index(tup)
        if w_sum+tup[1] <= max_weight:
            w_sum += tup[1]
            sum += tup[0]
            winners[index1] = True
            counter+=1
        else:
            return winners, sum
    return winners, sum

def algo2(val_w: List[tuple]):
    if algo1(val_w, lambda x: x[0])[1]>algo1(val_w, lambda x: x[0] / x[1])[1]:
        return algo1(val_w, lambda x: x[0])
    return algo1(val_w, lambda x: x[0] / x[1])

if __name__ == '__main__':
    print("********Examples from the class********")
    print("greedy algorithm:")
    greedy_tarmil = [(100, 100), (20, 2), (20, 2),(20,2)]
    print(payments(greedy_tarmil, lambda x: algo1(x, lambda y: y[0])[0]))
    greedy_tarmil = [(100, 100), (20, 2), (20, 2)]
    print(payments(greedy_tarmil, lambda x: algo1(x, lambda y: y[0])[0]))
    greedy_tarmil = [(54, 52), (52, 51), (49, 49)]
    print(payments(greedy_tarmil, lambda x: algo1(x, lambda y: y[0])[0]))
    greedy_tarmil = [(100, 100), (60, 2), (50, 2)]
    print(payments(greedy_tarmil, lambda x: algo1(x, lambda y: y[0])[0]))
    print("greedy a+b algorithm:")
    print(payments(greedy_tarmil, lambda x: algo2(x)[0]))
    greedy_tarmil = [(100, 100), (20, 2), (20, 2)]
    print(payments(greedy_tarmil, lambda x: algo2(x)[0]))
    greedy_tarmil = [(54, 52), (52, 51), (49, 49)]
    print(payments(greedy_tarmil, lambda x: algo2(x)[0]))


