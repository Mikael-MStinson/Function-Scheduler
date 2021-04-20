from singleton_decorator import singleton
from time import time

@singleton
class Scheduler:
	def __init__(self):
		self.functions = []
	
	def execute(self,function, seconds = 0, minutes = 0):
		interval = minutes * 60 + seconds
		self.functions.append({"function":function,"interval":interval,"time":time()})
		
	def tick(self):
		current_time = time()
		for function in self.functions:
			if current_time - function["time"] >= function["interval"]:
				function["function"]()
				function["time"] = current_time
		