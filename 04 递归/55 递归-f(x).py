def evaluate_m(i,number=1,answer=0):
    if number <= i :
        answer += 1/number
        number += 1
        return evaluate_m(i,number,answer)
    return answer
print('{} : {:.4}'.format(5, evaluate_m(5)))
