-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 06-03-2024 a las 13:43:10
-- Versión del servidor: 10.4.28-MariaDB
-- Versión de PHP: 8.0.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `stfg`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `clases`
--

CREATE TABLE `clases` (
  `Id` bigint(20) NOT NULL,
  `Orden` int(11) NOT NULL,
  `Tipo` smallint(6) NOT NULL,
  `Nombre` varchar(50) NOT NULL,
  `Descripcion` varchar(300) NOT NULL,
  `Creador` bigint(20) NOT NULL,
  `Fecha_alta` datetime NOT NULL DEFAULT current_timestamp(),
  `Fecha_mov` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `clases`
--

INSERT INTO `clases` (`Id`, `Orden`, `Tipo`, `Nombre`, `Descripcion`, `Creador`, `Fecha_alta`, `Fecha_mov`) VALUES
(1, 1, 1, 'Escalas', 'Escala mayor', 1, '2023-10-17 12:33:36', '2023-10-17 12:33:36'),
(2, 2, 2, 'Escalas', 'Escala mayor', 1, '2023-11-07 17:16:26', '2023-11-07 17:16:26');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `lecciones`
--

CREATE TABLE `lecciones` (
  `Id` bigint(20) NOT NULL,
  `Clase` bigint(20) NOT NULL,
  `Plantilla` bigint(20) NOT NULL,
  `Orden` int(11) NOT NULL,
  `Mensaje` bigint(20) NOT NULL,
  `Creador` bigint(20) NOT NULL,
  `Fecha_alta` datetime NOT NULL DEFAULT current_timestamp(),
  `Fecha_mov` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `lecciones`
--

INSERT INTO `lecciones` (`Id`, `Clase`, `Plantilla`, `Orden`, `Mensaje`, `Creador`, `Fecha_alta`, `Fecha_mov`) VALUES
(1, 1, 1, 1, 1, 1, '2023-10-17 12:36:57', '2023-10-17 12:36:57'),
(2, 1, 1, 2, 2, 1, '2023-11-05 11:50:40', '2023-11-05 11:50:40'),
(3, 1, 1, 3, 3, 1, '2023-11-05 13:07:42', '2023-11-05 13:07:42'),
(4, 2, 2, 5, 3, 1, '2023-11-05 16:54:23', '2023-11-05 16:54:23'),
(5, 2, 2, 6, 3, 1, '2023-11-08 10:50:08', '2023-11-08 10:50:08'),
(7, 2, 2, 4, 3, 1, '2023-11-12 11:52:48', '2023-11-12 11:52:48');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `mensajes`
--

CREATE TABLE `mensajes` (
  `Id` bigint(20) NOT NULL,
  `Texto` text NOT NULL,
  `Media` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `mensajes`
--

INSERT INTO `mensajes` (`Id`, `Texto`, `Media`) VALUES
(1, 'Una escala Mayor es un conjunto de 7 notas separadas entre si por tonos o semitonos, cuya sonoridad, da sensación de alegría. Sobre todo, la escala Mayor es el tipo de escala más usada en la música que escuchamos en la actualidad', ''),
(2, 'Una melodía es una sucesión de sonidos en una secuencia lineal, es decir, a lo largo del tiempo, y tiene una identidad y significado propio dentro de un entorno sonoro particular.', ''),
(3, 'Intenta tocar las notas con el dedo índice siguiendo la melodía.', '');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `notas`
--

CREATE TABLE `notas` (
  `Id` int(11) NOT NULL,
  `Escala` int(11) NOT NULL,
  `Nombre_latino` varchar(5) NOT NULL,
  `Nombre_ingles` varchar(2) NOT NULL,
  `Origen` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `notas`
--

INSERT INTO `notas` (`Id`, `Escala`, `Nombre_latino`, `Nombre_ingles`, `Origen`) VALUES
(1, 3, 'DO', 'C', 'C3.wav'),
(2, 3, 'DO#', 'Db', 'Db3.wav'),
(3, 3, 'RE', 'D', 'D3.wav'),
(4, 3, 'RE#', 'Eb', 'Eb3.wav'),
(5, 3, 'MI', 'E', 'E3.wav'),
(6, 3, 'FA', 'F', 'F3.wav'),
(7, 3, 'FA#', 'Gb', 'Gb3.wav'),
(8, 3, 'SOL', 'G', 'G3.wav'),
(9, 3, 'SOL#', 'Ab', 'Ab3.wav'),
(10, 3, 'LA', 'A', 'A3.wav'),
(11, 3, 'LA#', 'Bb', 'Bb3.wav'),
(12, 3, 'SI', 'B', 'B3.wav'),
(13, 2, 'DO', 'C', 'C2.wav'),
(14, 2, 'DO#', 'Db', 'Db2.wav'),
(15, 2, 'RE', 'D', 'D2.wav'),
(16, 2, 'RE#', 'Eb', 'Eb2.wav'),
(17, 2, 'MI', 'E', 'E2.wav'),
(18, 2, 'FA', 'F', 'F2.wav'),
(19, 2, 'FA#', 'Gb', 'Gb2.wav'),
(20, 2, 'SOL', 'G', 'G2.wav'),
(21, 2, 'SOL#', 'Ab', 'Ab2.wav'),
(22, 2, 'LA', 'A', 'A2.wav'),
(23, 2, 'LA#', 'Bb', 'Bb2.wav'),
(24, 2, 'SI', 'B', 'B2.wav'),
(28, 1, 'DO', 'C', 'C1.wav'),
(29, 1, 'DO#', 'Db', 'Db1.wav'),
(30, 1, 'RE', 'D', 'D1.wav'),
(31, 1, 'RE#', 'Eb', 'Eb1.wav'),
(32, 1, 'MI', 'E', 'E1.wav'),
(33, 1, 'FA', 'F', 'F1.wav'),
(34, 1, 'FA#', 'Gb', 'Gb1.wav'),
(35, 1, 'SOL', 'G', 'G1.wav'),
(36, 1, 'SOL#', 'Ab', 'Ab1.wav'),
(37, 1, 'LA', 'A', 'A1.wav'),
(38, 1, 'LA#', 'Bb', 'Bb1.wav'),
(39, 1, 'SI', 'B', 'B1.wav'),
(43, 5, 'DO', 'C', 'C5.wav'),
(44, 5, 'DO#', 'Db', 'Db5.wav'),
(45, 5, 'RE', 'D', 'D5.wav'),
(46, 5, 'RE#', 'Eb', 'Eb5.wav'),
(47, 5, 'MI', 'E', 'E5.wav'),
(48, 5, 'FA', 'F', 'F5.wav'),
(49, 5, 'FA#', 'Gb', 'Gb5.wav'),
(50, 5, 'SOL', 'G', 'G5.wav'),
(51, 5, 'SOL#', 'Ab', 'Ab5.wav'),
(52, 5, 'LA', 'A', 'A5.wav'),
(53, 5, 'LA#', 'Bb', 'Bb5.wav'),
(54, 5, 'SI', 'B', 'B5.wav'),
(58, 4, 'DO', 'C', 'C4.wav'),
(59, 4, 'DO#', 'Db', 'Db4.wav'),
(60, 4, 'RE', 'D', 'D4.wav'),
(61, 4, 'RE#', 'Eb', 'Eb4.wav'),
(62, 4, 'MI', 'E', 'E4.wav'),
(63, 4, 'FA', 'F', 'F4.wav'),
(64, 4, 'FA#', 'Gb', 'Gb4.wav'),
(65, 4, 'SOL', 'G', 'G4.wav'),
(66, 4, 'SOL#', 'Ab', 'Ab4.wav'),
(67, 4, 'LA', 'A', 'A4.wav'),
(68, 4, 'LA#', 'Bb', 'Bb4.wav'),
(69, 4, 'SI', 'B', 'B4.wav'),
(73, 6, 'DO', 'C', 'C6.wav'),
(74, 6, 'DO#', 'Db', 'Db6.wav'),
(75, 6, 'RE', 'D', 'D6.wav'),
(76, 6, 'RE#', 'Eb', 'Eb6.wav'),
(77, 6, 'MI', 'E', 'E6.wav'),
(78, 6, 'FA', 'F', 'F6.wav'),
(79, 6, 'FA#', 'Gb', 'Gb6.wav'),
(80, 6, 'SOL', 'G', 'G6.wav'),
(81, 6, 'SOL#', 'Ab', 'Ab6.wav'),
(82, 6, 'LA', 'A', 'A6.wav'),
(83, 6, 'LA#', 'Bb', 'Bb6.wav'),
(84, 6, 'SI', 'B', 'B6.wav'),
(88, 7, 'DO', 'C', 'C7.wav'),
(89, 7, 'DO#', 'Db', 'Db7.wav'),
(90, 7, 'RE', 'D', 'D7.wav'),
(91, 7, 'RE#', 'Eb', 'Eb7.wav'),
(92, 7, 'MI', 'E', 'E7.wav'),
(93, 7, 'FA', 'F', 'F7.wav'),
(94, 7, 'FA#', 'Gb', 'Gb7.wav'),
(95, 7, 'SOL', 'G', 'G7.wav'),
(96, 7, 'SOL#', 'Ab', 'Ab7.wav'),
(97, 7, 'LA', 'A', 'A7.wav'),
(98, 7, 'LA#', 'Bb', 'Bb7.wav'),
(99, 7, 'SI', 'B', 'B7.wav');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `plantillas`
--

CREATE TABLE `plantillas` (
  `Id` bigint(20) NOT NULL,
  `Nombre` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `plantillas`
--

INSERT INTO `plantillas` (`Id`, `Nombre`) VALUES
(1, 'Clase básica'),
(2, 'Practica');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `plantilla_detalle`
--

CREATE TABLE `plantilla_detalle` (
  `id` int(11) NOT NULL,
  `id_plantilla` bigint(20) NOT NULL,
  `nota` int(11) NOT NULL,
  `color_nota` varchar(15) NOT NULL,
  `posicion_x` int(11) NOT NULL,
  `posicion_y` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `plantilla_detalle`
--

INSERT INTO `plantilla_detalle` (`id`, `id_plantilla`, `nota`, `color_nota`, `posicion_x`, `posicion_y`) VALUES
(1, 1, 1, '(255,0,0)', 100, 100),
(2, 1, 3, '(0,255,0)', 100, 200),
(3, 1, 5, '(144,12,43)', 100, 300),
(4, 1, 6, '(255,228,0)', 100, 400),
(5, 1, 8, '(255,0,255)', 100, 500),
(6, 1, 10, '(0,255,255)', 100, 600),
(7, 1, 12, '(255,165,0)', 100, 700),
(8, 2, 1, '(255,0,0)', 100, 100),
(9, 2, 3, '(0,255,0)', 100, 200),
(10, 2, 5, '(144,12,43)', 100, 300),
(11, 2, 6, '(255,228,0)', 100, 400),
(12, 2, 8, '(255,0,255)', 100, 500),
(13, 2, 10, '(0,255,255)', 100, 600),
(14, 2, 12, '(255,165,0)', 100, 700);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `progreso`
--

CREATE TABLE `progreso` (
  `Id` bigint(20) NOT NULL,
  `Usuario` bigint(20) NOT NULL,
  `Clase` bigint(20) NOT NULL,
  `Leccion` bigint(20) DEFAULT NULL,
  `Fecha` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `progreso`
--

INSERT INTO `progreso` (`Id`, `Usuario`, `Clase`, `Leccion`, `Fecha`) VALUES
(5, 1, 2, 4, '2023-11-14 10:52:25'),
(8, 1, 1, 3, '2024-03-03 18:04:49');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `secuencias`
--

CREATE TABLE `secuencias` (
  `Id` bigint(20) NOT NULL,
  `Leccion` bigint(20) NOT NULL,
  `Nota` int(11) NOT NULL,
  `Tiempo` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `secuencias`
--

INSERT INTO `secuencias` (`Id`, `Leccion`, `Nota`, `Tiempo`) VALUES
(1, 1, 1, 3),
(2, 1, 3, 3),
(3, 1, 5, 3),
(4, 1, 6, 3),
(5, 1, 8, 3),
(6, 1, 10, 3),
(7, 1, 12, 3),
(8, 2, 1, 3),
(9, 2, 3, 3),
(10, 2, 5, 3),
(11, 2, 6, 3),
(12, 2, 8, 3),
(13, 2, 10, 3),
(14, 2, 12, 3),
(17, 3, 1, 3),
(18, 3, 3, 3),
(19, 3, 5, 3),
(20, 3, 6, 3),
(21, 3, 8, 3),
(22, 3, 10, 3),
(23, 3, 12, 3),
(32, 4, 12, 4),
(33, 4, 12, 4),
(34, 4, 1, 4),
(35, 4, 3, 4),
(36, 4, 3, 4),
(37, 4, 1, 4),
(38, 4, 12, 4),
(39, 4, 10, 4),
(40, 4, 8, 4),
(41, 4, 8, 4),
(42, 4, 10, 4),
(43, 4, 12, 4),
(44, 4, 12, 3),
(45, 4, 10, 4),
(46, 4, 10, 4),
(47, 5, 5, 4),
(48, 5, 24, 5),
(49, 5, 1, 5),
(50, 5, 3, 4),
(51, 5, 22, 4),
(52, 5, 22, 5),
(53, 5, 1, 5),
(54, 5, 5, 4),
(55, 5, 3, 5),
(56, 5, 1, 5),
(57, 5, 24, 4),
(58, 5, 1, 5),
(59, 5, 3, 5),
(60, 5, 5, 4),
(61, 5, 1, 4),
(62, 5, 22, 4),
(63, 5, 22, 3),
(64, 7, 1, 3),
(65, 7, 5, 3),
(66, 7, 3, 3),
(67, 7, 6, 3),
(68, 7, 5, 3),
(69, 7, 8, 3),
(70, 7, 6, 3),
(71, 7, 10, 3),
(72, 7, 8, 3),
(73, 7, 12, 3);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tiempos`
--

CREATE TABLE `tiempos` (
  `Id` int(20) NOT NULL,
  `Tempo` varchar(15) NOT NULL,
  `Valor` float NOT NULL,
  `Imagen` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `tiempos`
--

INSERT INTO `tiempos` (`Id`, `Tempo`, `Valor`, `Imagen`) VALUES
(1, 'redonda', 4, 'redonda.jpg'),
(2, 'blanca', 2, 'blanca.jpg'),
(3, 'negra', 1, 'negra.jpg'),
(4, 'corchea', 0.5, 'corchea.jpg'),
(5, 'semicorchea', 0.25, 'semicorchea.jpg'),
(6, 'fusa', 0.125, 'fusa.jpg'),
(7, 'semifusa', 0.0625, 'semifusa.jpg');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tipos`
--

CREATE TABLE `tipos` (
  `Id` smallint(6) NOT NULL,
  `Nombre` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `tipos`
--

INSERT INTO `tipos` (`Id`, `Nombre`) VALUES
(1, 'Clase'),
(2, 'Practica');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `Id` bigint(20) NOT NULL,
  `Tipo` smallint(6) NOT NULL,
  `Nombre` varchar(50) NOT NULL,
  `Apellido` varchar(50) NOT NULL,
  `Email` varchar(100) NOT NULL,
  `Clave` varchar(250) NOT NULL,
  `Token` varchar(300) NOT NULL,
  `Fecha_alta` datetime NOT NULL DEFAULT current_timestamp(),
  `Fecha_mod` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`Id`, `Tipo`, `Nombre`, `Apellido`, `Email`, `Clave`, `Token`, `Fecha_alta`, `Fecha_mod`) VALUES
(1, 1, 'Gustavo', 'Futo', 'gus@gmail.com', '$2b$12$pMRbI9.H.GMlXSWV/zlSkOwsdKxHH9EPa3CHB1aTanfUovLnFbjWW', 'dsfkdglkhlskghdkghkjghdfkjghfdkjghfdslkghdg64564654d6gfd4gfdgfdg4654g56dfgdkdsfpds', '2023-10-17 11:39:28', '2023-11-12 16:21:52');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `clases`
--
ALTER TABLE `clases`
  ADD PRIMARY KEY (`Id`),
  ADD KEY `Creador` (`Creador`),
  ADD KEY `Tipo` (`Tipo`);

--
-- Indices de la tabla `lecciones`
--
ALTER TABLE `lecciones`
  ADD PRIMARY KEY (`Id`),
  ADD KEY `lecciones_ibfk_1` (`Clase`),
  ADD KEY `Creador` (`Creador`),
  ADD KEY `Mensaje` (`Mensaje`),
  ADD KEY `Plantilla` (`Plantilla`);

--
-- Indices de la tabla `mensajes`
--
ALTER TABLE `mensajes`
  ADD PRIMARY KEY (`Id`);

--
-- Indices de la tabla `notas`
--
ALTER TABLE `notas`
  ADD PRIMARY KEY (`Id`);

--
-- Indices de la tabla `plantillas`
--
ALTER TABLE `plantillas`
  ADD PRIMARY KEY (`Id`);

--
-- Indices de la tabla `plantilla_detalle`
--
ALTER TABLE `plantilla_detalle`
  ADD PRIMARY KEY (`id`),
  ADD KEY `nota` (`nota`),
  ADD KEY `id_plantilla` (`id_plantilla`);

--
-- Indices de la tabla `progreso`
--
ALTER TABLE `progreso`
  ADD PRIMARY KEY (`Id`),
  ADD KEY `Usuario` (`Usuario`),
  ADD KEY `Clase` (`Clase`);

--
-- Indices de la tabla `secuencias`
--
ALTER TABLE `secuencias`
  ADD PRIMARY KEY (`Id`),
  ADD KEY `Nota` (`Nota`),
  ADD KEY `Leccion` (`Leccion`),
  ADD KEY `Tiempo` (`Tiempo`);

--
-- Indices de la tabla `tiempos`
--
ALTER TABLE `tiempos`
  ADD PRIMARY KEY (`Id`);

--
-- Indices de la tabla `tipos`
--
ALTER TABLE `tipos`
  ADD PRIMARY KEY (`Id`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`Id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `clases`
--
ALTER TABLE `clases`
  MODIFY `Id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `lecciones`
--
ALTER TABLE `lecciones`
  MODIFY `Id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `mensajes`
--
ALTER TABLE `mensajes`
  MODIFY `Id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `notas`
--
ALTER TABLE `notas`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=100;

--
-- AUTO_INCREMENT de la tabla `plantillas`
--
ALTER TABLE `plantillas`
  MODIFY `Id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `plantilla_detalle`
--
ALTER TABLE `plantilla_detalle`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT de la tabla `progreso`
--
ALTER TABLE `progreso`
  MODIFY `Id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT de la tabla `secuencias`
--
ALTER TABLE `secuencias`
  MODIFY `Id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=74;

--
-- AUTO_INCREMENT de la tabla `tiempos`
--
ALTER TABLE `tiempos`
  MODIFY `Id` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT de la tabla `tipos`
--
ALTER TABLE `tipos`
  MODIFY `Id` smallint(6) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `Id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `clases`
--
ALTER TABLE `clases`
  ADD CONSTRAINT `clases_ibfk_1` FOREIGN KEY (`Creador`) REFERENCES `usuarios` (`Id`),
  ADD CONSTRAINT `clases_ibfk_2` FOREIGN KEY (`Tipo`) REFERENCES `tipos` (`Id`);

--
-- Filtros para la tabla `lecciones`
--
ALTER TABLE `lecciones`
  ADD CONSTRAINT `lecciones_ibfk_1` FOREIGN KEY (`Clase`) REFERENCES `clases` (`Id`),
  ADD CONSTRAINT `lecciones_ibfk_2` FOREIGN KEY (`Creador`) REFERENCES `usuarios` (`Id`),
  ADD CONSTRAINT `lecciones_ibfk_3` FOREIGN KEY (`Mensaje`) REFERENCES `mensajes` (`Id`),
  ADD CONSTRAINT `lecciones_ibfk_4` FOREIGN KEY (`Plantilla`) REFERENCES `plantillas` (`Id`);

--
-- Filtros para la tabla `plantilla_detalle`
--
ALTER TABLE `plantilla_detalle`
  ADD CONSTRAINT `plantilla_detalle_ibfk_1` FOREIGN KEY (`nota`) REFERENCES `notas` (`Id`),
  ADD CONSTRAINT `plantilla_detalle_ibfk_2` FOREIGN KEY (`id_plantilla`) REFERENCES `plantillas` (`Id`);

--
-- Filtros para la tabla `progreso`
--
ALTER TABLE `progreso`
  ADD CONSTRAINT `progreso_ibfk_1` FOREIGN KEY (`Usuario`) REFERENCES `usuarios` (`Id`),
  ADD CONSTRAINT `progreso_ibfk_2` FOREIGN KEY (`Clase`) REFERENCES `clases` (`Id`);

--
-- Filtros para la tabla `secuencias`
--
ALTER TABLE `secuencias`
  ADD CONSTRAINT `secuencias_ibfk_1` FOREIGN KEY (`Nota`) REFERENCES `notas` (`Id`),
  ADD CONSTRAINT `secuencias_ibfk_4` FOREIGN KEY (`Leccion`) REFERENCES `lecciones` (`Id`),
  ADD CONSTRAINT `secuencias_ibfk_5` FOREIGN KEY (`Tiempo`) REFERENCES `tiempos` (`Id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
