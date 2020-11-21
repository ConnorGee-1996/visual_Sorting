import random
import matplotlib.pyplot as plt
import matplotlib.animation as anim
import numpy as np
import timeit
import time
import pdb

#Arr = np.random.randint(0,100,50)
#Arr = np.array([6, 41, 41, 50, 51, 59, 78, 41, 52, 24])
Arr = np.arange(50)
print(Arr)
np.random.shuffle(Arr)
print(Arr)


# Sorting algos - adding different colors
def selection_sort(Arr):
	Num_op = 0
	Num_swaps = 0
	i = 0
	sorted_idxs = []
	while i < len(Arr) -1:
		smallest = i
		Num_op += 1

		for k in range(i,len(Arr)):

			if Arr[smallest] > Arr[k]:
				smallest = k
			Num_op += 1

			# output the array with k, to show the index's being compared
			yield Arr, Num_op,sorted_idxs,Num_swaps,k,smallest

		swap(Arr,i,smallest)

		#every swap add to the number of swaps and add the index for the sorted array to sorted.
		Num_swaps += 1
		sorted_idxs.append(i)
		
		yield Arr, Num_op,sorted_idxs,Num_swaps,k,i # Arr  np.append(Arr, Num_op),sorted_idxs
		i += 1
	
	
	sorted_idxs.append(i)
	yield Arr, Num_op,sorted_idxs,Num_swaps,k,i # Arr
	
def bubble_sort(Arr):
	Num_op = [0]
	Num_swaps = 0

	sorted_idxs = []
	counter = 0

	
	while True:
		# check if done by iteration through the list with no swaps
		consecutive = 0
		
		for i in range(len(Arr) - counter - 1):
			j = i + 1

			if Arr[i] > Arr[j]:
				
				swap(Arr, i, j)
				consecutive += 1
				Num_swaps += 1

			Num_op[0] += 1	
			yield Arr, Num_op,sorted_idxs,Num_swaps,i,j # Arr
		
		sorted_idxs.append(len(Arr) - counter)
		counter += 1

		# check if done
		Num_op[0] += 1	
		if len(sorted_idxs) == len(Arr):
			break
	yield Arr, Num_op,sorted_idxs,Num_swaps,i,j # Arr 
		
def quick_sort_end(Arr,bot,top,Num_op,Num_swaps,sorted_idxs):
	Num_op = Num_op
	Num_swaps = Num_swaps
	sorted_idxs = sorted_idxs

	pivot = Arr[top]
	i = bot
	Num_op[0] += 1
	print(bot,top)
	if bot == top:
		sorted_idxs.append(i)
		yield Arr, Num_op,sorted_idxs,Num_swaps,bot,top
	if bot < top:

		for k in range(bot,top):
			Num_op[0] += 1
			if Arr[k] < pivot:

				swap(Arr, i, k)
				Num_swaps += 1

				i += 1
			yield Arr, Num_op,sorted_idxs,Num_swaps,k,i #np.append(Arr, Num_op) # Arr

		swap(Arr,i,top)
		Num_swaps += 1

		sorted_idxs.append(i)
	
		yield Arr, Num_op,sorted_idxs,Num_swaps,k,i # Arr	
		yield from quick_sort_end(Arr,bot,i - 1, Num_op,Num_swaps,sorted_idxs)
		yield from quick_sort_end(Arr,i + 1,top, Num_op,Num_swaps,sorted_idxs)

