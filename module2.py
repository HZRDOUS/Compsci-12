w, x, y, z = 4, 2, 3, 1

if w > x: x, w = w, x
if x > y: y, x = x, y
if y > z: z, y = y, z
if w > x: x, w = w, x
if x > y: y, x = x, y
if w > x: x, w = w, x

print(w, x, y, z)