import random
import matplotlib.pyplot as plt
import matplotlib.animation as anim
import numpy as np
import timeit
import time
import pdb

#Arr = np.random.randint(0,100,50)
#Arr = np.array([6, 41, 41, 50, 51, 59, 78, 41, 52, 24])
Arr = np.arange(250)
print(Arr)
np.random.shuffle(Arr)
print(Arr)


# Sorting algos
def selection_sort(Arr):
	Num_op = [0]
	i = 0
	while i < len(Arr) -1:
		smallest = i
		Num_op[0] += 1

		for k in range(i,len(Arr)):
			if Arr[smallest] > Arr[k]:
				smallest = k
			Num_op[0] += 1	

		swap(Arr,i,smallest)
		yield np.append(Arr, Num_op) # Arr
		i += 1
	

def bubble_sort(Arr):
	Num_op = [0]
	
	
	finished = False
	while finished == False:

		# check if done by iteration through the list with no swaps
		consecutive = 0
		
		for i in range(len(Arr) - 1):
			j = i + 1

			if Arr[i] > Arr[j]:
				
				swap(Arr, i, j)
				consecutive += 1

			Num_op[0] += 1	
			yield np.append(Arr, Num_op) # Arr
		
		# check if done		
		if consecutive == 0:
			Num_op[0] += 1
			finished = True
	yield np.append(Arr, Num_op) # Arr 
	print(Num_op)	

def quick_sort_end(Arr,bot,top,Num_op):
	Num_op = Num_op
	pivot = Arr[top]
	i = bot
	Num_op[0] += 1
	if bot < top:
		for k in range(bot,top):
			Num_op[0] += 1
			if Arr[k] < pivot:
				swap(Arr, i, k)
				i += 1
				yield np.append(Arr, Num_op) # Arr

		swap(Arr,i,top)
	
		yield np.append(Arr, Num_op) # Arr	
		yield from quick_sort_end(Arr,bot,i - 1, Num_op)
		yield from quick_sort_end(Arr,i + 1,top, Num_op)


def quick_sort_mid(Arr,bot,top,Num_op):
	Num_op = Num_op
	i = bot
	k = top
	mid_point = findMiddle(Arr[bot:top+1]) + i
	piv_index = mid_point
	Num_op[0] += 1
	if piv_index >= len(Arr):
		return Arr
	pivot = Arr[piv_index]
	Num_op[0] += 1
	if i < k:
		while True:
			

			while Arr[i] < pivot:
				Num_op[0] += 1
				i += 1
			Num_op[0] += 1	
			
			while Arr[k] > pivot:
				Num_op[0] += 1
				k -= 1
			Num_op[0] += 1

			Num_op[0] += 1
			if i >= k:
				break
			swap(Arr,i,k)

			yield np.append(Arr, Num_op) # Arr	
		
		

		yield from quick_sort_mid(Arr, bot, k - 1, Num_op)
		yield from quick_sort_mid(Arr, k + 1, top, Num_op)

				



def findMiddle(input_list):
	middle = float(len(input_list))/2
	if middle % 2 != 0:
		return int(middle - 0.5)
	else:
		return int(middle)







# Swap - swaps two elements from the input array in place
def swap(A,i,j):
	if A[i] == A[j]:
		return A

	ph = A[i]
	A[i] = A[j]
	A[j] = ph
	return A

algo = quick_sort_mid(Arr,0,len(Arr) -1,[0])
#algo = quick_sort_end(Arr,0,len(Arr) -1,[0])
#algo = selection_sort(Arr)
#algo = bubble_sort(Arr)
titles = ["Bubble Sort","Selection Sort","quick_sort"]

# makes the figure and the graph
fig, ax = plt.subplots()
ax.set_title(titles[2])
bar_rec = ax.bar(range(len(Arr)), Arr, align='edge')
text = ax.text(0.02, 0.95, "", transform=ax.transAxes)


#number of comparisons too. only works for selection sort and bubble
epochs = [0]
comp = [0]
def update_plot(Arr, rec, epochs):

    for rec, val in zip(rec, Arr[0:len(Arr)-1]):
        rec.set_height(val)
    epochs[0]+= 1
    comp[0] = Arr[len(Arr)-1]
    text.set_text("No.of swaps :{}, comparisons: {}".format(epochs[0],comp[0]))

anima = anim.FuncAnimation(fig, func=update_plot, fargs=(bar_rec, epochs), frames=algo, interval=1, repeat=False)
plt.show()



## without number of comparisons. Should just delete all the comp stuff from the other funcitons
# epochs = [0]
# def update_plot(Arr, rec, epochs):

#     for rec, val in zip(rec, Arr):
#         rec.set_height(val)
#     epochs[0]+= 1
#     text.set_text("No.of operations :{} ".format(epochs[0]))

# anima = anim.FuncAnimation(fig, func=update_plot, fargs=(bar_rec, epochs), frames=algo, interval=1, repeat=False)
# plt.show()



