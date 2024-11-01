CREATE  TABLE Empleados (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    direccion VARCHAR(255),
    telefono VARCHAR(15),
    email VARCHAR(100),
    fecha_inicio DATE,
    salario DECIMAL(10, 2)
);

CREATE  TABLE Departamentos (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    id_gerente INT,
    FOREIGN KEY (id_gerente) REFERENCES Empleados(id)
);

CREATE TABLE Empleados_Departamentos (
    id_empleado INT,
    id_departamento INT,
    PRIMARY KEY (id_empleado, id_departamento),
    FOREIGN KEY (id_empleado) REFERENCES Empleados(id),
    FOREIGN KEY (id_departamento) REFERENCES Departamentos(id)
);

CREATE TABLE Proyectos (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT,
    fecha_inicio DATE
);

CREATE TABLE Empleados_Proyectos (
    id_empleado INT,
    id_proyecto INT,
    PRIMARY KEY (id_empleado, id_proyecto),
    FOREIGN KEY (id_empleado) REFERENCES Empleados(id),
    FOREIGN KEY (id_proyecto) REFERENCES Proyectos(id)
);

CREATE TABLE Registro_Tiempo (
    id INT PRIMARY KEY AUTO_INCREMENT,
    id_empleado INT,
    id_proyecto INT,
    fecha DATE,
    horas_trabajadas DECIMAL(5, 2),
    descripcion TEXT,
    FOREIGN KEY (id_empleado) REFERENCES Empleados(id),
    FOREIGN KEY (id_proyecto) REFERENCES Proyectos(id)
);


