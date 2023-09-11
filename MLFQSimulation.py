from tkinter import *
from tkinter import ttk
import pandas as pd 
import plotly.figure_factory as ff
from random import randint

class Process():
    def __init__(self,pid : int ,arrivaltime : int ,bursts):
        self.pid = pid
        self.arrivaltime = arrivaltime
        self.bursts = bursts
        self.turnIntoInts()
        self.q1 = 5  
        self.q2 = 3  
        self.numOfInterrupt = 0
        self.currentQueue = None
        self.flag = False
        self.waiting = 0 

    def printInfo(self):
        print('pid is ' + str(self.pid) + ' arrival time is  ' + str(self.arrivaltime) + ' bursts =  ',self.bursts,' waiting time = ', self.waiting )
    def turnIntoInts(self):
        for i in range(len(self.bursts)):
            self.bursts[i] = int(self.bursts[i])
    def totalBurst(self):
        sum =0
        for i in range( len(self.bursts)):
            if i%2==0: sum += self.bursts[i]
        return sum

def fillTrees(tree):
    for i in processes:
        #tree1.insert(parent='', index=0, text='', values=(i.pid,i.arrivaltime,str(i.bursts)))
        tree.insert(parent='', index=0, text='', values=(i.pid,i.arrivaltime,str(i.bursts)))

def deleteFrames(main_frame : Frame):
    for frame in main_frame.winfo_children():
        frame.destroy()

def generateWorkLoad(numOfProcesses,maxArrival,maxNumOfCPU,minCPU,maxCPU,minIO,maxIO):
    pid = 0 
    file  = open('Workload.txt' , 'w')
    for i in range(numOfProcesses):
        str1 = str(pid) + '\t' + str(randint(0,maxArrival)) + '\t'
        cpuBurst = randint(1,maxNumOfCPU) 
        for j in range(cpuBurst):
            if j == cpuBurst-1:
                str1 = str1 + str(randint(minCPU,maxCPU))
                break
            str1 = str1 + str(randint(minCPU,maxCPU)) + '\t'
            if cpuBurst != 1 and j != cpuBurst-1:
                str1 = str1 + str(randint(minIO,maxIO)) +'\t'
        if i == numOfProcesses-1:
            file.write(str1)
            break
        str1 = str1 + '\n'   
        file.write(str1)
        pid+=1

