import numpy as np
from iapws import IAPWS97

def calculate_Re(rho, U, L, mu):
	return (rho*U*L)/mu

def calculate_skin_friction(Re):

	# Schlichting Skin-Friction Coefficient
	# Valid for Re_x < 10^9
	return (2*np.log10(Re) - 0.65)**(-2.3)

def calculate_wall_shear(cf, U, rho):
	return cf*0.5*rho*(U**2)

def calculate_ustar(tw, rho):
	return np.sqrt(tw/rho)

def calculate_y(rho, U, L, mu, yPlus):
	Re = calculate_Re(rho, U, L, mu)
	cf = calculate_skin_friction(Re)
	tw = calculate_wall_shear(cf, U, rho)
	ustar = calculate_ustar(tw, rho)

	return (yPlus*mu)/(rho*ustar)

def calculate_smallD(L, ND, bf):
	sum = 0
	gr = bf**(1.0/(ND-1))
	for i in range(ND):
	    sum += gr**i
	L1 = L/sum
	
	return L1

def calculate_y_water(T, P, G, L, yPlus):
	state = IAPWS97(P=P/1e6, T=T)
	U = G/state.rho
	return calculate_y(state.rho, U, L, state.mu, yPlus)

def calculate_BF(L, ND, L1):	
	test_list = list(np.arange(1, 31, 0.001))
	dummy = calculate_smallD(L, ND, np.arange(1, 31, 0.001))
	error = abs(dummy - L1)/L1
	index = np.where(error == min(error))[0][0]

	if test_list[index] < 30:
		return test_list[index]
	else:
		return 0.0