def postive_fib(n):
    postive_list = [0,1]
    for i in range(n-1):
        postive_list.append(postive_list[-2]+postive_list[-1])
    return postive_list

def negative_fiv(n):
    negative_list = [0,1]
    for i in range(n-1):
        negative_list.append(negative_list[-2]-negative_list[-1])
    return negative_list


print(negative_fiv(8)[::-1] + postive_fib(8)[1:])
