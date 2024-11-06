CREATE  TABLE Empleados (
    id_empleado INT PRIMARY KEY  AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    direccion VARCHAR(255),
    telefono VARCHAR(15),
    email VARCHAR(100),
    fecha_inicio VARCHAR(20),
    salario INT
);

CREATE TABLE Departamentos (
    id_departamento INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    id_empleado INT,
    FOREIGN KEY (id_empleado) REFERENCES Empleados(id_empleado)
);

CREATE TABLE Empleados_Departamentos (
    id_empleado INT,
    id_departamento INT,
    PRIMARY KEY (id_empleado, id_departamento),
    FOREIGN KEY (id_empleado) REFERENCES Empleados(id_empleado),
    FOREIGN KEY (id_departamento) REFERENCES Departamentos(id_departamento)
);

CREATE TABLE Proyectos (
    id_proyecto INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    descripcion VARCHAR(255),
    fecha_inicio VARCHAR(20)
);

CREATE TABLE Empleados_Proyectos (
    id_empleado INT,
    id_proyecto INT,
    PRIMARY KEY (id_empleado, id_proyecto),
    FOREIGN KEY (id_empleado) REFERENCES Empleados(id_empleado),
    FOREIGN KEY (id_proyecto) REFERENCES Proyectos(id_proyecto)
);

CREATE TABLE Registro_Tiempo (
    id_reg_temp INT PRIMARY KEY AUTO_INCREMENT,
    id_empleado INT,
    id_proyecto INT,
    fecha VARCHAR(20),
    horas_trabajadas VARCHAR(100),
    descripcion VARCHAR(255),
    FOREIGN KEY (id_empleado) REFERENCES Empleados(id_empleado),
    FOREIGN KEY (id_proyecto) REFERENCES Proyectos(id_proyecto)
);


