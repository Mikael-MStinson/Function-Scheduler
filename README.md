# Function Scheduler
A set of tools that allow you to put function calls on a schedule to be executed repeatedly

Example: updating the status of a variable once a week, while acting on said variable once a day and calling an execute function once every 5 minutes

Usage:

``` Python
from function_scheduler import Scheduler

scheduler = Scheduler()

def update():
	#performs an update every 5 mintues

scheduler.execute(update, minutes = 5)

def main():
	while True:
		try:
			scheduler.tick()
		except Exception:
			break

```
