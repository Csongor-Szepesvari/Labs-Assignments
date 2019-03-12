import turtle
import time as t
COUNTER = 1
def Koch(length, order):
    global COUNTER
    '''
    order 0 Koch is just a straight line
    '''
    if order == 0:
        turtle.forward(length)
        #print("Times exe:", COUNTER)
        COUNTER+=1
    else:
        Koch(length, order-1)
        turtle.left(60)
        Koch(length, order-1)
        turtle.right(120)
        Koch(length, order-1)
        turtle.left(60)
        Koch(length, order-1)

#test
def main(times):
    global COUNTER
    COUNTER = 0
    across = 50
    #for each increase in recursion, length has to be divided by 3
    reductionRatio =  3 **(times-1)
    length = across/reductionRatio
    turtle.setworldcoordinates(-1, -1, 150, 150)
    turtle.tracer(0,0)
    turtle.penup()
    turtle.goto(0,0)
    turtle.pendown()
    turtle.speed(0)
    Koch(length, times)
    turtle.update()
    print(COUNTER)
    #turtle.mainloop()
      
start = t.time()    
main(8)
print("4^8 takes %.2f seconds" % (t.time()-start))
start = t.time()
main(3)
print("4^3 takes %.2f seconds" % (t.time()-start))
start = t.time()
main(1)
print("4^1 takes %.2f seconds" % (t.time()-start))