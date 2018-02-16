import threading
import multiprocessing

ITERATIONS = 10000

def threadTest(index):
	for i in range(ITERATIONS):
		for j in range(ITERATIONS):
			pass

if __name__ == "__main__":

	threads = list()
	for i in range(10):
		threads.append(multiprocessing.Process(target=threadTest, args=(i,)))
		# 170%
		# threads.append(threading.Thread(target=threadTest, args=(i, ) ))


	for t in threads:
		t.start()

	for t in threads:
		print 'waiting'
		t.join()
