#import pandas as pd
import sqlite3

# Conectamos con la base de datos chinook.db
connection = sqlite3.connect("almacen.db")

# Obtenemos un cursor que utilizaremos para hacer las queries
cursor= connection.cursor()
   
query_tabla_proveedores = """
CREATE TABLE Proveedores (
    CodigoProveedor INTEGER PRIMARY KEY,
    Nombre TEXT NOT NULL,
    Direccion TEXT,
    Ciudad TEXT,
    Provincia TEXT
);
"""
cursor.execute(query_tabla_proveedores)

query_tabla_categoria = """
CREATE TABLE Categoria (
    CodigoCategoria INT PRIMARY KEY,
    Nombre TEXT NOT NULL
);
"""
cursor.execute(query_tabla_categoria)


query_tabla_pieza="""
CREATE TABLE Piezas (
    CodigoPieza INT PRIMARY KEY,
    Nombre TEXT NOT NULL,
    Color TEXT,
    Precio FLOAT NOT NULL,
    CodigoCategoria INT,
    FOREIGN KEY (CodigoCategoria) REFERENCES Categoria(CodigoCategoria)
        ON DELETE SET NULL
        ON UPDATE CASCADE
);
"""

cursor.execute(query_tabla_pieza)

query_tabla_suministro="""
CREATE TABLE Suministro (
    CodigoSuministro INT PRIMARY KEY,
    CodigoProveedor INT NOT NULL,
    CodigoPieza INT NOT NULL,
    Cantidad INT NOT NULL,
    Fecha DATE NOT NULL,
    FOREIGN KEY (CodigoProveedor) REFERENCES Proveedores(CodigoProveedor)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (CodigoPieza) REFERENCES Piezas(CodigoPieza)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);
"""
cursor.execute(query_tabla_suministro)

# Datos para cada tabla
datos_categoria = [
    (1, 'Resistencias'),
    (2, 'Capacitores'),
    (3, 'Semiconductores'),
    (4, 'Conectores')
]

datos_proveedores = [
    (1, 'ElectroTech S.L.', 'Av. Innovación 123', 'Madrid', 'Madrid'),
    (2, 'Componentes Globales', 'Calle Tecnología 456', 'Barcelona', 'Cataluña'),
    (3, 'Distribuidora del Norte', 'Av. Central 789', 'Bilbao', 'País Vasco'),
    (4, 'Electronix S.A.', 'Calle Comercio 101', 'Sevilla', 'Andalucía'),
    (5, 'Conexiones Avanzadas', 'Av. Industria 202', 'Valencia', 'Comunidad Valenciana')
]

datos_piezas = [
    (1, 'Resistencia 10kΩ', 'Marrón', 0.05, 1),
    (2, 'Capacitor 100uF', 'Azul', 0.10, 2),
    (3, 'Transistor NPN', 'Negro', 0.50, 3),
    (4, 'Diodo LED', 'Rojo', 0.15, 3),
    (5, 'Conector USB Tipo-C', 'Plateado', 1.00, 4)
]

datos_suministro = [
    (1, 1, 1, 1000, '2024-01-01'),
    (2, 1, 2, 500, '2024-01-02'),
    (3, 2, 3, 200, '2024-01-03'),
    (4, 3, 4, 750, '2024-01-04'),
    (5, 4, 5, 300, '2024-01-05')
]

# Inserción de datos
cursor.executemany("INSERT INTO Categoria (CodigoCategoria, Nombre) VALUES (?, ?)", datos_categoria)
cursor.executemany("INSERT INTO Proveedores (CodigoProveedor, Nombre, Direccion, Ciudad, Provincia) VALUES (?, ?, ?, ?, ?)", datos_proveedores)
cursor.executemany("INSERT INTO Piezas (CodigoPieza, Nombre, Color, Precio, CodigoCategoria) VALUES (?, ?, ?, ?, ?)", datos_piezas)
cursor.executemany("INSERT INTO Suministro (CodigoSuministro, CodigoProveedor, CodigoPieza, Cantidad, Fecha) VALUES (?, ?, ?, ?, ?)", datos_suministro)

# Confirmar cambios y cerrar conexión
connection.commit()
connection.close()
