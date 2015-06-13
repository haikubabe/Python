class Parent():

	def __init__(self,last_name,eye_color):
		print "Parent's constructor called"
		self.last_name=last_name
		self.eye_color=eye_color

	def show_info(self):
		print("Last name - "+self.last_name)
		print("Eye color - "+self.eye_color)


class Child(Parent):
	def __init__(self,last_name,eye_color,number_of_toys):
		print "Child's constructor called"
		Parent.__init__(self,last_name,eye_color)
		self.toys=number_of_toys

	def show_info(self):
		print("Last name - "+self.last_name)
                print("Eye color - "+self.eye_color)
		print("Toys - "+str(self.toys))


billy_cyrus=Parent("Cyrus","green")
billy_cyrus.show_info()

miley_cyrus=Child("Cyrus","blue",5)
miley_cyrus.show_info()

