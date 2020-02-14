# the-game
aca empieza la historia

## ESQUEMA GENERAL:
Header con el logo de la app y acceso al menu
Footer con publicidad

componente App 
-componente Header
--componente HeaderMenu
--componente Logo 

-componente Contenido
--componente ListadoResultados
---componente ItemResultado
----componente BotonReservar
----componente BotonDetalle
----componente DatosEmpresa
-----componente LogoEmpresa
-----componente NombreEmpresa
-----componente DireccionEmpresa
----componente RatingEmpresa
----componente MiniPreviewDisponibilidadEmpresa
---componente PersonalizarBusqueda

-componente Footer
--componente Publicidad

## PANTALLA LANDING:
pantalla de bienvenida donde ubica al usuario manual o automaticamente dependiendo de los permisos y le ofrece una lista de servicios cercanos ordenados por el algoritmo trevisan. tambien ofrece un boton donde personalizar la busqueda por rating, ubicacion, etc.

### SISTEMA DE ESCORING:
algoritmo trevisan
1.0 pts por estrella de rating
0.1 pts por diferencia negativa de la media de precio

4estrellas, 0 de dif
3estrellas, 15 de dif 
3estrellas, 25 de dif

## MODAL DE DETALLE EMPRESA:
pantalla de detalle de la empresa donde se ve el logo, nombre, descripcion, trayectoria, reviews, boton de reserva, mini preview de disponibilidad en ubicacion actual

## PANTALLA DE RESERVA:
pantalla de reserva donde se muestra una serie de opciones para registrar una reserva en el sistema
0. ubicacion
1. tipo de servicio requerido
2. fecha y hora
3. boton de reservar
4. boton de volver al listado de busqueda
5. metodo de contacto (registracion)

## MODELO EMPRESA LIMPIEZA:
-buffer time entre trabajos configurable en minutos
-prioridad de tipo de contratacion configurable
-jornadas excepcional marcar ciertos dias con mas trabajo (ex, recambios)

## REVIEWS
mail de satisfaccion donde va a poder elegir ratear directamente desde ahi o escribir un review
