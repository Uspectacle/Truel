import numpy as np
import matplotlib.pyplot as plt
import os
import shutil

def ShootFirst(winner, looser):
  return winner / (winner + looser * (1 - winner))

def ShootSecond(winner, looser):
  return winner * (1 - looser) / (looser + winner * (1 - looser))

def BobKillCharlie(a, b, c):
  return ShootFirst(b, c)

def CharlieKillBob(a, b, c):
  return ShootSecond(c, b)

def AliceKillBobIfBobKillCharlie(a, b, c):
  return ShootFirst(a, b)

def AliceKillCharlieIfCharlieKillBob(a, b, c):
  return ShootFirst(a, c)

def AliceKillBobIfAliceKillCharlie(a, b, c):
  return ShootSecond(a, b)

def AliceWinIfAliceKillCharlie(a, b, c):
  return AliceKillBobIfAliceKillCharlie(a, b, c)

def AliceWinIfAliceDoNotKillCharlie(a, b, c):
  return (
    AliceKillBobIfBobKillCharlie(a, b, c) * BobKillCharlie(a, b, c) +
    AliceKillCharlieIfCharlieKillBob(a, b, c) * CharlieKillBob(a, b, c)
  )

def AliceKillCharlieIsTheBestStrategy(a, b, c):
  return (
    AliceWinIfAliceKillCharlie(a, b, c) -
    AliceWinIfAliceDoNotKillCharlie(a, b, c)
  )

def fixingA(a):
  b_values = np.linspace(0, 1, 101)
  c_values = np.linspace(0, 1, 101)

  B, C = np.meshgrid(b_values, c_values)

  Z = AliceKillCharlieIsTheBestStrategy(a, B, C)

  plt.figure(figsize=(8, 6))
  plt.imshow(Z, extent=(0, 1, 0, 1), origin='lower', cmap='seismic', vmin=-1, vmax=1)

  plt.colorbar(label=f'f(a={a:.2f}, b, c)')
  plt.xlabel('b')
  plt.ylabel('c')
  plt.title(f'Red is "Better to shoot",\nBlue is "Better to wait"')

  plt.contourf(B, C, B > C, colors=[(0,0,0,0), (0,0,0,0.3)])
  plt.contourf(B, C, a > C, colors=[(0,0,0,0), (0,0,0,0.3)])

  plt.savefig(f'output/fixingA/{a:.2f}.png')
  plt.close()  

def fixingB(b):
  a_values = np.linspace(0, 1, 101)
  c_values = np.linspace(0, 1, 101)

  A, C = np.meshgrid(a_values, c_values)

  Z = AliceKillCharlieIsTheBestStrategy(A, b, C)

  plt.figure(figsize=(8, 6))
  plt.imshow(Z, extent=(0, 1, 0, 1), origin='lower', cmap='seismic', vmin=-1, vmax=1)

  plt.colorbar(label=f'f(a, b={b:.2f}, c)')
  plt.xlabel('a')
  plt.ylabel('c')
  plt.title(f'Red is "Better to shoot",\nBlue is "Better to wait"')

  plt.contourf(A, C, b > C, colors=[(0,0,0,0), (0,0,0,0.3)])
  plt.contourf(A, C, A > C, colors=[(0,0,0,0), (0,0,0,0.3)])

  plt.savefig(f'output/fixingB/{b:.2f}.png')
  plt.close()  

def fixingC(c):
  a_values = np.linspace(0, 1, 101)
  b_values = np.linspace(0, 1, 101)

  A, B = np.meshgrid(a_values, b_values)

  Z = AliceKillCharlieIsTheBestStrategy(A, B, c)

  plt.figure(figsize=(8, 6))
  plt.imshow(Z, extent=(0, 1, 0, 1), origin='lower', cmap='seismic', vmin=-1, vmax=1)
  
  plt.colorbar(label=f'f(a, b, c={c:.2f})')
  plt.xlabel('a')
  plt.ylabel('b')
  plt.title(f'Red is "Better to shoot",\nBlue is "Better to wait"')

  plt.contourf(A, B, B > c, colors=[(0,0,0,0), (0,0,0,0.3)])
  plt.contourf(A, B, A > B, colors=[(0,0,0,0), (0,0,0,0.3)])

  plt.savefig(f'output/fixingC/{c:.2f}.png')
  plt.close()  

if os.path.exists('output'):
    shutil.rmtree('output')
os.makedirs('output')
os.makedirs("output/fixingA")
os.makedirs("output/fixingB")
os.makedirs("output/fixingC")

# Iterate over different values of c and call the fixingC function
for a in np.linspace(0, 1, 101):
    fixingA(a)
for b in np.linspace(0, 1, 101):
    fixingB(b)
for c in np.linspace(0, 1, 101):
    fixingC(c)