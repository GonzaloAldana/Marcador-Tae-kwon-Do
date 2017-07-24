# Marcador-Tae-kwon-Do
Marcador electrónico para peleas de Tae Kwon Do

Utiliza python 2.7 y la librería pygame para funcionar.
Utiliza glovepie para configurar los controles inalámbricos que necesita cada juez.

Las áreas de combate de TKD necesitan tener de 2 a 4 jueces de esquina que verifican cuando un peleador golpea a otro y así marcar los puntos correspondientes por golpe/patada. Para que el sistema le agregue puntos a algún jugador es necesario que por lo menos 2 jueces (dependiendo de la configuración) lo indiquen en un lapso menor o igual a 2 segundos.
Éste marcador se puede configurar para 2, 3 o 4 jueces; esto afecta directamente a la sensibilidad de los controles, es decir, con 2 jueces el mínimo para que el sistema marque el punto son los 2 jueces simultaneamente; si son 3 o 4 jueces, por lo menos 3 jueces deben marcar el punto simultaneamente.
Puede marcar amonestaciones, puntos en contra, tiempo fuera, tiempo de descanso, número de rounds, etc.
