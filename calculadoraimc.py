print("Calculadora de IMC")
print("Comece informando o seu peso")
peso = int(input())
print("E sua altura:")
altura = float(input())
imc = peso / (altura * altura)
print("Calculando...\nSeu IMC é: ", round(imc, 2))
if imc < 18.5:
  print("Magreza")
elif imc >= 18.5 and imc < 25:
  print("Normal")
elif imc >= 25 and imc < 30:
  print("Grau de obesidade I")
elif imc >= 30 and imc < 35:
  print("Grau de obesidade II")
elif imc >= 35 and imc < 40:
  print("Grau de obesidade III")
elif imc >= 40:
  print("Grau de 💀")
ideal1 = 18.5 * (altura * altura)
ideal2 = 24.9 * (altura * altura)
print("Seu peso ideal seria entre: ", round(ideal1, 1), "  ", round(ideal2, 1))