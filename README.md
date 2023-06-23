# edge-sizing
## Edge Sizing in ANSYS Meshing

This is a general edge sizing app where smallest cell size is calculated for given $y^+$ in a turbulent pipe flow with input properties and velocity and mesh parameters and recommend a closer bias factor for the given $y^+$.

This contains two different options.

1. Water
2. Other Fluids

## Water

This can calculate the thermophysical properties for Water from IAPWS module from initial temperature and properties and calculate the smallest cell size and a recommended bias factor accordingly.

## Other Fluids

This contains general edge sizing app where y+ is calculated for a turbulent pipe flow with input properties and velocity and geometry parameters.

## Calculation module:

### Skin Friction Coefficient
The Skin-friction coefficient is calculated by Schlichting Skin-Friction Coefficient that is Valid for $Re_x < 10^9$ as follows.

$$
c_f = (2 log_{10}(Re_D) - 0.65)^{-2.3}
$$

### Smallest Cell Size for given $y^+$

$$
\Delta x_{min} = \frac{y^+ \mu}{\rho u^*} 
$$

where $u^*$ is calcualted as,

$$
u^*  = \sqrt{\frac{\tau_w}{\rho}} = \sqrt{0.5 c_f U^2}
$$

### Smallest Cell Size in the mesh
The Edge Sizing method in ANSYS Meshing works by a simple geometric progression where the bias factor (bf) is the ratio of the G.P, and L is the length of the edge divided into N divisions.

$$
\Delta x_{min} = \frac{L}{\Sigma_{i = 0}^{N} (bf^{(1/N-1)})^i}
$$

### Recommended Bias factor
This runs the Small cell utility for multiple bias factors from 1 to 31 with a step of 0.01 and find the closest value to the Small cell size given by $y^+$ and recommend that bias factor to be used for the given $y^+$.