def WorkLoadGenerator(main_frame):
    deleteFrames(main_frame)

    f1 = Frame(main_frame)

    # pack everything onto f1 
    # deleteFrames(main_frame)
    style = ttk.Style()
    style.theme_use('default')

    style.configure("Treeview",
    background="#D3D3D3",
    foreground="black",
    rowheight=25,
    fieldbackground="#D3D3D3")

    style.map('Treeview',
    background=[('selected', "#347083")])
    f1 = Frame(main_frame)
    scroller = Scrollbar(f1)
    scroller.pack(side=RIGHT, fill=Y,pady="25")
    tree1 = ttk.Treeview(f1, yscrollcommand=scroller.set, selectmode="extended")
    tree1.pack(pady="25")
    f1.pack()
    scroller.config(command=tree1.yview)
    tree1['columns'] = ("Process ID", "Arrival Time", "Bursts")

    tree1.column("#0", width=0, stretch=NO)
    tree1.column("Process ID", anchor=CENTER, width=75)
    tree1.column("Arrival Time", anchor=CENTER, width=75)
    tree1.column("Bursts", anchor=CENTER, width=350)

    tree1.heading("#0", text="", anchor=W)
    tree1.heading("Process ID", text="Process ID", anchor=CENTER)
    tree1.heading("Arrival Time", text="Arrival Time", anchor=CENTER)
    tree1.heading("Bursts", text="Bursts", anchor=CENTER)
    
    data_frame = LabelFrame(f1, text="Data",pady="15")
    data_frame.pack(fill="x", padx=20)

    lb1 = Label(data_frame,text="# of Processes")
    lb1.grid(row=0,column=0, padx=10,pady=10)
    numOfProcesses = Entry(data_frame)
    numOfProcesses.grid(row=0,column=1, padx=10,pady=10)


    lb2 = Label(data_frame,text="Max Arrival Time")
    lb2.grid(row=0,column=2, padx=10,pady=10)
    maxArrival = Entry(data_frame)
    maxArrival.grid(row=0,column=3, padx=10,pady=10)
    lb3 = Label(data_frame,text="Max # of CPU Bursts")
    lb3.grid(row=1,column=0, padx=10,pady=10)
    maxBursts = Entry(data_frame)
    maxBursts.grid(row=1,column=1, padx=10,pady=10)
    lb4 = Label(data_frame,text="Min IO Duration")
    lb4.grid(row=2,column=0, padx=10,pady=10)
    minIO = Entry(data_frame)
    minIO.grid(row=2,column=1, padx=10,pady=10)
    lb5 = Label(data_frame,text="Max IO Duration")
    lb5.grid(row=2,column=2, padx=10,pady=10)
    maxIO = Entry(data_frame)
    maxIO.grid(row=2,column=3, padx=10,pady=10)
    lb6 = Label(data_frame,text="Min CPU Duration")
    lb6.grid(row=3,column=0, padx=10,pady=10)
    minCPU = Entry(data_frame)
    minCPU.grid(row=3,column=1, padx=10,pady=10)
    lb7 = Label(data_frame,text="Max CPU Duration")
    lb7.grid(row=3,column=2, padx=10,pady=10)
    maxCPU = Entry(data_frame)
    maxCPU.grid(row=3,column=3, padx=10,pady=10)

    generate = Button(data_frame,text="Generate WorkLoad",command= lambda : generateWorkLoad(int(numOfProcesses.get()),int(maxArrival.get()),int(maxBursts.get()),int(minCPU.get()),int(maxCPU.get()),int(minIO.get()),int(maxIO.get())))
    generate.grid(row=4,column=0,padx=10,pady=10)
    fillTrees(tree1)

def Processes(main_frame):
    deleteFrames(main_frame)

    f1 = Frame(main_frame)

    style = ttk.Style()
    style.theme_use('default')

    style.configure("Treeview",
    background="#D3D3D3",
    foreground="black",
    rowheight=25,
    fieldbackground="#D3D3D3")

    style.map('Treeview',
    background=[('selected', "#347083")])
    f1 = Frame(main_frame)
    scroller = Scrollbar(f1)
    scroller.pack(side=RIGHT, fill=Y,pady="25")
    tree = ttk.Treeview(f1, yscrollcommand=scroller.set, selectmode="extended")
    tree.pack(pady="25")
    f1.pack()
    scroller.config(command=tree.yview)
    tree['columns'] = ("Process ID", "Arrival Time", "Bursts")

    tree.column("#0", width=0, stretch=NO)
    tree.column("Process ID", anchor=CENTER, width=75)
    tree.column("Arrival Time", anchor=CENTER, width=75)
    tree.column("Bursts", anchor=CENTER, width=350)

    tree.heading("#0", text="", anchor=W)
    tree.heading("Process ID", text="Process ID", anchor=CENTER)
    tree.heading("Arrival Time", text="Arrival Time", anchor=CENTER)
    tree.heading("Bursts", text="Bursts", anchor=CENTER)
    
    data_frame = LabelFrame(f1, text="Data",pady="15")
    data_frame.pack(fill="x", padx=20)
    def addProcess(PP,ARR):
        if int(PP) not in [x.pid for x in processes]:
            processes.append(Process(int(PP),int(ARR),[]))

    lb1 = Label(data_frame,text="Processes ID").grid(row=0,column=0, padx=10,pady=10)
    PID = Entry(data_frame)
    PID.grid(row=0,column=1, padx=10,pady=10)
    lb2 = Label(data_frame,text="Arrival Time").grid(row=0,column=2, padx=10,pady=10)
    Arrival = Entry(data_frame)
    Arrival.grid(row=0,column=3, padx=10,pady=10)
    create = Button(data_frame,text="Create Process",command=lambda : addProcess(PID.get(),Arrival.get())).grid(row=0,column=4,padx=10,pady=10)

    burst_frame = LabelFrame(f1,text="Bursts",pady=25)
    burst_frame.pack(fill="x",padx=20)
    def addBurstToProcess(pid,amount):
        for i in processes:
            if i.pid == pid:
                i.bursts.append(amount)
    lb3 = Label(burst_frame,text="Process ID").grid(row=0,column=0, padx=10,pady=10)
    PID2 = Entry(burst_frame)
    PID2.grid(row=0,column=1, padx=10,pady=10)
    lb4 = Label(burst_frame,text="Burst Duration").grid(row=0,column=3, padx=10,pady=10)
    burst = Entry(burst_frame)
    burst.grid(row=0,column=4, padx=10,pady=10)
    addBurst = Button(burst_frame,text="Add Burst",command=lambda : addBurstToProcess(int(PID2.get()),int(burst.get())))
    addBurst.grid(row=1,column=0,padx=10,pady=10)

    fillTrees(tree)

