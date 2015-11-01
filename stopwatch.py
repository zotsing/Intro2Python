# template for "Stopwatch: The Game"
#j.z. 10/31/15
import simplegui

# define global variables
canvas_w = 400
canvas_h = 400
interval = 100
time = 0
counts  = 0
success = 0 
isRun    = False
# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):  
    tenth_sec = t % 10
    sec       = (t / 10) % 60
    minute    = (t / 600)% 600
    message = '%d:%02d.%d' % (minute, sec, tenth_sec)
    return message 
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global isRun
    isRun = True
    timer.start()
    
def stop():
    global isRun, counts, success, time
    if isRun:
        isRun = False 
        counts += 1
        if time % 10 == 0:
            success += 1
    timer.stop()  
    
def reset(): 
    global isRun, counts, success, time
    isRun  = False
    counts = 0
    success = 0
    time    = 0
    timer.stop() 

# define event handler for timer with 0.1 sec interval
def tick():
    global time
    time += 1
    
# define draw handler
def draw(canvas):
    canvas.draw_text("StopWatch", (canvas_w/4, canvas_h*0.4), 44,'white')
    canvas.draw_text(format(time), (canvas_w * 0.4, canvas_h*0.6), 44,'white')
    canvas.draw_text(str(success) + '/' + str(counts), (canvas_w*0.75, canvas_h*0.15), 44, 'red')
    
# create frame
frame = simplegui.create_frame("StopWatch Game", canvas_w, canvas_h)
timer = simplegui.create_timer(interval, tick) 

# register event handlers
frame.add_button("Start", start, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("Reset", reset, 100)
frame.set_draw_handler(draw) 

# start frame
frame.start()


