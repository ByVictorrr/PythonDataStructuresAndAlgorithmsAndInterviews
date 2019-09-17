# given: two non-empty linked-lists rep two non neg numbers. the digits are stored in reverse order and each node contains a single digit.
# objective: add the two nums and return it as a linked list
# example: (2->4->3) + (5->6->4)
#	explanation: 342 + 465 = 807

class Node(object):

	def __init__(self, value):
		self.value = value
		self.next = None



def addTwoNumbers(l1, l2):
	# backtacking problem
	stack1,stack2 = [],[]
	ref = l1
	while ref:
		stack1.append(ref.value)
		ref = ref.next

	ref = l2
	while ref:
		stack2.append(ref.value)
		ref = ref.next
	

	num1 = 0
	#factor1 = 0
	while len(stack1) > 0:
		factor1 = len(stack1) - 1
		num1 += stack1.pop() * (10 ** factor1)

	num2 = 0
	while len(stack2) > 0:
		factor2 = len(stack2) - 1
		num2 += stack2.pop() * (10 ** factor2) 
	
	new_num = num1+num2

	
	ret_ll = None

	ptr = ret_ll = Node(new_num%10) 
	new_num//=10
	while new_num > 0:	
		ret_ll = ret_ll.next
		ret_ll = Node(new_num%10)
		new_num//=10
		#print(new_num)

	ret_ll.next = None
	return ptr



if __name__  == "__main__":
	l1 = Node(2)
	l1.next = Node(4)
	l1.next.next = Node(3)

	l2 = Node(5)
	l2.next = Node(6)
	l2.next.next = Node(4)

	ptr = addTwoNumbers(l1,l2)
	while ptr != None:
		print(ptr.value)
		ptr=ptr.next


