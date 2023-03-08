#!/usr/bin/env python
# coding: utf-8

# In[28]:


filled = 0
number = 30
row = 0
tempFilled = -1

def construct(seatsGrid):
    seats = []
    for i in seatsGrid:
        rows = i[1]
        cols = i[0]
        # mat = [[-1]*cols]*rows
        mat = []
        for i in range(rows):
            mat.append([-1]*cols)
        seats.append(mat)
    return seats

def printSeats(seats):
    blksize = len(str(number))
    rows = [x[1] for x in seatsGrid]
    cols = [x[0] for x in seatsGrid]
    maximum = max(rows)
    top = True
    for i in range(maximum):
        rowlist = []
        rowlistl = []
        for j in range(length):
            row = ' '
            rowl = ' '
            if len(seats[j]) <= i:
                for k in range(cols[j]):
                    row += ' '*blksize
                    rowl += ' '*blksize
                    row += ' '
                    rowl += ' '
            else:
                row = '|'
                rowl = '+'
                for k in seats[j][i]:
                    if k == -1:
                        row += ' '*blksize
                        rowl += '-'*blksize
                        row += '|'
                        rowl += '+'
                    else:
                        row += str(k)+(' '*(blksize - len(str(k))))
                        rowl += '-'*blksize
                        row += '|'
                        rowl += '+'
            
            rowlist.append(row)
            rowlistl.append(rowl)
        if top:
            print('    '.join(rowlistl))
            top = False
        print('    '.join(rowlist))
        print('    '.join(rowlistl))

                
def fill_aisle_seats():
    # filled = 0
    global filled
    row = 0
    tempFilled = -1
    while filled < number and filled != tempFilled:
        tempFilled = filled
        for i in range(length):
            if seatsGrid[i][1] > row:
                if i == 0 and seatsGrid[i][0] > 1:
                    filled += 1
                    aisleCol = seatsGrid[i][0] - 1
                    seats[i][row][aisleCol] = filled
                    if filled >= number:
                        break
                elif i == length - 1 and seatsGrid[i][0] > 1:
                    filled += 1
                    aisleCol = 0
                    seats[i][row][aisleCol] = filled
                    if filled >= number:
                        break
                else:
                    filled += 1
                    aisleCol = 0
                    seats[i][row][aisleCol] = filled
                    if filled >= number:
                        break
                    if seatsGrid[i][0] > 1:
                        filled += 1
                        aisleCol = seatsGrid[i][0] - 1
                        seats[i][row][aisleCol] = filled
                        if filled >= number:
                            break
        row += 1


def fill_window_seats():
    row = 0
    global filled
    global number
    tempFilled = 0
    while filled < number and filled != tempFilled:
        tempFilled = filled
        if seatsGrid[0][1] > row:
            filled += 1
            window = 0
            seats[0][row][window] = filled
            if filled >= number:
                break
        if seatsGrid[length-1][1] > row:
            filled += 1
            window = seatsGrid[length-1][0] - 1
            seats[length-1][row][window] = filled
            if filled >= number:
                break
        row += 1

def fill_middle_seats():
    row = 0
    tempFilled = 0
    global filled
    while filled < number and filled != tempFilled:
        tempFilled = filled
        for i in range(length):
            if seatsGrid[i][1] > row:
                if seatsGrid[i][0] > 2:
                    for col in range(1, seatsGrid[i][0] - 1):
                        filled += 1
                        seats[i][row][col] = filled
                        if filled >= number:
                            break
        row += 1


seatsGrid = [[3,2], [4,3], [2,3], [3,4]]
seats = construct(seatsGrid)
# print seats
length = len(seatsGrid)


# Aisle
fill_aisle_seats()

# Window

fill_window_seats()

# Center
row = 0
tempFilled = 0
fill_middle_seats()


printSeats(seats)


# In[30]:


#global variables

num_pass=int(input("Number of passengers:"))   # number of passengers in waiting queue
filled_seats=0

