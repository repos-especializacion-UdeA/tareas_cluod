namespace py Servicios

enum TipoEstructura {
  VENTA = 1,
  GARANTIA = 2
}

struct Venta {
	1: string cod_producto,
	2: string producto,
	3: string cod_venta,
	4: string ced_cliente,
	5: string nombre_cliente,
	6: string fecha_venta,
	7: string tipo_garantia,
	8: i32 tiempo_garantia,
	9: i32 valor_venta,
	10: string tipo_tienda,
    11: string ciudad_sede,
	12: string sede,
	13: string entrega,
	14: string vendedor,
	15: i32 calificacion_servicio,
	16: string comentario_servicio
}

struct Garantia {
	1: string cod_venta,
	2: string fecha_compra,
	3: string tipo_garantia,
	4: i32 tiempo_garantia,
	5: i32 calificacion,
	6: string comentarios,
	7: string detalle_garantia
}

struct Contenedor {
  1: TipoEstructura tipo,
  2: binary datos
}