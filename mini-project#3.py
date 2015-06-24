"""
"Stopwatch: The Game"
"""

import simplegui

time = 0
successful_stops = 0
total_stops = 0

def format(t):
    """
    Converts time in tenths of seconds into formatted 
    string A:BC.D
    """
    a = t / 600
    b = t % 600 / 100
    c = t % 600 / 10 % 10
    d = t % 10
    return str(a) + ':' + str(b) + str(c) + '.' + str(d)

def score():
    """
    Returns string with the current score
    """
    return str(successful_stops) + "/" + str(total_stops)
        
def start():
    """
    Event handler for "Start" button
    """
    timer.start()
    
def stop():
    """
    Event handler for "Stop" button
    """
    global successful_stops, total_stops
    if timer.is_running():
        if time % 10 == 0:
            successful_stops += 1
        total_stops += 1
        timer.stop()
    
def reset():
    """
    Event handler for "Reset" button
    """
    global time, successful_stops, total_stops
    timer.stop()
    time = 0
    successful_stops = 0
    total_stops = 0

def tick():
    """
    Event handler for timer with 0.1 sec interval
    """
    global time
    time += 1
    

def draw(canvas):
    """
    Draw handler
    """
    canvas.draw_text(format(time), [100, 105], 48, "White")
    canvas.draw_text(score(), [240, 30], 32, "Green")

    
# Create frame
frame = simplegui.create_frame("StopWatch", 300, 200)

# Create timer
timer = simplegui.create_timer(100, tick)

# Register event handlers
frame.set_draw_handler(draw)
frame.add_button("Start", start, 120)
frame.add_button("Stop", stop, 120)
frame.add_button("Reset", reset, 120)


# Start frame
frame.start()
