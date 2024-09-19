#1
def mail(persona):

	print("на эту почку", persona, "будет отправлено приглашение")
pochta = input("Введите эл.почту приглашаемого")
mail(pochta)

#2
a = (i**2 for i in range(1,5))

for i in a:

	print(i)