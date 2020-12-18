segundos=input("Por favor, entre com o número de segundos que deseja converter: ")
total=int(segundos)
dias=total//86400
horas=(total%86400)//3600
minutos=((total%86400)%3600)//60
segundos2=((total%86400)%3600)%60
print(dias,"dias,",horas,"horas,",minutos,"minutos e",segundos2,"segundos.")
