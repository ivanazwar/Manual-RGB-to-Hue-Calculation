R=150/225
G=140/225
B=110/225

C_MAX= max(R,G,B)
C_MIN= min(R,G,B)

delta= C_MAX -C_MIN

if delta ==0:
    H=0
elif C_MAX == R:
    H=60 * (((G-B)/delta) % 6)
elif C_MAX == G:
    H=60 * (((B-R)/delta) + 2)
elif C_MAX == B:
    H=60 * (((R-G)/delta) + 4)

#JIKA H NEGATIF TAMBAHKAN 360
if H<0:
    H+= 360

print(H)

