"""Sample text."""
input_number = int(input("Enter a sum: "))  # Paneme summa numbrit

out50 = input_number // 50  # Leiame kui palju 50s selle arvu sisse mahub.
jaak50 = input_number % 50  # Leiame sellest jaak

out20 = jaak50 // 20  # Siin ja edasi kõik sama
jaak20 = jaak50 % 20

out10 = jaak20 // 10
jaak10 = jaak20 % 10

out5 = jaak10 // 5
jaak5 = jaak10 % 5

out1 = jaak5 // 1

sum_out = int(out50 + out20 + out10 + out5 + out1)  # Teeme sellest summa

print("Amount of coins needed:", sum_out)
