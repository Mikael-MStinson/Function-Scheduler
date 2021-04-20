from function_scheduler import Scheduler

scheduler = Scheduler()

def ten_seconds():
	print("10 seconds has elapsed")
	
def thirty_seconds():
	print("30 seconds has elapsed")

scheduler.execute(ten_seconds, seconds = 10)
scheduler.execute(thirty_seconds, seconds = 30)

def main():
	while True:
		try:
			scheduler.tick()
		except Exception as e:
			print(e)
			exit()
			
if __name__ == "__main__":
	main()