def printarrangement(seats):
    size = len(str(num_pass))
    rows = [y[1] for y in seats_arrg]
    cols = [y[0] for y in seats_arrg]
    maximum = max(rows)
    top = True
    for i in range(maximum):
        rowlist = []
        rowlist1= []
        for j in range(length):
            row = ' '
            rowl = ' '
            if len(seats[j]) <= i:
                for k in range(cols[j]):
                    row += ' '*size
                    rowl += ' '*size
                    row += ' '
                    rowl += ' '
            else:
                row = '|'
                rowl = '+'
                for k in seats[j][i]:
                    if k == -1:
                        row += ' '*size
                        rowl += '-'*size
                        row += '|'
                        rowl += '+'
                    else:
                        row += str(k)+(' '*(size - len(str(k))))
                        rowl += '-'*size
                        row += '|'
                        rowl += '+'
            
            rowlist.append(row)
            rowlist1.append(rowl)
        if top:
            print('    '.join(rowlist1))
            top = False
        print('    '.join(rowlist))
        print('    '.join(rowlist1))



def arrange(seats_arrg):
    seats=[]
    for i in seats_arrg:
        mat=[]
        col=i[0]
        row=i[1]
        mat=[[-1 for j in range(col)] for i in range(row)]
        seats.append(mat)
    return seats

def filling_aisle():
    
    global filled_seats
    row=0 #this used to traverse from first row to last row
    temp=-1
    while filled_seats < num_pass and filled_seats!=temp:  # the loop terminates if we filled all seats or there are no  
                                                         # aisle seats to fill
        temp=filled_seats
        for i in range(length):  #to fill seats from first row to last row
            if seats_arrg[i][1] > row :  #we have different number of rows in each grid
                
                if i==0 and seats_arrg[i][0] > 1 :    #if we are in first grid of seats where only on right we have aisle seats
                    filled_seats += 1
                    aisle_pos=seats_arrg[i][0]-1    #last column of block
                    seats[i][row][aisle_pos]=filled_seats   #allocating passenger 
                    if filled_seats >= num_pass :
                        break
                elif i==length-1 and seats_arrg[i][0]>1:  # last grid of seats aisle seats only on left
                    filled_seats += 1
                    aisle_pos=0
                    seats[i][row][aisle_pos]=filled_seats
                    if filled_seats >=  num_pass :
                        break
                else:         # for grids in middle fill both aisle seats on left and right
                    filled_seats += 1
                    aisle_pos=0
                    seats[i][row][aisle_pos]=filled_seats
                    if filled_seats >= num_pass:
                        break
                    if seats_arrg[i][0] > 1:
                        filled_seats += 1
                        aisle_pos=seats_arrg[i][0]-1 
                        seats[i][row][aisle_pos]=filled_seats
                        if filled_seats >= num_pass :
                            break
        row+=1
    
def filling_window():
    # only first and last grids have window seats
    global filled_seats
    temp=0
    row=0
    while filled_seats < num_pass and filled_seats!=temp:    
                                                        
        temp=filled_seats
        if seats_arrg[0][1] > row :
            filled_seats+=1
            win_pos=0
            seats[0][row][win_pos]=filled_seats
            if filled_seats >= num_pass :
                            break
        if seats_arrg[length-1][1] > row:
            filled_seats+=1
            win_pos = seats_arrg[length-1][0] - 1
            seats[length-1][row][win_pos]=filled_seats
            if filled_seats >= num_pass :
                            break
        
        row += 1
    
def filling_center():
    global filled_seats
    temp=0
    row=0
    while filled_seats < num_pass and filled_seats!=temp:  
        
        temp=filled_seats
        for x in range(length):
            if seats_arrg[x][1] > row:
                if seats_arrg[x][0] > 2:
                    for column in range(1,seats_arrg[x][0]-1):
                        filled_seats+=1
                        #seats[x][row][column]=filled_seats
                        if filled_seats > num_pass :
                            break
                        seats[x][row][column]=filled_seats
        row+=1
    
# grid to arrange seats in airplane

seats_arrg=[[3,4], [4,5], [2,3], [3,4]]

# index 0- columns number
# index 1-row number for each grid

# here in arrange function we are assigning -1 to each seat to differentiate
#between allocated and not allocated seats

seats=arrange(seats_arrg)

'''now we start filling the seats in order:
      1.aisle
      2.window
      3.center   '''

length=len(seats_arrg)

#for aisle seats
filling_aisle()

#for window seats
filling_window()

#for center
filling_center()

#we are printing seat arrangement as a grid

printarrangement(seats)
      
      


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




