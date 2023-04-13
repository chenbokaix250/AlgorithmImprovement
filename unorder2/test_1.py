i= 0
N= int(input())

str_line = []
def time_print(a):
    h = str(int(a/3600))
    m = str(int(a%3600/60))
    s = str(int(a%60))
    print(h + " "+ m + " "+s) 
while True:
    word = int(input())
    time_print(word)
    i = i+1
    if i == N:
        break