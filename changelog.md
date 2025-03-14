v0.1
- Ajustar la seleccion de de texto del OCR, mejorar la clasificacion del texto!
hay valores que no corresponden por ejemplo el total: en algunas pruebas pone el total de iva y no el total de la facturta


- En las tablas
ocultar la columna uid y fecha de registro
agregar boton de edicion y eliminar 




- Mejoras futuras: 
agregar informacion que se recopile en el google calender (boleta/factura)




- Graficos interactivos: Con la data que se exportara (CSV)

### Facturas
- La exportacion de la app esta siendo dificultada por la libreria docx2pdf==0.1.8, al parecer no la reconoce correctamente al momento de empaquetar mi app en un .exe

### Calandario
cuando registre una boleta/factura/pdf en mi bd de google sheet tiene que registrar la fecha_factura_boleta (por ejemplo) tambien en mi tabla interna 'fechas importantes' para luego poder asociar esta tabla con el calendario
