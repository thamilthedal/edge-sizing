import streamlit as st
from calc import calculate_y, calculate_smallD

title = st.title(r"$\Delta x_{min}(\rho, \mu, L, U_\infty, y^+)$")
caption = st.caption("Calculates the smallest cell size for given $y^+$ and mesh details for ANSYS Meshing.")
st.divider()

st.markdown("**Enter the thermophysical properties of the fluid:**")

col1, col2 = st.columns(2)

rho = col1.text_input("Density ($kg/m^3$):", key='rho', value = '0.0')

mu = col2.text_input("Dynamic viscosity ($Pa\ s$):", key = 'mu', value = '0.0')

st.markdown("**Enter other flow parameters:**")

col1, col2 = st.columns(2)

U = col1.text_input("Freestream velocity of the flow ($m/s$):", key = 'U', value = '0.0')

yPlus = col2.text_input("$y^+$ value near the wall:", key = 'yPlus', value = '0.0')

st.markdown("**Enter edge sizing details:**")

col1, col2, col3 = st.columns(3)

L = col1.text_input("Edge Length ($m$):", key = 'L', value = '0.0')

ND = col2.text_input("Number of divisions to be made:", key = 'ND', value = '0')

bf = col3.text_input("Bias-factor to apply:", key = 'bf', value = '0.0')

if st.button("Calculate"):
	result = calculate_y(float(rho), float(U), float(L), float(mu), float(yPlus))
	result2 = calculate_smallD(float(L)/2, int(ND), float(bf))

	col1, col2 = st.columns(2)
	with st.container():
		col1.success(r'$\Delta x_{min}$ for the $y^+$ is ' + f'{result:{3}.{5}}' + ' m')
		col2.success(r'$\Delta x_{min}$ for the mesh is ' + f'{result2:{3}.{5}}' + ' m')

with st.expander(r"Code for calculating $\Delta x_{min}$ for the mesh"):d
	code = '''def calculate_smallD(L, ND, bf):
	sum = 0
	gr = bf**(1.0/(ND-1))
	for i in range(ND):
	    sum += gr**i
	L1 = L/sum
	
	return L1'''

	st.code(code, language='python')
