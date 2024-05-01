import rotatescreen
screen = rotatescreen.get_primary_display()

if(screen.current_orientation==180):
    screen.rotate_to(0)
    print("Screen Rotated")
else:
    screen.rotate_to(180)
    print("Screen Rotated")