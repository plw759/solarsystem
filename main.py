from ursina import *
from ursina.shaders import lit_with_shadows_shader
import numpy as np


class Sky(Entity):
    def __init__(self, **kwargs):
        from ursina.shaders import unlit_shader
        super().__init__(
            parent = render,
            name = 'sky',
            model = 'sky_dome',
            texture = "milk",
            scale = 9900,
            shader = unlit_shader,
            )
        for key, value in kwargs.items():
            setattr(self, key, value)

    def update(self):
        self.world_position = camera.world_position


def update():
    global t
    global dt

    t = t + dt
    angle = np.pi * 40 / 180
    factor = 10
    ellipse = 1.4
    radius_1 = 10 * factor
    mercury.x = np.cos(4*t) * radius_1 * 1.2
    mercury.z = np.sin(4*t) * radius_1

    radius_2 = 12 * factor
    venus.x = np.cos(2*t + angle) * radius_2 * 1.2
    venus.z = np.sin(2*t + angle) * radius_2

    radius_3 = 15 * factor
    earth.x = np.cos(t + angle * 2) * radius_3 * 1.2
    earth.z = np.sin(t + angle * 2) * radius_3
    clouds.x = np.cos(t + angle * 2) * radius_3 * 1.2
    clouds.z = np.sin(t + angle * 2) * radius_3
    moon.x = np.cos(t + angle * 2)
    moon.z = np.sin(t + angle * 2)

    radius_4 = 18 * factor
    mars.x = np.cos(.6*t + angle * 3) * radius_4 * 1.2
    mars.z = np.sin(.6*t + angle * 3) * radius_4

    radius_5 = 32 * factor
    jupiter.x = np.cos(.2*t + angle * 4) * radius_5 * ellipse
    jupiter.z = np.sin(.2*t + angle * 4) * radius_5

    radius_6 = 45 * factor
    saturn.x = np.cos(.08*t + angle * 5) * radius_6 * ellipse
    saturn.z = np.sin(.08*t + angle * 5) * radius_6

    radius_7 = 59 * factor
    uranus.x = np.cos(.02*t + angle * 6) * radius_7 * ellipse
    uranus.z = np.sin(.02*t + angle * 6) * radius_7

    radius_8 = 80 * factor
    neptune.x = np.cos(.01*t + angle * 7) * radius_8 * ellipse
    neptune.z = np.sin(.01*t + angle * 7) * radius_8

    radius_9 = 100 * factor
    pluto.x = np.cos(.005*t + angle * 8) * radius_9 * ellipse
    pluto.z = np.sin(.005*t + angle * 8) * radius_9

    earth.rotation_y += dt * 1000
    earth.rotation_z += dt * 10000
    clouds.rotation_y += dt * 1000
    clouds.rotation_z += dt * 10000
    jupiter.rotation_y += dt * 100
    mercury.rotation_y = earth.rotation_y
    venus.rotation_y = earth.rotation_y
    mars.rotation_y = earth.rotation_y
    saturn.rotation_y = jupiter.rotation_y
    uranus.rotation_x = jupiter.rotation_y
    neptune.rotation_y = jupiter.rotation_y
    earth.rotation_x = 21.5;
    earth.rotation_z = 5.5;
    clouds.rotation_x = 21.5;
    clouds.rotation_z = 5.5;
    saturn.rotation_z = 2;
    jupiter.rotation_x = 2;
    uranus.rotation_x = 98;
    neptune.rotation_z = 3;
    global textureOffset  # Inform we are going to use the variable defined outside this function
    textureOffset += time.dt * 0.01  # Increment this variable just a little based on the time
    setattr(sun, "texture_offset", (textureOffset, textureOffset))  # Assign the new texture offset to the entity
    global textureOffset2  # Inform we are going to use the variable defined outside this function
    textureOffset2 += time.dt * 0.02  # Increment this variable just a little based on the time
    setattr(sun2, "texture_offset", (textureOffset2, textureOffset2))  # Assign the new texture offset to the entity
    setattr(clouds, "texture_offset", (0, textureOffset2))


def input(key):
    global dt
    global save
    global t
    if key == 'left mouse down':
        B.visible = False
        C.visible = False
        D.visible = False
        E.visible = False
    if key == 'e':
        if dt == 0:
            dt = save
        else:
            dt *= 1.3
    if key == 'q' and dt != 0:
        save = dt
        dt = 0
    if key == 'r':
        t = 0
        dt = .0005
        save = 0


app = Ursina(vsync=True)
dt = 0.0005
save = 0
textureOffset = 0.0
textureOffset2 = 0.0
Cursor(texture='cursor')
mouse.visible = False
b = []
B = Button(text='   hello world!', color=color.clear, scale=.40, text_origin=(0, .2))
C = Button(text='   e: speed up!', color=color.clear, scale=.40, text_origin=(0, -.2))
D = Button(text='   q: slow down!', color=color.clear, scale=.40, text_origin=(0, -.4))
E = Button(text='   r: reset!', color=color.clear, scale=.40, text_origin=(0, 0))
b.append(B)
b.append(C)
b.append(D)
b.append(E)


