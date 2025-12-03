# 1
age = int(input("Yoshingizni kiriting: "))
if age >= 18:
    print("Kattasiz")
else:
    print("Kattasiz emas")
# 2
a = float(input("Birinchi sonni kiriting: "))
b = float(input("Ikkinchi sonni kiriting: "))

if a > b:
    print("Birinchi son katta")
elif b > a:
    print("Ikkinchi son katta")
else:
    print("Sonlar teng")
# 3
  x = float(input("Son kiriting: "))
if x > 0:
    print("Musbat son")
elif x < 0:
    print("Manfiy son")
else:
    print("Son 0 ga teng")

# 4
  n = int(input("Raqam kiriting: "))
if n < 10:
    print("10 dan kichik")
elif n == 10:
    print("10 ga teng")
else:
    print("10 dan katta")

# 5
  a = float(input("Birinchi sonni kiriting: "))
b = float(input("Ikkinchi sonni kiriting: "))

if a == b:
    print("Sonlar teng")
else:
    print("Sonlar teng emas")

# 6
s = input("So'z kiriting: ").strip().lower()

if s == "hello":
    print("Salom!")
elif s == "bye":
    print("Xayr!")
else:
    print("Noma'lum so'z")
