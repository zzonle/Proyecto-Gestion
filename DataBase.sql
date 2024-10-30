-- Crear la base de datos
CREATE DATABASE IF NOT EXISTS `gestionproyectos` 
    /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci */;
USE `gestionproyectos`;

-- Eliminar tablas si existen
DROP TABLE IF EXISTS `registro_tiempo`;
DROP TABLE IF EXISTS `empleados_proyecto`;
DROP TABLE IF EXISTS `proyecto`;
DROP TABLE IF EXISTS `empleado`;
DROP TABLE IF EXISTS `departamento`;

-- Tabla departamento
CREATE TABLE `departamento` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `gerente_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `gerente_id` (`gerente_id`)
);

-- Insertar datos en la tabla departamento
INSERT INTO `departamento` (id, nombre, gerente_id) VALUES 
(1, 'Informatica', NULL),
(2, 'Administración', NULL);

-- Tabla empleado
CREATE TABLE `empleado` (
  `id` int NOT NULL AUTO_INCREMENT,
  `rut` varchar(12) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `direccion` varchar(255) DEFAULT NULL,
  `telefono` varchar(15) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `fecha_inicio` date DEFAULT NULL,
  `salario` decimal(10,2) DEFAULT NULL,
  `departamento_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `departamento_id` (`departamento_id`)
);

-- Insertar datos en la tabla empleado
INSERT INTO `empleado` (id, rut, nombre, direccion, telefono, email, fecha_inicio, salario, departamento_id) VALUES 
(1, '1-9', 'Rodrigo Ruiz', 'san felipe 176', '56962218', 'rodrigo.ruiz05@inacapmail.cl', '1971-07-28', 3000000.00, 1),
(2, '2-7', 'Sofía Gómez', 'calle falsa 123', '56998765', 'sofia.gomez@email.cl', '1980-03-15', 2500000.00, 2);

-- Tabla proyecto
CREATE TABLE `proyecto` (
   `proyecto_id` int(11) NOT NULL AUTO_INCREMENT,
   `nombre_proyecto` varchar(25) NOT NULL,
   `descripcion_proyecto` varchar(200) DEFAULT NULL,
   `fecha_inicio_proyecto` date DEFAULT NULL,
   PRIMARY KEY (`proyecto_id`)
);

-- Insertar datos en la tabla proyecto
INSERT INTO `proyecto` (proyecto_id, nombre_proyecto, descripcion_proyecto, fecha_inicio_proyecto) VALUES 
(1, 'Proyecto 1', 'Descripción del Proyecto 1', '2023-09-25'),
(2, 'Proyecto 2', 'Descripción del Proyecto 2', '2024-09-25');

-- Tabla empleados_proyecto
CREATE TABLE `empleados_proyecto` (
   `proyecto_id` int(11) NOT NULL,
   `empleado_id` int(11) NOT NULL,
   PRIMARY KEY (`proyecto_id`,`empleado_id`),
   KEY `empleado_id` (`empleado_id`)
);

-- Insertar datos en la tabla empleados_proyecto
INSERT INTO `empleados_proyecto` (proyecto_id, empleado_id) VALUES 
(1, 1),
(1, 2),
(2, 2);

-- Tabla registro_tiempo
CREATE TABLE `registro_tiempo` (
   `id` int(11) NOT NULL AUTO_INCREMENT,
   `fecha` date DEFAULT NULL,
   `horas` time DEFAULT NULL,
   `descripcion` varchar(400) NOT NULL,
   `empleado_id` int(11) DEFAULT NULL,
   `proyecto_id` int(11) DEFAULT NULL,
   PRIMARY KEY (`id`),
   KEY `empleado_id` (`empleado_id`),
   KEY `proyecto_id` (`proyecto_id`)
);

-- Insertar datos en la tabla registro_tiempo
INSERT INTO `registro_tiempo` (id, fecha, horas, descripcion, empleado_id, proyecto_id) VALUES 
(1, '2023-09-26', '08:00:00', 'Trabajo en el Proyecto 1', 1, 1),
(2, '2023-09-27', '07:30:00', 'Trabajo en el Proyecto 1', 2, 1),
(3, '2023-09-28', '06:00:00', 'Trabajo en el Proyecto 2', 2, 2);