def ghanttChart(q1,q2):
    for i in processes:
        i.q1 = q1
        i.q2 = q2
        i.printInfo()
    if True:
        q1 = False
        q2 = False
        q3 = False
        q4 = False

        Queue1 = []
        Queue2 = []
        Queue3 = []
        Queue4 = []
        io  = [] 
        History = [] 
        time = 0
        q3p = None
        maxArrival = 0
        currProcess = None
        cpuWork = 0
        for i in processes:
            if i.arrivaltime > maxArrival:maxArrival = i.arrivaltime

    while True: # SIMULATES CPU 
        for p in processes:
            if p.arrivaltime == time:
                Queue1.append(p) ; p.currentQueue = 1       
        if len(Queue1) == 0 and len(Queue2) == 0  and len(Queue3) == 0 and len(Queue4) ==0:
            q1 = False
            q2 = False
            q3 = False
            q4 = False
        if len(Queue1) != 0:
            q1 = True
            q2 = False
            q3 = False
            q4 = False
        if len(Queue1) == 0 and len(Queue2) != 0:
            q1 = False
            q2 = True
            q3 = False
            q4 = False
        if len(Queue1) == 0 and len(Queue2) == 0  and len(Queue3) != 0:
            q1 = False
            q2 = False
            q3 = True
            q4 = False
        if len(Queue1) == 0 and len(Queue2) == 0  and len(Queue3) == 0 and len(Queue4) !=0 :
            q1 = False
            q2 = False
            q3 = False
            q4 = True

        if q1: 
            p = Queue1[0]
            currProcess = p
            p.q1 -=1
            p.bursts[0]-=1
            cpuWork+=1
            History.append((p.pid,'RR1',time,'With Bursts',str(p.bursts)))
            if p.q1 == 0:
                Queue1.remove(p)
                Queue2.append(p)
                p.currentQueue = 2
        if q2:
            p = Queue2[0]
            currProcess = p
            p.q2 -=1   
            p.bursts[0]-=1
            cpuWork+=1
            History.append((p.pid,'RR2',time,'With Bursts ', str(p.bursts)))
            if p.q2 ==0:
                Queue2.remove(p)
                Queue3.append(p)
                p.currentQueue =3
        if q3:
            p = Queue3[0]
            Burst = p.bursts[0]
            cpuWork+=1
            for i in Queue3:
                    if i.bursts[0] < Burst: p = i ; Burst = i.bursts[0]
            currProcess = p
            if q3p != None and q3p in Queue3 and q3p.pid != p.pid :q3p.numOfInterrupt+=1 # ; print("PROCESS ", q3p.pid , 'Was just interrupted by ' , p.pid)
            if q3p !=  None and  q3p.numOfInterrupt == 3: 
                Queue3.remove(q3p)
                Queue4.append(q3p)
                q3p.currentQueue = 4
                #print("PROCESS ", q3p.pid,'HAD JUST GOT ITS THIRD INTERRUPT & GOING TO FCFS')
            
            p.bursts[0]-=1
            History.append((p.pid,'SRTF',time,'with bursts', str(p.bursts))) # (proc) if proc not in/in Queue3:
            q3p = p
        if q4:
            p = Queue4[0]
            currProcess = p 
            p.bursts[0]-=1
            cpuWork+=1
            History.append((p.pid,'FCFS',time, 'with bursts', str(p.bursts)))

        for i in processes:
            if i != currProcess and i not in io and (i in Queue1 or i in Queue2 or i in Queue3 or i in Queue4): 
                i.waiting +=1
                #print("Increase waiting for ", i.pid,'at time ',time)

        for i in io:
            i.bursts[1]-=1
            if i.bursts[1] == 0:
                if i.currentQueue == 1: Queue1.append(i) 
                elif i.currentQueue == 2: Queue2.append(i) 
                elif i.currentQueue == 3: Queue3.append(i) 
                elif i.currentQueue == 4:  Queue4.append(i)
                i.bursts = i.bursts[2:]
                i.flag = True

        for p in processes:
            if p.flag == True:
                io.remove(p)
                p.flag = False

        for i in processes:
            if i.bursts[0] == 0:
                if len(i.bursts) > 2 and i not in io:
                    io.append(i)
                if i.currentQueue == 1 and i in Queue1: Queue1.remove(i)
                elif i.currentQueue == 2 and i in Queue2: Queue2.remove(i)
                elif i.currentQueue == 3 and i in Queue3: Queue3.remove(i)
                elif i.currentQueue == 4 and i in Queue4:  Queue4.remove(i)

        time+=1
        if time > maxArrival and not q1 and not q2 and not q3 and not q4:break
        
    
    #for i in History:print(i)
    finalHistory = []
    finalHistory.append(History[0])
    index = 0 
    for i in range(len(History)):
        if i+1 == len(History) or i == 0:continue
        if (History[i][0] == History[i+1][0] and History[i][0] == History[i-1][0])  and (History[i][1] == History[i+1][1] and History[i][1] == History[i-1][1]) :continue
        if ( not History[i][0] == History[i+1][0] and not History[i][0] == History[i-1][0])  and (History[i][1] == History[i+1][1] and History[i][1] == History[i-1][1]) == False:
            finalHistory.append(History[i])
            finalHistory.append(History[i])
        else: finalHistory.append(History[i])

    finalHistory.append(History[-1])
    #for i in finalHistory:print(i)
    for i in processes:i.printInfo()
    print('CPU UTILIZATION = ', cpuWork/(time-1))
    sum = 0
    for i in processes: sum+=i.waiting
    print( "  Average Waiting Time ; ", sum/len(processes))

    GHANTT = []
    index = 0  
    while True:
        GHANTT.append((finalHistory[index][0], finalHistory[index][1], finalHistory[index][2] , finalHistory[index+1][2]+1  ))
        index +=2
        if index == len(finalHistory):break
    print(GHANTT)


    df = pd.DataFrame([   dict(Task="P "+str(x[0])+ ' '+str(x[1]),Start=x[2], Finish=x[3] ,Resource="Process"+str(x[0])) for x in GHANTT ])

    fig = ff.create_gantt(df, index_col = 'Resource',  bar_width = 0.4, show_colorbar=True,showgrid_x=True )
    fig.update_layout(xaxis_type='linear', autosize=False, width=800, height=400)
    fig.show()

