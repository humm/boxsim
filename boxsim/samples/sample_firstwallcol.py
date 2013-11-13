import testenv
import boxsim
from common import cfg

cfg.toys.ball1.friction    = 0.0
cfg.toys.ball1.restitution = 2.0
cfg.toys.ball1.density     = 0.2

cfg.sprimitive.name = 'collisions'
cfg.sprimitive.setA = ['ball1']
cfg.sprimitive.setB = ['wallN', 'wallS', 'wallE', 'wallW']

box = boxsim.Simulation(cfg)

print(box.execute_order([0.685, 0.581, 0.725, 0.271, 0.752, 0.425, 0.252, 0.756, 0.262, 0.083, 0.290, 0.712, 0.0]))
print(box.execute_order([0.685, 0.581, 0.725, 0.271, 0.752, 0.425, 0.252, 0.756, 0.262, 0.083, 0.290, 0.712, 0.699]))
print(box.execute_order([0.580, 0.641, 0.423, 0.792, 0.456, 0.523, 0.603, 0.284, 0.105, 0.187, 0.617, 0.271, 0.507]))

box.close()