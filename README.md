# edge-sizing
Edge Sizing in ANSYS Meshing

This contains two different options.

1. app.py
2. app_Water.py

## app.py

This contains general edge sizing app where smallest cell size is calculated for given $y^+$ in a turbulent pipe flow with input properties and velocity and mesh parameters and recommend a closer bias factor for the given $y^+$.

## app_Water.py

This can calculate the thermophysical properties for Water from IAPWS module from initial temperature and properties and calculate the smallest cell size and a recommended bias factor accordingly.

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
