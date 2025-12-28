#promedio de duraciones

otros_cursos_min = 2.5

otros_cursos_max = 7

otros_cursos_prom = 4

dalto_curso = 1.5

#diferencias de duracion

diferencia_con_min = 100 - dalto_curso / otros_cursos_min * 100

diferencia_con_max = 100 - dalto_curso * 1000 // otros_cursos_max / 10

diferencia_con_prom = 100 - dalto_curso / otros_cursos_prom * 100

#diferencia de duracion en crudo ( sin editar )

crudo_promedio = 5

crudo_dalto = 3.5

tiempo_vacio_promedio = 100 - otros_cursos_prom * 1000 // crudo_promedio / 10
tiempo_vacio_dalto = 100 - dalto_curso * 1000 // crudo_dalto / 10


#calculos diferencias de duracion ( ejercicio A )
print(f"el curso de dalto dura un: {diferencia_con_min}% menos que el mas rapido")
print(f"el curso de dalto dura un: {diferencia_con_max}% menos que el mas lento")
print(f"el curso de dalto dura un: {diferencia_con_prom}% menos que el promedio")

#calculos diferencias de duracion ( ejercicio B )
print(f"el curso de dalto dura un: {tiempo_vacio_promedio}% de tiempo vacio en promedio")
print(f"este curso elimino el {tiempo_vacio_dalto}% de tiempo vacio %")

#mostrando diferencias si los cursos duraran 10 hs
print(f"ver 10 hs de este curso equivale a ver {otros_cursos_prom * 1000 // dalto_curso / 100} horas de otros curso")
print(f"ver 10 hs de otros cursos equivale a ver {dalto_curso * 100 // otros_cursos_prom / 10} horas de este curso")