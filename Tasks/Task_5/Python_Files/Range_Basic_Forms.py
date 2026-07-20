# Three Forms Of range():
#   range(stop)            -> 0, 1, 2, ..., stop-1
#   range(start, stop)     -> start, start+1, ..., stop-1
#   range(start, stop, step) -> start, start+step, ..., < stop
 
# range(stop): 0 To 10 Inclusive — Use stop=11
print("Numbers 0 To 10:")
for num in range(11):           # range(stop)
    print(num, end=" ")
 
# range(start, stop): 5 To 15 Inclusive — stop=16
print("\nNumbers 5 To 15:")
for num in range(5, 16):        # range(start, stop)
    print(num, end=" ")

# range(start, stop, step): Odd Numbers 1 To 21, step=2
print("\nOdd Numbers 1 To 21:")
for num in range(1, 22, 2):     # range(start, stop, step)
    print(num, end=" ")