window.title = 'Patrick\'s Solar System'
sun = Entity(model='sphere', color=color.white, scale=120,texture="sun", shader=lit_with_shadows_shader)
sun2 = Entity(model='sphere', color=color.rgba(255,255,255,180), scale=121,texture="sun", shader=lit_with_shadows_shader)
sun3 = Entity(model='sphere', color=color.rgba(255,255,255,60), scale=122,texture="sun", shader=lit_with_shadows_shader)

mercury = Entity(model='sphere', color=color.smoke, scale=3.8,texture="mercury", shader=lit_with_shadows_shader)
venus = Entity(model='sphere', color=color.smoke, scale=9.5,texture="venus", shader=lit_with_shadows_shader)
earth = Entity(model='sphere', color=color.smoke, scale=10.0,texture="earth", shader=lit_with_shadows_shader)
clouds = Entity(model='sphere', color=color.rgba(100,100,100,100), scale=10.1,texture="earth_clouds", shader=lit_with_shadows_shader)
moon = Entity(parent=earth, model='sphere', color=color.gray, scale=.3,texture="moon", shader=lit_with_shadows_shader)
mars = Entity(model='sphere', color=color.light_gray, scale=5.2,texture="mars", shader=lit_with_shadows_shader)
jupiter = Entity(model='sphere', color=color.gray, scale=33.0,texture="jupiter", shader=lit_with_shadows_shader)
saturn = Entity(model='sphere', color=color.gray, scale=30,texture="saturn", shader=lit_with_shadows_shader)
rings = Entity(parent=saturn, model=Cylinder(100, 1.05, -.01, height=.004), color=color.rgba(119,136,153,220),shader=lit_with_shadows_shader)
rings2 = Entity(parent=saturn, model=Cylinder(100, .95, -.01, height=.005), color=color.rgba(20,20,25,220),shader=lit_with_shadows_shader)
rings3 = Entity(parent=saturn, model=Cylinder(100, .90, -.01, height=.006), color=color.rgba(119,136,153,220) ,shader=lit_with_shadows_shader)
rings4 = Entity(parent=saturn, model=Cylinder(100, .87, -.01, height=.007), color=color.rgba(100,100,100,160),shader=lit_with_shadows_shader)
rings5 = Entity(parent=saturn, model=Cylinder(100, .82, -.01, height=.008), color=color.rgba(119,136,153,220) ,shader=lit_with_shadows_shader)
rings6 = Entity(parent=saturn, model=Cylinder(100, .75, -.01, height=.009), color=color.rgba(119,121,121,220),shader=lit_with_shadows_shader)
rings7 = Entity(parent=saturn, model=Cylinder(100, .70, -.01, height=.01), color=color.rgba(0,0,0,220),shader=lit_with_shadows_shader)
uranus = Entity(model='sphere', color=color.gray, scale=28, texture="uranus", shader=lit_with_shadows_shader)
neptune = Entity(model='sphere', color=color.gray, scale=30, texture="neptune", shader=lit_with_shadows_shader)
pluto = Entity(model='sphere', color=color.gray, scale=3, texture="download", shader=lit_with_shadows_shader)

t = -np.pi
entities = [earth, moon]
glow = SpotLight(parent=sun2, y=1, z=2, shadows=True)
glow.look_at((1,-1,-1))
glow2 = SpotLight(parent=sun2, y=1, z=2, shadows=True)
glow2.look_at((1,-1,-1))
glow3 = SpotLight(parent=sun2, y=1, z=2, shadows=True)
glow3.look_at((1,-1,-1))
glow4 = SpotLight(parent=sun2, y=1, z=2, shadows=True)
glow4.look_at((1,-1,-1))
glow5 = SpotLight(parent=sun2, y=1, z=2, shadows=True)
glow5.look_at((1,-1,-1))
glow6 = SpotLight(parent=sun2, y=1, z=2, shadows=True)
glow6.look_at((1,-1,-1))
glo = SpotLight(parent=sun2, y=1, z=2, shadows=True)
glo.look_at((1,-1,-1))
glo2 = SpotLight(parent=sun2, y=1, z=2, shadows=True)
glo2.look_at((1,-1,-1))
glo3 = SpotLight(parent=sun2, y=1, z=2, shadows=True)
glo3.look_at((1,-1,-1))
glo4 = SpotLight(parent=sun2, y=1, z=2, shadows=True)
glo4.look_at((1,-1,-1))
glo5 = SpotLight(parent=sun2, y=1, z=2, shadows=True)
glo5.look_at((1,-1,-1))
glo6 = SpotLight(parent=sun2, y=1, z=2, shadows=True)
glo6.look_at((1,-1,-1))
gl = SpotLight(parent=sun2, y=1, z=2, shadows=True)
gl.look_at((1,-1,-1))
gl2 = SpotLight(parent=sun2, y=1, z=2, shadows=True)
gl2.look_at((1,-1,-1))
gl3 = SpotLight(parent=sun2, y=1, z=2, shadows=True)
gl3.look_at((1,-1,-1))
gl4 = SpotLight(parent=sun2, y=1, z=2, shadows=True)
gl4.look_at((1,-1,-1))
gl5 = SpotLight(parent=sun2, y=1, z=2, shadows=True)
gl5.look_at((1,-1,-1))
gl6 = SpotLight(parent=sun2, y=1, z=2, shadows=True)
gl6.look_at((1,-1,-1))
Sky()
EditorCamera()
app.run()