def runn(q11,q22,pauseTime):
    for i in processes:
        i.q1 = q11
        i.q2 = q22
        i.printInfo()
    if True:
        q1 = False
        q2 = False
        q3 = False
        q4 = False

        Queue1 = []
        Queue2 = []
        Queue3 = []
        Queue4 = []
        io  = [] 
        History = [] 
        time = 0
        q3p = None
        maxArrival = 0
        currProcess = None
        cpuWork = 0
        for i in processes:
            if i.arrivaltime > maxArrival:maxArrival = i.arrivaltime

    while True: # SIMULATES CPU 
        if time ==  pauseTime:
            print("At time ", time )
            print('Queue #1 : ' , str (    [ "P" + str(x.pid) for x in Queue1  ] )  )
            print('Queue #2 : ' , str (    [ "P" + str(x.pid)  for x in Queue2  ] )  )
            print('Queue #3 : ' , str (    [ "P" + str(x.pid)  for x in Queue3  ] )  )
            print('Queue #4 : ' , str (    [ "P" + str(x.pid)  for x in Queue4  ] )  )
            print('I/O ' , str (    [ "P" + str(x.pid) for x in io  ] )  )
        for p in processes:
            if p.arrivaltime == time:
                Queue1.append(p) ; p.currentQueue = 1       
        if len(Queue1) == 0 and len(Queue2) == 0  and len(Queue3) == 0 and len(Queue4) ==0:
            q1 = False
            q2 = False
            q3 = False
            q4 = False
        if len(Queue1) != 0:
            q1 = True
            q2 = False
            q3 = False
            q4 = False
        if len(Queue1) == 0 and len(Queue2) != 0:
            q1 = False
            q2 = True
            q3 = False
            q4 = False
        if len(Queue1) == 0 and len(Queue2) == 0  and len(Queue3) != 0:
            q1 = False
            q2 = False
            q3 = True
            q4 = False
        if len(Queue1) == 0 and len(Queue2) == 0  and len(Queue3) == 0 and len(Queue4) !=0 :
            q1 = False
            q2 = False
            q3 = False
            q4 = True

        if q1: 
            p = Queue1[0]
            currProcess = p
            p.q1 -=1
            p.bursts[0]-=1
            cpuWork+=1
            History.append((p.pid,'RR1',time,'With Bursts',str(p.bursts)))
            if p.q1 == 0:
                Queue1.remove(p)
                Queue2.append(p)
                p.currentQueue = 2
        if q2:
            p = Queue2[0]
            currProcess = p
            p.q2 -=1   
            p.bursts[0]-=1
            cpuWork+=1
            History.append((p.pid,'RR2',time,'With Bursts ', str(p.bursts)))
            if p.q2 ==0:
                Queue2.remove(p)
                Queue3.append(p)
                p.currentQueue =3
        if q3:
            p = Queue3[0]
            Burst = p.bursts[0]
            cpuWork+=1
            for i in Queue3:
                    if i.bursts[0] < Burst: p = i ; Burst = i.bursts[0]
            currProcess = p
            if q3p != None and q3p in Queue3 and q3p.pid != p.pid :q3p.numOfInterrupt+=1 # ; print("PROCESS ", q3p.pid , 'Was just interrupted by ' , p.pid)
            if q3p !=  None and  q3p.numOfInterrupt == 3: 
                Queue3.remove(q3p)
                Queue4.append(q3p)
                q3p.currentQueue = 4
                #print("PROCESS ", q3p.pid,'HAD JUST GOT ITS THIRD INTERRUPT & GOING TO FCFS')
            
            p.bursts[0]-=1
            History.append((p.pid,'SRTF',time,'with bursts', str(p.bursts))) # (proc) if proc not in/in Queue3:
            q3p = p
        if q4:
            p = Queue4[0]
            currProcess = p 
            p.bursts[0]-=1
            cpuWork+=1
            History.append((p.pid,'FCFS',time, 'with bursts', str(p.bursts)))

        for i in processes:
            if i != currProcess and i not in io and (i in Queue1 or i in Queue2 or i in Queue3 or i in Queue4): 
                i.waiting +=1

        for i in io:
            i.bursts[1]-=1
            if i.bursts[1] == 0:
                if i.currentQueue == 1: Queue1.append(i) 
                elif i.currentQueue == 2: Queue2.append(i) 
                elif i.currentQueue == 3: Queue3.append(i) 
                elif i.currentQueue == 4:  Queue4.append(i)
                i.bursts = i.bursts[2:]
                i.flag = True

        for p in processes:
            if p.flag == True:
                io.remove(p)
                p.flag = False

        for i in processes:
            if i.bursts[0] == 0:
                if len(i.bursts) > 2 and i not in io:
                    io.append(i)
                if i.currentQueue == 1 and i in Queue1: Queue1.remove(i)
                elif i.currentQueue == 2 and i in Queue2: Queue2.remove(i)
                elif i.currentQueue == 3 and i in Queue3: Queue3.remove(i)
                elif i.currentQueue == 4 and i in Queue4:  Queue4.remove(i)
        time+=1
        if time > maxArrival and not q1 and not q2 and not q3 and not q4:break
    
    print('CPU UTILIZATION = ', cpuWork/(time-1))
    sum = 0
    for i in processes: sum+=i.waiting
    print( "  Average Waiting Time ; ", sum/len(processes))

