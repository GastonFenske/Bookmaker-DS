/*select a.fecha, a.monto, a.equipo_ganador_id, a.partido from apuestas a, partidos p where a.cliente == 99
and a.equipo_ganador_id == p.ganador;*/

select a.fecha, a.monto, a.equipo_ganador_id, a.partido from apuestas a, partidos p where a.cliente == 99
and a.equipo_ganador_id =! p.ganador;