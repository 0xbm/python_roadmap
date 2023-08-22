print("""
1. raise -> exceptions

Ex:
x = 10
if x > 5:
    raise Exception('x should not exceed 5. The value of x was: {}'.format(x))

2. try:
        run code
    except:
        execute this code when is exception
        
Ex:
try:
    print(2 / 0)
except ZeroDivisionError as z:
    print("Och nie, coś poszło nie tak! Szczegóły poniżej:")
    print(z)
        
3. finally:

Ex:
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")
""")

# def silnia(n):
#     if n < 0:
#         raise ValueError("silnia niezdefiniowana dla liczb ujemnych")
#     wynik = 1
#     for i in range(1, n + 1):
#         wynik *= i
#     return wynik
#
#
# try:
#     print(f"Silnia z 5 to {silnia(5)}")
# except ValueError as e:
#     print("Och nie, coś poszło nie tak! Szczegóły poniżej:")
#     print(e)

