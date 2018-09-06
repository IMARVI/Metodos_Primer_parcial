import sys
import random

costo_promedio_anual=75000
autos_rentados_en_el_dia=0
cant_autos_prom=0
costo_prom=0
costo_falta=0
cuenta=0
#caclular para cada plan: 0 autos, 1 auto, 2 autos, 3 autos y 4 autos como base. 
plan = [0,1,2,3,4]
gastos_plan_sobra=[0,0,0,0,0]
gastos_plan_falta=[0,0,0,0,0]
ganancias_plan=[0,0,0,0,0]
gastos_plan_compra=[0,75000,2*75000,3*75000,4*75000]
for a in range(0,365):
	autos_rentados=random.random()
	if(autos_rentados<0.10):
		#no hay autos rentados ese día
		autos_rentados_en_el_dia=0
	elif(autos_rentados>=0.10 and autos_rentados<0.20):
		#se rentó 1 auto. 
		autos_rentados_en_el_dia=1

	elif(autos_rentados>=0.20 and autos_rentados<0.45):
		#se rentaron 2 autos. 
		autos_rentados_en_el_dia=2

	elif(autos_rentados>=0.45 and autos_rentados<0.75):
		# se rentaron 3 autos. 
		autos_rentados_en_el_dia=3

	else:
		# se rentaron 4 autos. 
		autos_rentados_en_el_dia=4
	for ii in range(0,4):
		#print(f"autos del día: {autos_rentados_en_el_dia} y plan: {ii}")
		if(autos_rentados_en_el_dia<plan[ii]):
			#debo cobrarle la diferencia. 
			costo_espera=(plan[ii]-autos_rentados_en_el_dia)*50
			gastos_plan_sobra[ii] = gastos_plan_sobra[ii] + costo_espera
		elif(autos_rentados_en_el_dia>plan[ii]):
			#debo cobrar los autos que no tengo. 
			costo_falta= (autos_rentados_en_el_dia-plan[ii])*200
			gastos_plan_falta[ii]= gastos_plan_falta[ii] + costo_falta
		else:
			#no necesito cobrar extras porque se rentaron justitos. Yo gano dinero.
			hola=0
		#ahora ya sé cuantos autos se rentaron y cuanto perdí. Tocan las ganancias:
		#print(f"renté {autos_rentados_en_el_dia} autos hoy")
		para_rentar=plan[ii]
		while(para_rentar>0):
			tiempo_renta=random.random()
			para_rentar-=1
			#print(f"el plan {ii} tiene")
			if(tiempo_renta<0.40):
				#se renta 1 día
				ganancias_plan[ii] = ganancias_plan[ii]  + 1*350
			elif(tiempo_renta>0.40 and tiempo_renta<0.75):
				#se renta 2 días. 
				ganancias_plan[ii] = ganancias_plan[ii]  + 2*350

			elif(tiempo_renta>=0.75 and tiempo_renta<0.90):
				#se renta 3 días
				ganancias_plan[ii] = ganancias_plan[ii]  + 3*350

			else:
				#se renta 4 días. 
				ganancias_plan[ii] = ganancias_plan[ii]  + 4*350
		#print(f"El plan {ii} ganó {ganancias_plan[ii]} y gastó {gastos_plan_falta[ii] + gastos_plan_sobra[ii]} en el día {a}")
	cuenta+=1
for i in range(0,4):
	print(f"En promedio el plan {i} ganó {ganancias_plan[i]/cuenta} y gastó {(gastos_plan_falta[i] + gastos_plan_sobra[i])/cuenta} al día")
	print(f"Sin embargo, tomando en cuenta inversiones: ")
	print(f"El plan {i} ganó {ganancias_plan[i]} en el año y gastó {gastos_plan_falta[i] + gastos_plan_sobra[i] + gastos_plan_compra[i]} contando las compras")
	print(f"Por lo tanto, la verdadera ganancia total del plan {i} es de {ganancias_plan[i] - gastos_plan_falta[i] + gastos_plan_sobra[i] + gastos_plan_compra[i]} al año")
	print(" ")




