import streamlit as st
from calc import calculate_y, calculate_smallD

title = st.title(r"$y_d(\rho, \mu, L, U_\infty, y^+)$")

rho = st.text_input("Density ($kg/m^3$):", key='rho', value = '0.0')

mu = st.text_input("Dynamic viscosity ($Pa\ s$):", key = 'mu', value = '0.0')

L = st.text_input("Characteristic length of the flow ($m$):", key = 'L', value = '0.0')

U = st.text_input("Freestream velocity of the flow ($m/s$):", key = 'U', value = '0.0')

ND = st.text_input("Number of divisions to be made:", key = 'ND', value = '0')

bf = st.text_input("Bias-factor to apply:", key = 'bf', value = '0.0')

yPlus = st.text_input("$y^+$ value near the wall:", key = 'yPlus', value = '0.0')

if st.button("Calculate"):
	result = calculate_y(float(rho), float(U), float(L), float(mu), float(yPlus))
	result2 = calculate_smallD(float(L)/2, int(ND), float(bf))
	st.write(f'$y_d$ near the wall is {result:{3}.{5}} m')
	st.write(f'$y_d$ for the proposed mesh is {result2:{3}.{5}} m')
