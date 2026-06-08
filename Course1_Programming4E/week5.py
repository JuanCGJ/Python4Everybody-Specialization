sc = input("Enter Score: ")
score=float(sc)
if score >= 0.0 :
   if score <= 1.0 :
     if score >=0.9 :
        print("A")
     elif score >=0.8 :
        print("B")
     elif score >=0.7 :
        print("C")
     elif score >=0.6 :
        print("D")
     elif score < 0.6 :
        print("F")
   else:
        print("Out of range")
if score < 0.0 :
    print("Out of range")
