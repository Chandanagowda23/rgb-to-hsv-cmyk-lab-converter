import cv2
import numpy as np

#____________________________________________________________________#

# ### Convert RGB to HSV: 
image = cv2.imread('Lenna.png')
image = image.astype(float)

b, g, r  = image[:, :, 0], image[:, :, 1], image[:, :, 2]

b_scaled = b/255
g_scaled = g/255
r_scaled = r/255

V_max = np.maximum(np.maximum(b_scaled, g_scaled), r_scaled)
V_min = np.minimum(np.minimum(b_scaled, g_scaled), r_scaled)

s = np.zeros((512, 512))

s_1 = (V_max!=0)
s_2 = (V_max==0)

s[s_1] = (V_max[s_1]-V_min[s_1])/(V_max[s_1])
s[s_2] = 0

h = np.zeros((512, 512))

red =  (V_max == r_scaled)
green = (V_max == g_scaled)
blue =  (V_max == b_scaled)

h[red] = 60*(g_scaled[red]-b_scaled[red])/V_max[red]-V_min[red]
h[green] =  120+(60*(b_scaled[green]-r_scaled[green]))/V_max[green]-V_min[green]
h[blue] = 240+(60*(r_scaled[blue]-g_scaled[blue]))/V_max[blue]-V_min[blue]
h[(r_scaled == g_scaled) & (g_scaled == b_scaled)] = 0

h[h < 0] += 360
h = (h / 2)
s = (s * 255)
v = (V_max * 255)

hsv_image= np.dstack([h, s, v])
cv2.imwrite('hsv_image 1.png', hsv_image)

#____________________________________________________________________#

# ### Convert RGB to HSV: 

image = cv2.imread('Lenna.png')
image = image.astype(float)

b, g, r  = image[:, :, 0], image[:, :, 1], image[:, :, 2]

b_scaled = b/255
g_scaled = g/255
r_scaled = r/255

mini = np.minimum(np.minimum(b_scaled, g_scaled), r_scaled)
I = (r_scaled+g_scaled+b_scaled)/3

S1 = (3/(r_scaled+g_scaled+b_scaled))*mini
S = 1 - S1

numi = 0.5*((r_scaled-g_scaled)+(r_scaled-b_scaled))
denomi = ((r_scaled-g_scaled)**2+(r_scaled-b_scaled)*(g_scaled-b_scaled))**0.5
theta = np.arccos(numi/denomi)

H = np.zeros((512, 512))
h_lesser = (b_scaled<=g_scaled)
h_greater = b_scaled>g_scaled

H[h_lesser] = theta[h_lesser]
H[h_greater] = 360 - theta[h_greater]

hsi_image = np.dstack([H, S, I])*255
cv2.imwrite('hsv_image 2.png', hsi_image)

#____________________________________________________________________#

# ### Convert RGB to CMYK: 

image = cv2.imread('Lenna.png')
image = image.astype(float)

b, g, r  = image[:, :, 0], image[:, :, 1], image[:, :, 2]

b_scaled = b/255
g_scaled = g/255
r_scaled = r/255

c =1-r_scaled
m = 1-g_scaled
y =1-b_scaled

k = np.minimum(np.minimum(c, m), y)

C = (c-k)/(1-k)
M = (m-k)/(1-k)
Y = (y-k)/(1-k)

k1 = (k==1)
C[k1] = 0
M[k1] = 0
Y[k1] = 0

CMYK_image = (np.dstack((C,M,Y,k))*255).astype(np.uint8)
cv2.imwrite('cmyk_image.png', CMYK_image)

#____________________________________________________________________#

# ### Convert RGB to LAB: 

image = cv2.imread('lenna.png')
image = image.astype(float)

b, g, r  = image[:, :, 0], image[:, :, 1], image[:, :, 2]

b_scaled = b/255
g_scaled = g/255
r_scaled = r/255

X = (0.412453 * r_scaled) + (0.357580 * g_scaled) + (0.180423 * b_scaled)
Y = (0.212671 * r_scaled) + (0.715160 * g_scaled) + (0.072169 * b_scaled)
Z = (0.019334 * r_scaled) + (0.119193 * g_scaled) + (0.950227 * b_scaled)

Xn=0.950456
Zn=1.088754

X = X/Xn
Z = Z/Zn

Y_greater = (Y>0.008856)
Y_lesser = (Y<=0.008856)

L = np.zeros((512, 512))

L[Y_greater] = (116*((Y[Y_greater])**(1/3)))-16
L[Y_lesser] = 903.3*(Y[Y_lesser])

def f(t):
    cond = t > 0.008856
    t = np.where(cond, t ** (1/3), (7.787*t)+(16/116))
    return t

a = (500*(f(X)-f(Y)))+0
b = (200*(f(Y)-f(Z)))+0

L = ((L * 255)/100)
a = (a + 128)
b = (b + 128)

lab_image = np.dstack((L, a, b))

cv2.imwrite('lab_image.png', lab_image)
#____________________________________________________________________#