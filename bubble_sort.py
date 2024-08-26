def bubble(list):
    l = len(list)
    for i in range(l-1):
        for j in range(l-i-1):
            if list[j]>list[j+1]:
                list[j],list[j+1]=list[j+1],list[j]
    return list             

#list = [3,4,1,2,5]
#print(bubble(list))