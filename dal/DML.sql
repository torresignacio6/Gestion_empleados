INSERT  INTO Empleados (nombre, direccion, telefono, email, fecha_inicio, salario) VALUES
('Ignacio Torres', 'Calle Falsa 123, Ciudad A', '555-1234', 'juan.perez@gmail.com', '2023-01-15', 50000.00),
('María Gómez', 'Av. Principal 456, Ciudad B', '555-5678', 'maria.gomez@gmail.com', '2022-08-10', 52000.00),
('Jaider Torres', 'Boulevard Central 789, Ciudad C', '555-8765', 'carlos.lopez@gmail.com', '2021-11-05', 48000.00),
('Ana Martínez', 'Calle Norte 101, Ciudad D', '555-4321', 'ana.martinez@gmail.com', '2020-02-20', 47000.00),
('Luis Fernández', 'Av. Sur 202, Ciudad E', '555-6789', 'luis.fernandez@gmail.com', '2019-05-30', 55000.00);

INSERT INTO Departamentos (nombre, id_gerente) VALUES
('Desarrollo Sostenible', 1),
('Investigación y Desarrollo', 2),
('Ventas', 3),
('Recursos Humanos', 4),
('Marketing', 5);

INSERT  INTO Empleados_Departamentos (id_empleado, id_departamento) VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5);

INSERT INTO Proyectos (nombre, descripcion, fecha_inicio) VALUES
('Proyecto Solar', 'Desarrollo de paneles solares de alta eficiencia', '2023-02-01'),
('Proyecto Eólico', 'Investigación de nuevas turbinas eólicas', '2022-09-15'),
('Proyecto Reciclaje', 'Creación de un sistema de reciclaje automatizado', '2021-12-05'),
('Proyecto Educación', 'Desarrollo de una plataforma de educación ambiental', '2020-03-10'),
('Proyecto Agua', 'Mejora en la eficiencia de sistemas de filtración de agua', '2019-06-25');

INSERT INTO Empleados_Proyectos (id_empleado, id_proyecto) VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5),
(1, 2),
(2, 3),
(3, 4),
(4, 5),
(5, 1);

INSERT INTO Registro_Tiempo (id_empleado, id_proyecto, fecha, horas_trabajadas, descripcion) VALUES
(1, 1, '2023-02-10', 8.0, 'Instalación de paneles solares'),
(2, 2, '2023-02-11', 6.5, 'Análisis de eficiencia de turbinas'),
(3, 3, '2023-02-12', 7.0, 'Diseño del sistema de reciclaje'),
(4, 4, '2023-02-13', 8.0, 'Desarrollo de módulos educativos'),
(5, 5, '2023-02-14', 5.0, 'Pruebas de filtración de agua'),
(1, 2, '2023-02-15', 6.0, 'Optimización de paneles solares'),
(2, 3, '2023-02-16', 8.0, 'Revisión de prototipos'),
(3, 4, '2023-02-17', 5.5, 'Desarrollo de software de reciclaje'),
(4, 5, '2023-02-18', 6.5, 'Creación de contenido educativo'),
(5, 1, '2023-02-19', 7.0, 'Mantenimiento de sistemas de filtración');


