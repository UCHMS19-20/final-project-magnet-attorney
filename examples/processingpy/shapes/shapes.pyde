hue = 0
    

def setup():
    global path
    size(600,400)
    background(0)
    colorMode(HSB, 360, 100, 100)
    # create shape
    path = createShape()
    path.beginShape()
    path.fill(color(0,0,100))
    path.stroke(0)
    path.strokeWeight(3)
    path.vertex(0,10)
    path.vertex(50, 80)
    path.vertex(40,20)
    path.vertex(0,10)
    path.endShape()

def draw():
    global hue
    global path
    background(hue, 100, 100)
    hue += 1
    if hue > 360:
        hue = 0
    
    shape(path)
    print(mouseX)
    
    if mouseX > width/2:
        path.setFill(color(0,0,0))
    else:
        path.setFill(color(0,0,100))
