class call(object):
	"""docstring for call"""
	def __init__(self, ids, caller, phone, time, reason):
		self.ids = ids
		self.caller = caller
		self.phone = phone
		self.time = time
		self.reason = reason
	def display_info(self):
		print "Unique Id: {}".format(self.ids)
		print "Caller Name: {}".format(self.caller)
		print "Phone Number: {}".format(self.phone)
		print "Time of Call: {}".format(self.time)
		print "Reason for Call: {}".format(self.reason)

class callCenter(object):
	"""docstring for callCenter"""
	def __init__(self):
		# super(callCenter, self).__init__()
		self.calls = []
		self.queue = len(self.calls)
	def addCall(self, moo):
		# callInfo = self.caller,
		self.calls.append(moo)
		self.queue += 1
		return self
	def display(self):
		for x in xrange(0, len(self.calls)):
			print self.calls[x].display_info()
		print "Queue Length: {}".format(self.queue)

call1 = call(001, "Becky", 206, "9:23", "Wrong Number")
call2 = call(002, "Becky", 206, "9:23", "Wrong Number")
call3 = call(003, "Nicki", 206, "9:23", "Wrong Number")
call4 = call(004, "Curtis", 206, "9:23", "Wrong Number")
call5 = call(005, "Me", 206, "9:23", "Wrong Number")
		
Center = callCenter()

Center.addCall(call1).addCall(call2).display()
		