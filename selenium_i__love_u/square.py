import math


def sqrt(list):
	num=0
	for i in list:
		num=num+i*i
	return math.sqrt(num)

def how_many(num):

	List=[]
	for i in num:
		List.append(i)

	return List


def cheng(list1,list2):
	sum=0
	lon=len(list1)
	for i in range(lon):
		sum=sum+list1[i]*list2[i]
	return sum


def cos(list1,list2):
	upper=cheng(list1,list2)
	lower=sqrt(list1)*sqrt(list2)
	return upper/lower


def zhuanzhi(list1):

	row = len(list1)
	col = len(list1[0])
	list2=[[0]*row for i in range(col)]
	# print(list1)
	# print(list2)

	for i in range(row):
		for j in range(col):
			

			list2[j][i]=list1[i][j]
			# print(list2)
			# print("list2"+"["+str(j)+"]"+"["+str(i)+"]"+"="+"list1"+"["+str(i)+"]"+"["+str(j)+"]")
			# print(str(list2[j][i])+"="+str(list1[i][j]))
			# # print("------list1-----"+str(list1[i][j]))
			# # print("------list2-----"+str(list2[j][i]))
			# print(list2)
			# print("\n")
	
	return list2


def all_people(list):
	row = len(list)
	# i=len(list)
	# print(row)
	list_new = [[0]*row for i in range(row)]
	i=0
	while(i<row):
		j=0
		while(j<row):
			# print(str(i)+"\t"+str(j))
			list_new[i][j]=cos(list[i],list[j])
			# print("inside")
			# print(list_new)
			j=j+1
			# print(i)
			# print(j)
			
		i=i+1	
		# print("outsider")
	# for i in range(row):
	# 	for j in range(row):
	# 		list_new[i][j]=cos(list[i],list[j])

	return list_new





def all_book(list):
	list_zhuanzhi=zhuanzhi(list)
	row = len(list_zhuanzhi)
	
	list_new = [[0]*row for i in range(row)]
	i=0
	while(i<row):
		j=0
		while(j<row):
			list_new[i][j]=cos(list_zhuanzhi[i],list_zhuanzhi[j])
			j=j+1
		i=i+1	
	return list_new


# a=input("input:")
# print(a)
# c=all_book([[5,3,2,4],[4,5,3,2],[5,2,3,4]])
# print(c)
#
# d=all_people([[5,3,2,4],[4,5,3,2],[5,2,3,4]])
# print(d)
# # c=zhuanzhi([[5,3,2,4],[4,5,3,2],[5,2,3,4]])
# # print(c)



