from visual import *
from visual.graph import *

a, b = 30, 30
scene = display(width=800, height=500)
scene.up = vector(0, 0, 1)
scene.autoscale = True
scene.forward = vector(-1, 1, -1)
scene.center = vector(20.6, 40.85, 0)
#scene.autocenter = True
CB=color.white
curve(pos = [vector(0, 0, 0), vector(a, 0, 0)], color=CB, radius=0.5)
curve(pos = [vector(0, 0, 0), vector(0, a, 0)], color=CB, radius=0.5)
curve(pos = [vector(0, 0, 0), vector(0, 0, a)], color=CB, radius=0.5)
label(pos = vector(40,-10,0), text='Y', color=CB, height=50, opacity=0)
label(pos = vector(-20,40,0), text='X', color=CB, height=50, opacity=0)
gdisplay(x=800, y=0,width=800, height=500, foreground=color.black, background=color.white, xtitle='t [sec]', ytitle = 'Vx [cm/sec]')

table = box(pos = vector(30.6, 60.95, -2), length = 121.9, height = 61.2, width = 4, color = color.green, axis = vector(0, 1, 0), material=materials.rough)
ball = sphere(pos = vector(30.6, 80, 1.805), radius = 1.805)

ball.velocity = vector(0.0, -224.0, 0.0)
ball.accel = vector(0.0, 0.0, 0.0)
ball.mass = 53.8 # 53.8 g
seconds = 0
dt = 0.01 # 0.01 sec
mu = 0.3  # friction coefficient
g = 979   # gravity in cgs units
vel = gcurve()

ic, fnum = 0, 0

while seconds <= 0.76:
    rate(20)
    seconds += dt
    ball.friction = -mu * ball.mass * g * norm(ball.velocity)
    ball.accel = ball.friction / ball.mass
    ball.pos = ball.pos + ball.velocity * dt
    ball.velocity = ball.velocity + ball.accel * dt
    vel.plot(pos = (seconds, ball.velocity.y))
    if ball.pos.y <= ball.radius:
        ball.velocity.y = -ball.velocity.y
        
