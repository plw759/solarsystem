from ursina import *
from ursina.shaders import lit_with_shadows_shader
from ursina.shaders import basic_lighting_shader
from ursina.shaders import projector_shader
from ursina.shaders import matcap_shader
import numpy as np
texoffset = 0.0
texoffset2 = 0.0
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

    t = t + 0.005
    angle = np.pi * 40 / 180
    factor = 10
    ellipse = 1.4
    radius_1 = 10 * factor
    mercury.x = np.cos(4*t) * radius_1 * ellipse
    mercury.z = np.sin(4*t) * radius_1

    radius_2 = 12 * factor
    venus.x = np.cos(2*t + angle) * radius_2 * ellipse
    venus.z = np.sin(2*t + angle) * radius_2

    radius_3 = 15 * factor
    earth.x = np.cos(t + angle * 2) * radius_3 * ellipse
    earth.z = np.sin(t + angle * 2) * radius_3

    moon.x = np.cos(t + angle * 2)
    moon.z = np.sin(t + angle * 2)

    radius_4 = 18 * factor
    mars.x = np.cos(.6*t + angle * 3) * radius_4 * ellipse
    mars.z = np.sin(.6*t + angle * 3) * radius_4

    radius_5 = 29 * factor
    jupiter.x = np.cos(.2*t + angle * 4) * radius_5 * ellipse
    jupiter.z = np.sin(.2*t + angle * 4) * radius_5

    radius_6 = 36 * factor
    saturn.x = np.cos(.08*t + angle * 5) * radius_6 * ellipse
    saturn.z = np.sin(.08*t + angle * 5) * radius_6

    radius_7 = 49 * factor
    uranus.x = np.cos(.02*t + angle * 6) * radius_7 * ellipse
    uranus.z = np.sin(.02*t + angle * 6) * radius_7

    radius_8 = 59 * factor
    neptune.x = np.cos(.01*t + angle * 7) * radius_8 * ellipse
    neptune.z = np.sin(.01*t + angle * 7) * radius_8

    radius_9 = 66 * factor
    pluto.x = np.cos(.005*t + angle * 8) * radius_9 * ellipse
    pluto.z = np.sin(.005*t + angle * 8) * radius_9

    for entity in entities:  # Go through the cube list
        entity.rotation_y += time.dt * 100  # Rotate all the cubes every time update is called
    global texoffset  # Inform we are going to use the variable defined outside this function
    texoffset += time.dt * 0.01  # Increment this variable just a little based on the time
    setattr(sun, "texture_offset", (texoffset,texoffset))  # Assign the new texture offset to the entity
    global texoffset2  # Inform we are going to use the variable defined outside this function
    texoffset2 += time.dt * 0.02  # Increment this variable just a little based on the time
    setattr(sun2, "texture_offset", (texoffset2, texoffset2))  # Assign the new texture offset to the entity
app = Ursina(vsync=True)

Cursor(texture = 'cursor' )
mouse.visible = False
b = Button(text='hello world!', scale=.40, text_origin=(0,0))
def input(key):
    if key == 'left mouse down':
        b.visible = False

window.title = 'Patrick\'s Solar System'


sun = Entity(model='sphere', color=color.white, scale=120,texture="sun", shader=lit_with_shadows_shader)
sun2 = Entity(model='sphere', color=color.rgba(255,255,255,180), scale=121,texture="sun", shader=lit_with_shadows_shader)
sun3 = Entity(model='sphere', color=color.rgba(255,255,255,60), scale=122,texture="sun", shader=lit_with_shadows_shader)

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


mercury = Entity(model='sphere', color=color.smoke, scale=3.8,texture="mercury", shader=lit_with_shadows_shader)
venus = Entity(model='sphere', color=color.smoke, scale=9.5,texture="venus", shader=lit_with_shadows_shader)
earth = Entity(model='sphere', color=color.white, scale=10.0,texture="earth", shader=lit_with_shadows_shader)
moon = Entity(parent=earth, model='sphere', color=color.white, scale=.3,texture="mercury", shader=lit_with_shadows_shader)

mars = Entity(model='sphere', color=color.light_gray, scale=5.2,texture="mars", shader=lit_with_shadows_shader)

jupiter = Entity(model='sphere', color=color.gray, scale=33.0,texture="jupiter", shader=lit_with_shadows_shader)
saturn = Entity(model='sphere', color=color.gray, scale=30,texture="saturn", shader=lit_with_shadows_shader)
uranus = Entity(model='sphere', color=color.gray, scale=28,texture="uranus", shader=lit_with_shadows_shader)
neptune = Entity(model='sphere', color=color.gray, scale=30,texture="neptune", shader=lit_with_shadows_shader)
pluto = Entity(model='sphere', color=color.gray, scale=3,texture="download", shader=lit_with_shadows_shader)

t = -np.pi
entities=[]
entities.append(earth)
entities.append(moon)

Sky()
EditorCamera()
app.run()