# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: servicios.proto
# Protobuf Python Version: 4.25.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0fservicios.proto\x12\tServicios\"\xe0\x02\n\x05Venta\x12\x14\n\x0c\x63od_producto\x18\x01 \x01(\t\x12\x10\n\x08producto\x18\x02 \x01(\t\x12\x11\n\tcod_venta\x18\x03 \x01(\t\x12\x13\n\x0b\x63\x65\x64_cliente\x18\x04 \x01(\t\x12\x16\n\x0enombre_cliente\x18\x05 \x01(\t\x12\x13\n\x0b\x66\x65\x63ha_venta\x18\x06 \x01(\t\x12\x15\n\rtipo_garantia\x18\x07 \x01(\t\x12\x17\n\x0ftiempo_garantia\x18\x08 \x01(\x05\x12\x13\n\x0bvalor_venta\x18\t \x01(\x05\x12\x13\n\x0btipo_tienda\x18\n \x01(\t\x12\x13\n\x0b\x63iudad_sede\x18\x0b \x01(\t\x12\x0c\n\x04sede\x18\x0c \x01(\t\x12\x0f\n\x07\x65ntrega\x18\r \x01(\t\x12\x10\n\x08vendedor\x18\x0e \x01(\t\x12\x1d\n\x15\x63\x61lificacion_servicio\x18\x0f \x01(\x05\x12\x1b\n\x13\x63omentario_servicio\x18\x10 \x01(\t\"\xa8\x01\n\x08Garantia\x12\x11\n\tcod_venta\x18\x01 \x01(\t\x12\x14\n\x0c\x66\x65\x63ha_compra\x18\x02 \x01(\t\x12\x15\n\rtipo_garantia\x18\x03 \x01(\t\x12\x17\n\x0ftiempo_garantia\x18\x04 \x01(\x05\x12\x14\n\x0c\x63\x61lificacion\x18\x05 \x01(\x05\x12\x13\n\x0b\x63omentarios\x18\x06 \x01(\t\x12\x18\n\x10\x64\x65talle_garantia\x18\x07 \x01(\tb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'servicios_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_VENTA']._serialized_start=31
  _globals['_VENTA']._serialized_end=383
  _globals['_GARANTIA']._serialized_start=386
  _globals['_GARANTIA']._serialized_end=554
# @@protoc_insertion_point(module_scope)
