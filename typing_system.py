# typing speed system
from time import time
 # to find accuracy
def find_error(prompt):
    global inwords
    words=prompt.split()
    error=0
    for i in range(len(inwords)):
        if i in (0,len(inwords)-1):
            if  inwords[i]==words[i]:
                continue
            else:
                error+=1
        else:
            if inwords[i]==words[i]:
                if inwords[i+1]==words[i+1] and inwords[i-1]==words[i-1]:
                    continue
                else:
                    error+=1
            else:
                error+=1
    return error
# now to calculate speed
def speed(inprompt,stime,etime):
    global time
    global inwords
    inwords=inprompt.split()
    twords=len(inwords)
    speed= twords / time
    return speed
# noe to calculate total elapsed time
def elapsed_time(etime,stime):
    time=etime-stime    #etime--->ending time and stime --> strating time
    return time


if __name__=='__main__':
    prompt="fdjfdif dhk fdbfhlnkdhg nkfguydo fjodsn fid ng,ugodfjl;d mdig jdklfgm gjg gjujfl;sdu" # this is the typing paraghraph
    print("enter this--->",prompt)
    print("press enter if you are ready for result or for checking the result")

    # colloct information for function
    stime=time()
    inprompt=input()
    etime=time()

    #now call the functions
    time=round(elapsed_time(stime,etime),2)
    speed=speed(inprompt,stime,etime)
    error=find_error(prompt)


    # now show the result of typing

    print("total time elapsed ",time,"second")
    print("the average speed is",speed,"word per minute")
    print("with total errors",error,"error")


    # thank you