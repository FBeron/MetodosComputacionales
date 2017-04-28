# Tarea4.mk

Resultados_hw4.pdf : Resultados_hw4.tex T*.png T*.txt
	pdflatex Resultados_hw4.tex

Resultados_hw4.tex : T*.png
	touch Resultados_hw4.tex

T*.txt : DifusionTemperatura.c
	cc DifusionTemperatura.c -lm -o Dif.x
	./Dif.x

T*.png : Plots_Temperatura.py
	python Plots_Temperatura.py

T*.png : T*.txt
