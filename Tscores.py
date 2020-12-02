""" T scores """
def tscore(num, max_scores):
    """ T scores """
    lst_num = []
    for _ in range(num):
        scores = int(input())
        if scores <= max_scores:
            lst_num.append(scores)
    lst_num_times = [i**2 for i in lst_num]
    sd_scores = ((num*sum(lst_num_times)-(sum(lst_num)**2))/(num*(num-1)))**0.5
    mean = sum(lst_num)/num
    z_scores = [(i-mean)/sd_scores for i in lst_num]
    t_scores = ['%.2f' %(50+10*j) for j in z_scores]
    print(*t_scores, sep='\n')
tscore(int(input()), int(input()))

