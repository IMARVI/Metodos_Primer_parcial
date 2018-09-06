import sys
import random
import math

media_personas1=20/60 #personas por minuto
media_atencion1=2 #minutos por persona
media_personas2 = 0 #las que lleguen siendo atendidas del 1
media_atencion2=0 #50% de las veces será 1 y 50% será 2. 
cola1=0
cola2=0
tiempo_transcurrido=0
tiempo_llegadas1=[]
tiempo_llegadas2=[]
sig_atendido1=False
t_transcurrido2=0
t_transcurrido=0
cliente=0
promedio_espera1=0
promedio_espera2=0
probabilidad_atencion_mayor= 1-(1-math.exp(-(0.5*2))) #probabilidad de tardar más de dos minutos (supondré que tardó 3)
probabilidad_atencion_menor= (1-math.exp(-(0.5*2))) #probabilidad de tardar menos de dos minutos (supondré que tardó 1)
probabilidad_cliente = (math.exp(-media_personas1) * (media_personas1))/1 #probabilidad de que llegue un cliente en el próximo minuto según poisson. (Cola 1)
print("Probabilidad de llegar: ", probabilidad_cliente)
for i in range (0,10): #los próximos 5000 minutos. 
	llega_cola=random.random()
	if(llega_cola<probabilidad_cliente):
		#llega un cliente en ese minuto
		cola1+=1
		cliente+=1
		tiempo_transcurrido+=1
		print(f"El cliente {cliente} llegó al minuto {tiempo_transcurrido}")
		tiempo_llegadas1.append(tiempo_transcurrido)
	else:
		#no llegó nadie ese minuto
		print("No llegó nadie")
		tiempo_transcurrido+=1
#acabaron de llegar los 5000 clientes a la primera estación. los voy a atender. 
tiempo_reversa=0
t_esp=0
t_transcurrido=tiempo_llegadas1[0]
for i in range(0,cliente): #el primer cliente no espera
	T_aten=random.random()
	if(T_aten<probabilidad_atencion_menor): 
		#tardo 1 minuto. 
		t_transcurrido+=1
		t_esp=1

	elif(T_aten>probabilidad_atencion_menor):
		t_transcurrido+=3
		t_esp=3
	if(i==0):
		print(f"el cliente {i} llegó al minuto {tiempo_llegadas1[i]} pero no tuvo que esperar nada.")
		t_esp=0
	if(t_transcurrido>tiempo_llegadas1[i]):
		#checar si el tiempo transcurrido está siendo mayor que lo que he esperado o viceversa. 
		print("t_transcurrido era más grande")
		if(i!=0):
			promedio_espera1+= (t_transcurrido - tiempo_llegadas1[i])
			print(f"Este cliente esperó: {(t_transcurrido - tiempo_llegadas1[i])}")
		print(f"El cliente {i} llegó al minuto {tiempo_llegadas1[i]} y se va al {t_transcurrido}.")
		#cuando se va se mete a la fila 2:
		tiempo_llegadas2.append(t_transcurrido)
		cola1-=1
		cola2+=1
	else:
		t_transcurrido=tiempo_llegadas1[i]
		promedio_espera1+=0
		print(f"Este cliente esperó: {(t_transcurrido - tiempo_llegadas1[i])}")

		print(f"El cliente {i} llegó al minuto {tiempo_llegadas1[i]} y se va al {t_transcurrido +t_esp}.")
		tiempo_llegadas2.append(t_transcurrido + t_esp)
		cola1-=1
		cola2+=1

		#NOTA ARREGLAR PROBLEMA CON LOS TIEMPOS:
for i in range(0,cliente):

	tiempo_transcurrido2 = tiempo_transcurrido
	t_aten2=random.random()
	if(t_aten2<0.5):
		t_esp=1
		t_transcurrido2+=1
	else:
		t_esp=2
		t_transcurrido2+=2
	if(t_transcurrido2>tiempo_llegadas2[i]):
		if(i!=0):
			promedio_espera2+=(t_transcurrido2-tiempo_llegadas2[i])
			print("Este cliente esperó:", {t_transcurrido2-tiempo_llegadas2[i]})
		printf(f"El cliente {i} llegó a la fila 2 al minuto {tiempo_llegadas2[i]} y se va al {tiempo_transcurrido2}")
	else:
		t_transcurrido2=tiempo_llegadas2[i]
		promedio_espera2+=0
		print(f"El cliente {i} llegó a la fila 2 al minuto {tiempo_llegadas2[i]} y se va al {t_transcurrido2 + t_esp}")


print(f"En promedio la gente esperó: {promedio_espera1/cliente} minutos... O bien, {promedio_espera1*60/cliente} segundos en la fila 1")






	 

