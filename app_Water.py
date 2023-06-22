import streamlit as st
from calc import calculate_y_water, calculate_smallD, calculate_BF

title = st.title(r"$\Delta x_{min}(T, P, L, G, y^+)\ for\ Water$")

caption = st.caption("Calculates the smallest cell size for given $y^+$ and mesh details for ANSYS Meshing.")
st.divider()

st.markdown("**Enter the state of the water:**")

col1, col2 = st.columns(2)

T = col1.text_input("Temperature (K):", key='T', value = '0.0')

P = col2.text_input("Pressure ($Pa$):", key = 'P', value = '0.0')

st.markdown("**Enter other flow parameters:**")

col1, col2 = st.columns(2)

G = col1.text_input("Mass velocity of the flow ($kg/m^2 s$):", key = 'U', value = '0.0')

yPlus = col2.text_input("$y^+$ value near the wall:", key = 'yPlus', value = '0.0')


st.markdown("**Enter edge sizing details:**")

col1, col2, col3 = st.columns(3)

L = col1.text_input("Edge Length ($m$):", key = 'L', value = '0.0')

ND = col2.text_input("Number of divisions to be made:", key = 'ND', value = '0')

bf = col3.text_input("Bias-factor to apply:", key = 'bf', value = '0.0')

if st.button("Calculate"):
	result = calculate_y_water(float(T), float(P), float(G), float(L), float(yPlus))
	result2 = calculate_smallD(float(L)/2, int(ND), float(bf))
	result3 = calculate_BF(float(L)/2, int(ND), result)

	col1, col2 = st.columns(2)
	with st.container():
		col1.success(r'$\Delta x_{min}$ for the $y^+$ is ' + f'{result:{3}.{5}}' + ' m')
		col2.success(r'$\Delta x_{min}$ for the mesh is ' + f'{result2:{3}.{5}}' + ' m')

	with st.container():
		st.success(r'Recommended bias factor for the given $y^+$ could be '+ f'{result3:{1}.{4}}')


with st.expander(r"Code for calculating $\Delta x_{min}$ for the mesh"):
	code = '''def calculate_smallD(L, ND, bf):
	sum = 0
	gr = bf**(1.0/(ND-1))
	for i in range(ND):
	    sum += gr**i
	L1 = L/sum
	
	return L1'''

	st.code(code, language='python')


with st.expander(r'Code for calculating recommended bias factor'):
	code = '''def calculate_BF(L, ND, L1):
	test_list = list(np.arange(1, 31, 0.001))
	dummy = calculate_smallD(L, ND, np.arange(1, 31, 0.001))
	error = abs(dummy - L1)/L1
	index = np.where(error == min(error))[0][0]
	
	return test_list[index]'''

	st.code(code, language='python')