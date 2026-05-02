# Calculate displacement using s = ut + 0.5*a*t^2
u = float(input("Enter initial velocity (u) in m/s: "))
a = float(input("Enter acceleration (a) in m/s^2: "))
t = float(input("Enter time (t) in seconds: "))
s = u * t + 0.5 * a * t * t
print("Displacement (s) =", s, "meters")
