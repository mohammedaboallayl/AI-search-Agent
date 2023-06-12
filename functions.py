def AvailableMoves(puzzle):  #function that diplay puzzle
    Moves= []
    colindex=(puzzle.index(0)+1)%3    #in this line we check position so we can determine which moves is available
    rowindex=(int((puzzle.index(0))/3))%3
    if colindex !=0:
        Moves.append('>')
    if colindex !=1:
        Moves.append('<')
    if rowindex !=0:
        Moves.append('^')
    if rowindex !=2:
        Moves.append('v')
    return Moves


def display(puzzle):
    for [index,num] in enumerate(puzzle):  #displaying puzzle for determined shape
        if (index)%3==0 and index >2:
            print("\n------------")
        if num==0:
            print("   |" ,end="")
        else:
            print(f" {num} |" ,end='')


def SelectInput(Moves): #select input from user in recursive way for more optimization in code
    inputstr=input(f"\nselect One Move : {Moves}")
    if inputstr in Moves:
        return inputstr
    else:
        return SelectInput(Moves)


def ChangePuzzle(puzzle,inputstr): # used to change puzzle list for next shape after user input is detected
    colindex=(puzzle.index(0)+1)%3
    rowindex=(int((puzzle.index(0)+1)/3))%3
    if inputstr=='>':
        if colindex !=0:
            index=puzzle.index(0)
            puzzle[index],puzzle[index+1]=puzzle[index+1],puzzle[index]

    elif inputstr=='<':
        if colindex !=1:
            index=puzzle.index(0)
            puzzle[index],puzzle[index-1]=puzzle[index-1],puzzle[index]
    elif inputstr=='^':
        index=puzzle.index(0)
        puzzle[index],puzzle[index-3]=puzzle[index-3],puzzle[index]
    elif inputstr=='v':
        index=puzzle.index(0)
        puzzle[index],puzzle[index+3]=puzzle[index+3],puzzle[index]

    return puzzle

def Check(puzzle): #check if puzzel have been solved or not
    state=False
    for i in range(8):
        if puzzle[i]>puzzle[i+1]:# this see if list is not sorted makes break and state is true
            state=True
            break

    return state
