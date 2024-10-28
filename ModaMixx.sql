-- Crear la base de datos
CREATE DATABASE MODAMIXX;
GO

USE MODAMIX;
GO

-- Tabla de categorías (prendas, accesorios, etc.)
CREATE TABLE Categoria (
    CategoriaID INT PRIMARY KEY IDENTITY(1,1),
    NombreCategoria VARCHAR(100) NOT NULL
);

-- Tabla de productos (prendas y accesorios para hombre y mujer)
CREATE TABLE Producto (
    ProductoID INT PRIMARY KEY IDENTITY(1,1),
    NombreProducto VARCHAR(100) NOT NULL,
    DescripcionProducto VARCHAR(255),
    Precio DECIMAL(10,2) NOT NULL,
    Talla VARCHAR(10),
    Color VARCHAR(50),
    Genero VARCHAR(10) CHECK (Genero IN ('Hombre', 'Mujer')),
    CategoriaID INT FOREIGN KEY REFERENCES Categorias(CategoriaID)
);

-- Tabla de inventario
CREATE TABLE Inventarioo (
    InventarioID INT PRIMARY KEY IDENTITY(1,1),
    ProductoID INT FOREIGN KEY REFERENCES Productos(ProductoID),
    CantidadDisponible INT NOT NULL,
    FechaIngreso DATE
);

-- Tabla de clientes
CREATE TABLE Clientess (
    ClienteID INT PRIMARY KEY IDENTITY(1,1),
    NombreCliente VARCHAR(100) NOT NULL,
    CorreoCliente VARCHAR(100) NOT NULL UNIQUE,
    TelefonoCliente VARCHAR(15),
    DireccionCliente VARCHAR(255)
);

-- Tabla de pedidos
CREATE TABLE Pedidoss (
    PedidoID INT PRIMARY KEY IDENTITY(1,1),
    ClienteID INT FOREIGN KEY REFERENCES Clientes(ClienteID),
    FechaPedido DATE NOT NULL,
    TotalPedido DECIMAL(10,2) NOT NULL
);

-- Tabla de detalles de pedidos
CREATE TABLE DetallesPedidoo (
    DetalleID INT PRIMARY KEY IDENTITY(1,1),
    PedidoID INT FOREIGN KEY REFERENCES Pedidos(PedidoID),
    ProductoID INT FOREIGN KEY REFERENCES Productos(ProductoID),
    Cantidad INT NOT NULL,
    PrecioUnitario DECIMAL(10,2) NOT NULL
);

-- Inserción de datos iniciales en la tabla Categorías
INSERT INTO Categorias (NombreCategoria) VALUES
('Prendas Hombre'),
('Prendas Mujer'),
('Accesorios Hombre'),
('Accesorios Mujer');

-- Inserción de algunos productos de ejemplo
INSERT INTO Productos(NombreProducto, DescripcionProducto, Precio, Talla, Color, Genero, CategoriaID) VALUES
('Camiseta Polo', 'Camiseta casual de algodón', 29.99, 'M', 'Azul', 'Hombre', 1),
('Pantalón Jean', 'Pantalón denim de corte slim', 49.99, '32', 'Negro', 'Hombre', 1),
('Blusa Casual', 'Blusa ligera para uso diario', 24.99, 'S', 'Rojo', 'Mujer', 2),
('Vestido Elegante', 'Vestido de gala para ocasiones especiales', 89.99, 'L', 'Verde', 'Mujer', 2),
('Gorra Deportiva', 'Gorra ajustable para uso casual', 14.99, NULL, 'Negro', 'Hombre', 3),
('Bolso de Mano', 'Bolso de mano de cuero sintético', 59.99, NULL, 'Marrón', 'Mujer', 4);

-- Inserción de algunos datos en la tabla Inventario
INSERT INTO Inventario (ProductoID, CantidadDisponible, FechaIngreso) VALUES
(1, 100, '2024-10-10'),
(2, 50, '2024-10-10'),
(3, 200, '2024-10-10'),
(4, 30, '2024-10-10'),
(5, 150, '2024-10-10'),
(6, 80, '2024-10-10');

-- Ejemplo de cliente
INSERT INTO Clientess (NombreCliente, CorreoCliente, TelefonoCliente, DireccionCliente) VALUES
('Juan Pérez', 'juan.perez@example.com', '3216549870', 'Calle Falsa 123');

-- Ejemplo de pedido
INSERT INTO Pedidoss (ClienteID, FechaPedido, TotalPedido) VALUES
(1, '2024-10-10', 79.98);

-- Detalle del pedido
INSERT INTO DetallesPedidoo (PedidoID, ProductoID, Cantidad, PrecioUnitario) VALUES
(1, 1, 2, 29.99);




SELECT * FROM productos ;

SELECT * FROM Inventario ;


SELECT * FROM Clientess ;

SELECT * FROM Pedidoss;

SELECT * FROM DetallesPedidoo;

