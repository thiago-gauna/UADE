"""
. Sistema de gestión de eventos de un teatro 
Este sistema permite gestionar funciones teatrales, incluyendo 
la programación de espectáculos, la asignación de funciones 
por fecha y hora, y la reserva de entradas por parte de los es
pectadores. Está orientado a teatros, salas culturales o centros 
artísticos que ofrecen múltiples funciones y desean mantener 
un control eficiente de la asistencia y ocupación. Las entidades 
sugeridas son: Eventos (espectáculos), que representan las 
obras o shows disponibles en cartelera; Funciones, que corres
ponden a cada presentación en una fecha y horario específico; 
y Reservas, que registran los datos de quienes asisten a cada 
función. La entidad de unión es Reservas, ya que conecta a un espectador con una función 
determinada de un evento. 
El sistema deberá implementar operaciones CRUD sobre todas las entidades, permitiendo 
crear nuevos espectáculos, programar funciones, registrar y cancelar reservas. También de
berá permitir búsquedas como espectadores registrados para una función específica. Se uti
lizarán matrices para representar el calendario de funciones y la ocupación por día y horario, 
listas y diccionarios para estructurar los datos de espectáculos, funciones y espectadores, y 
recursividad para calcular ocupación acumulada o buscar funciones según filtros múltiples. 
Las estadísticas incluirán: cantidad total de funciones realizadas, promedio de espectadores 
por función, y porcentaje de ocupación por espectáculo. Se deberá incluir validación de da
tos mediante manejo de excepciones, almacenamiento en archivos, uso de Git para el con
trol de versiones y pruebas unitarias que validen el correcto funcionamiento del sistema.
"""


