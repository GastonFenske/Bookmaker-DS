select e.nombre, e.id from equipos e, partidos p 
where (e.id == p.equipo_local or e.id == p.equipo_visistante) and p.id == 1;