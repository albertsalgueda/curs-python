# EXPLICACIÓ

from temps_status import get_status
from cultius import cultius
from activador_reg import reg
from informador import informador
from temporitzador import temporitzador
from reset import reset

# Falta temporitzar el reg quan s'encèn
# Falta temporitzar tot el procès sencer

poble = "42.19706849706395,2.191078679466587" # Escriure les coordenades del poble
poblacio, pais, temp, humitat, presio, data, pluja, condicions = get_status(poble)

humitat_optima, cultiu = cultius()

informador(poblacio, pais, temp, humitat, presio, data, pluja, condicions,humitat_optima,cultiu)

estat_reg, temps = reg(pluja, humitat, humitat_optima)

temporitzador(estat_reg, temps)

reset()
