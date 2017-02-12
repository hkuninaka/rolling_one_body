from visual import *
from PIL import ImageGrab   # PIL
from subprocess import call # for issuing commands

a, b = 10, 10
scene = canvas(width=800, height=400)
scene.up = vector(0, 0, 1)
scene.autoscale = True
scene.forward = vector(-1, 1, -1)
scene.center = vector(30.6, 60.85, 0)
CB=color.white
curve(pos = [vector(0, 0, 0), vector(a, 0, 0)], color=CB)
curve(pos = [vector(0, 0, 0), vector(0, a, 0)], color=CB)
curve(pos = [vector(0, 0, 0), vector(0, 0, a)], color=CB)
#graph(width=600, height=400, foreground=color.black, background=color.white)

table = box(pos = vector(30.6, 60.95, -2), length = 121.9, height = 61.2, width = 4, color = color.green, axis = vector(0, 1, 0))
ball = sphere(pos = vector(30.6, 80, 1.805), radius = 1.805)

ball.velocity = vector(0.0, -224.0, 0.0)
ball.accel = vector(0.0, 0.0, 0.0)
ball.mass = 53.8 # 53.8 g
seconds = 0
dt = 0.01 # 0.01 sec
mu = 0.3  # friction coefficient
g = 979   # gravity in cgs units
#vel = gcurve()

ic, fnum = 0, 0

while True:
    rate(20)
    seconds += dt
    ball.friction = -mu * ball.mass * g * norm(ball.velocity)
    ball.accel = ball.friction / ball.mass
    ball.pos = ball.pos + ball.velocity * dt
    ball.velocity = ball.velocity + ball.accel * dt
#    vel.plot(pos = (seconds, ball.velocity.y))
    if ball.pos.y <= ball.radius:
        ball.velocity.y = -ball.velocity.y
    
    if (fnum >= 200): 
        break
    elif (ic%20 == 0):      # grab every 20 iterations, may need adjustment
        im = ImageGrab.grab(bbox = (10, 10, 400, 400))
        num = '00'+repr(fnum)           # sequence num 000-00999, trunc. below
        im.save('img-'+num[-3:]+'.png') # save to png file, 000-999, 3 digits
        fnum += 1
    ic += 1

# if the program cannot find "ffmpeg", check its path. can also replace it with "movie.bat"
call("ffmpeg -r 20 -i img-%3d.png -vcodec libx264 -vf format=yuv420p,scale=412:412 -y movie.mp4")
print ("\n Movie made: movie.mp4")