def quick_sort_mid(Arr,bot,top,Num_op,Num_swaps,sorted_idxs):
	Num_op = Num_op
	Num_swaps = Num_swaps
	sorted_idxs = sorted_idxs

	i = bot
	k = top
	mid_point = findMiddle(Arr[bot:top+1]) + i
	piv_index = mid_point


	Num_op[0] += 1
	if piv_index >= len(Arr):
		return Arr
	pivot = Arr[piv_index]
	print("piv",pivot)

	if bot == top:
		sorted_idxs.append(i)
		yield Arr, Num_op,sorted_idxs,Num_swaps,bot,top

	Num_op[0] += 1
	if i < k:
		while True:
			

			while Arr[i] < pivot:
				Num_op[0] += 1
				i += 1
				yield Arr, Num_op,sorted_idxs,Num_swaps,k,i
			Num_op[0] += 1	
			
			while Arr[k] > pivot:
				Num_op[0] += 1
				k -= 1
				yield Arr, Num_op,sorted_idxs,Num_swaps,k,i				
			Num_op[0] += 1

			Num_op[0] += 1
			if i >= k:
				break

			swap(Arr,i,k)
			Num_swaps += 1


			yield Arr, Num_op,sorted_idxs,Num_swaps,k,i # Arr

		if Arr[k] == pivot:
			sorted_idxs.append(k)
		elif Arr[i] == pivot:
			sorted_idxs.append(i)
		
		

		yield from quick_sort_mid(Arr, bot, k - 1, Num_op,Num_swaps,sorted_idxs)
		yield from quick_sort_mid(Arr, k + 1, top, Num_op,Num_swaps,sorted_idxs)			

def findMiddle(input_list):
	middle = float(len(input_list))/2
	if middle % 2 != 0:
		return int(middle - 0.5)
	else:
		return int(middle)

def medianOfThree(Arr,bot,top):
	middle = round((bot + top/2))



# Swap - swaps two elements from the input array in place
def swap(A,i,j):
	if A[i] == A[j]:
		return A

	ph = A[i]
	A[i] = A[j]
	A[j] = ph
	return A

algo = quick_sort_mid(Arr,0,len(Arr) -1,[0],0,[])
#algo = quick_sort_end(Arr,0,len(Arr) -1,[0],0,[])
#algo = selection_sort(Arr)
#algo = bubble_sort(Arr)
titles = ["Bubble Sort","Selection Sort","quick_sort"]

# makes the figure and the graph
fig, ax = plt.subplots(figsize = [10, 6])

ax.set_title(titles[1])
bar_rec = ax.bar(range(len(Arr)), Arr, align='edge',color = "red")
text = ax.text(0.01, 0.93, "", transform=ax.transAxes)




#number of comparisons too. Adding color changes. only works for selection sort
why = "This has to be inserted into the function else it takes in the array as seperate arguments into the function instead of one. not sure why."

def update_plot(Arr, rec,why):
    counter = 0

    for rec, val in zip(rec, Arr[0]):
        rec.set_height(val)


        # make all unsorted red apart from comparison index
        if counter == Arr[4] or counter == Arr[5]:
        	rec.set_color("darkblue")
        else:
        	rec.set_color("firebrick")

        if counter in Arr[2] :
        	rec.set_color("forestgreen")	

        if counter == len(Arr[0]):
            rec.set_color("forestgreen")
        print(np.sort(Arr[2]))    


        counter += 1

    
    
    text.set_text("No.of swaps :{}\nNo.of comparisons: {}".format(Arr[3],Arr[1]))

anima = anim.FuncAnimation(fig, func=update_plot, fargs=(bar_rec,why), frames=algo, interval=100, repeat=False)
plt.show()







# #number of comparisons too.
# epochs = [0]
# comp = [0]
# def update_plot(Arr, rec, epochs):

#     for rec, val in zip(rec, Arr[0:len(Arr)-1]):
#         rec.set_height(val)
#     epochs[0]+= 1
#     comp[0] = Arr[len(Arr)-1]
#     text.set_text("No.of swaps :{}, comparisons: {}".format(epochs[0],comp[0]))

# anima = anim.FuncAnimation(fig, func=update_plot, fargs=(bar_rec, epochs), frames=algo, interval=100, repeat=False)
# plt.show()



# # without number of comparisons. Should just delete all the comp stuff from the other funcitons
# epochs = [0]
# def update_plot(Arr, rec, epochs):

#     for rec, val in zip(rec, Arr):
#         rec.set_height(val)
#     epochs[0]+= 1
#     text.set_text("No.of operations :{} ".format(epochs[0]))

# anima = anim.FuncAnimation(fig, func=update_plot, fargs=(bar_rec, epochs), frames=algo, interval=1, repeat=False)
# plt.show()



