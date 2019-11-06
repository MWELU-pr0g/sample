#pyhton oop
#class is blueprint for instances and class instance 
#intance variable containce data that is unique to each instances
class Employee:
	raise_amount=1.04
	nums_of_emps=0

   	def __init__(self,first,last,pay):
		self.first=first
		self.last=last
		self.pay=pay
		self.email=first+'.'+last +'@company.com'
		Employee.nums_of_emps+=1

	def fullname(self):
	    return'{}' ' ''{}'.format(self.first,self.last)

	def apply_raise(self):
		self.pay=(self.pay *self.raise_amount)

		@classmethod
		def set_raise_amount(cls,amount):
			cls.raise_amount=amount
class developer(Employee):
	
	def fullname(self):
		print(super.fullname())
	    return "company"


dev_1=developer('carol','mutinda',700000)
dev_2=developer('musyoka','joshua',800000)
print(dev_1.fullname())

emp_1=Employee('liam','mutinda',600000)
emp_2=Employee('prince','muasya',50000)

print(Employee.nums_of_emps)

print(dev_2.email)

# print(emp_2.pay)
# # emp_2.apply_raise()
# print(emp_2.raise_amount)
# print(emp_2.apply_raise())
# Employee.set_raise_amount(100)  #to work on this asap
# print(Employee.raiseamount)