def Simulator(main_frame):
    deleteFrames(main_frame)
    f1 = Frame(main_frame)
    f1.pack()
    
    opts_frame = LabelFrame(f1, text="System Options",pady="15")
    opts_frame.pack(fill="x", padx=20)

    lb10 = Label(opts_frame,text="Queue 1 Quatum")
    lb10.grid(row=0, column=0,padx=10,pady=10)
    Queue1Quantum = Entry(opts_frame)
    Queue1Quantum.grid(row=0, column=1,padx=10,pady=10)

    lb12 = Label(opts_frame,text="Queue 2 Quantum")
    lb12.grid(row=0, column=2,padx=10,pady=10)
    Queue2Quantum = Entry(opts_frame)
    Queue2Quantum.grid(row=0, column=3,padx=10,pady=10)

    RunSimulation = Button(opts_frame, text="Run Simulation" , command= lambda : runn(int(Queue1Quantum.get()),int(Queue2Quantum.get()) ,int(pause.get())))
    RunSimulation.grid(row=2, column=0,padx=10,pady=10)

    ghanttChartbt = Button(opts_frame,text="Gantt Chart" ,command= lambda : ghanttChart( int(Queue1Quantum.get()),int(Queue2Quantum.get())    ))
    ghanttChartbt.grid(row=2,column=1,padx=10,pady=10)

    lb77 = Label(opts_frame,text="Pause Time ")
    lb77.grid(row=1, column=0,padx=10,pady=10)
    pause = Entry(opts_frame)
    pause.grid(row=1, column=1,padx=10,pady=10)

def readFile():
    ps =  open('Workload.txt' , 'r').read().split('\n')
    for i in range(len(ps)):
        processes.append(Process( int(ps[i].split('\t')[0]),int(ps[i].split('\t')[1]), ps[i].split('\t')[2:]))

root = Tk()
root.title("CPU Multi Level Feedback Queue Simulator")
root.geometry("800x600+100+50")
global processes
processes = []
main_frame = Frame(root)
options_frame = LabelFrame(root,bg="#c3c3c3")

main_frame.grid(row=0,column=1 , padx=25,pady=25)
options_frame.grid(row=0,column=0,padx=25,pady=25)

btn1 = Button(options_frame, text="Work Load", command= lambda : WorkLoadGenerator(main_frame))
btn2 = Button(options_frame, text="Processes", command= lambda : Processes(main_frame))
btn3 = Button(options_frame, text="Simulator", command= lambda : Simulator(main_frame))
btn4 = Button(options_frame,text="Read File", command= readFile )
btn1.pack(pady=25,padx=10)
btn2.pack(pady=25,padx=10)
btn3.pack(padx=10,pady=25)
btn4.pack(padx=10,pady=25)
root.mainloop()