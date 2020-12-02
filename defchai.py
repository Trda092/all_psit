"""main function"""
  
  
def main():
    """sad tuple"""
    t_1 = []
    num_1 = int(input())
    for _ in range(num_1):
        nums = int(input())
        if nums == 0:
            break
        t_1.append(nums)
  
    for i in range(1, num_1+1):
        if i not in t_1:
            print(i)
  
  
main()