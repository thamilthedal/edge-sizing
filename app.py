import streamlit as st
from calc import calculate_y, calculate_smallD, calculate_y_water, calculate_BF

title = st.title(r"$\Delta x_{min}(L, N_D, BF, y^+)$")

st.sidebar.write('Made by Thedal')
st.sidebar.markdown('''
- [Github Repo](https://github.com/thamilthedal/edge-sizing)
- [About me](https://thamilthedal.github.io/)
- [Instagram](https://www.instagram.com/thamilthedal/)
''', unsafe_allow_html=True)

caption = st.caption(
    "Calculates the smallest cell size for given $y^+$ for a turbulent pipe flow and mesh details for ANSYS Meshing.")

fluid = st.selectbox("Select Fluid:", options = ["Water", "Others"])

if fluid == "Water":
    st.markdown("**Enter the state of the water:**")
    col1, col2 = st.columns(2)

    T = col1.text_input("Temperature (K):", key='T', value='0.0')
    P = col2.text_input("Pressure ($Pa$):", key='P', value='0.0')

    st.markdown("**Enter other flow parameters:**")

    col1, col2 = st.columns(2)

    G = col1.text_input(
        "Mass velocity of the flow ($kg/m^2 s$):", key='G', value='0.0')
    yPlus_Water = col2.text_input(
        "$y^+$ value near the wall:", key='yPlus_Water', value='0.0')

else:
    st.markdown("**Enter the thermophysical properties of the fluid:**")
    col1, col2 = st.columns(2)

    rho = col1.text_input("Density ($kg/m^3$):", key='rho', value='0.0')
    mu = col2.text_input(r"Dynamic viscosity ($Pa\ s$):", key='mu', value='0.0')

    st.markdown("**Enter other flow parameters:**")

    col1, col2 = st.columns(2)

    U = col1.text_input(
        r"Freestream velocity of the flow ($m/s$):", key='U', value='0.0')

    yPlus_General = col2.text_input(
        r"$y^+$ value near the wall:", key='yPlus_General', value='0.0')


st.markdown("**Enter edge sizing details:**")

col1, col2, col3 = st.columns(3)

L = col1.text_input("Edge Length ($m$):", key='L', value='0.0')

ND = col2.text_input("Number of divisions to be made:", key='ND', value='0')

bf = col3.text_input("Bias-factor to apply:", key='bf', value='0.0')

if st.button("Calculate"):
    if fluid == "Water":
        input_error = [T, P, G, yPlus_Water]
        if '0.0' in input_error:
            st.error("Invalid input")
        else:
            result = calculate_y_water(float(T), float(
            P), float(G), float(L), float(yPlus_Water))
    else:
        input_error = [rho, mu, U, yPlus_General]
        if '0.0' in input_error:
            st.error("Invalid input")
        else:
            result = calculate_y(float(rho), float(U), float(
                L), float(mu), float(yPlus_General))

    if '0.0' not in input_error:
        result2 = calculate_smallD(float(L)/2, int(ND), float(bf))
        result3 = calculate_BF(float(L)/2, int(ND), result)

        col1, col2 = st.columns(2)
        with st.container():
            col1.success(r'$\Delta x_{min}$ for the $y^+$ is ' + f'{result:{3}.{5}}' + ' m')
            col2.success(r'$\Delta x_{min}$ for the mesh is ' + f'{result2:{3}.{5}}' + ' m')

        with st.container():
            if result3 != 0.0:
                st.success(r'Recommended bias factor for the given $y^+$ could be ' + f'{result3:{1}.{4}}')
            else:
                st.error(
                    r'Recommended bias factor is too high. Consider changing mesh settings.')

with st.expander(r'Code for calculating $\Delta x_{min}$ for the mesh'):

    code = '''def calculate_smallD(L, ND, bf):
    sum = 0
    gr = bf**(1.0/(ND-1))
    for i in range(ND):
        sum += gr**i
    L1 = L/sum
    
    return L1'''

    st.code(code, language='python')


with st.expander('Code for calculating recommended bias factor'):

    code = '''def calculate_BF(L, ND, L1):
    test_list = list(np.arange(1, 31, 0.001))
    dummy = calculate_smallD(L, ND, np.arange(1, 31, 0.001))
    error = abs(dummy - L1)/L1
    index = np.where(error == min(error))[0][0]
    
    if test_list[index] < 30:
        return test_list[index]
    else:
        return 0.0'''

    st.code(code, language='python')
