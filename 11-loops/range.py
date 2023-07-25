# Sample of range using For python 3 convert range to list

stop=5
result=list(range(stop))
print(f"start=default, stop={stop} and step=default range({stop}): {result}")
start=0
stop=5
result=list(range(start,stop))
print(f"start={start}, stop={stop} and step=default range({start},{stop}): {result}")
start=0
stop=5
step=1
result=list(range(start,stop,step))
print(f"start={start}, stop={stop} and step={step} range({start},{stop},{step}): {result}")
start=0
stop=20
step=2
result=list(range(start,stop,step))
print(f"\nstart={start}, stop={stop} and step={step} range({start},{stop},{step}): {result}")
start=0
stop=21
step=2
result=list(range(start,stop,step))
print(f"\nstart={start}, stop={stop} and step={step} range({start},{stop},{step}): {result}")
start=0
stop=21
step=3
result=list(range(start,stop,step))
print(f"\nstart={start}, stop={stop} and step={step} range({start},{stop},{step}): {result}")
start=0
stop=21
step=7
result=list(range(start,stop,step))
print(f"\nstart={start}, stop={stop} and step={step} range({start},{stop},{step}): {result}")
start=10
stop=2
step=-1
result=list(range(start,stop,step))
print(f"\nDecrease \nstart={start}, stop={stop} and step={step} range({start},{stop},{step}): {result}")
start=-2
stop=-10
step=-3
result=list(range(start,stop,step))
print(f"\nDecrease \nstart={start}, stop={stop} and step={step} range({start},{stop},{step}): {result}")

my_list=[4,9,64,7,"Python"]
print(f"The number of values in my list {my_list} are {len(my_list)}")
print(f"The range of index of my list {my_list} is {range(len(my_list))}")
print(f"The indexes of my list {my_list} are {list(range(len(my_list)))}")

for each_index in range(len(my_list)):
    print(f"Index {each_index} --> {my_list[each_index]}")