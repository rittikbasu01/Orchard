def RemoveDuplicate(duplicate):
    final_list=[]
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list

mylist=[]
n=int(input("Enter size of the list:\n"))
 
for i in range(0,n):
    temp=int(input("Enter number to append:\n"))
    mylist.append(temp)

result = RemoveDuplicate(mylist)
print(result)
