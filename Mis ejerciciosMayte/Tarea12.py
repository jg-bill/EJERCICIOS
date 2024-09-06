cant= int (input( "Cantidad de productos vendidos: "))
precio= int (input( "Precio de productos vendidos: "))
IGV=0.18
subtotal= cant*precio
IGVTotal= subtotal * IGV
TotalPagar=subtotal+IGVTotal
print (" EL SUB TOTAL ES IGUAL A", subtotal, " EL IGVTOTAL ES ", IGVTotal, " Y EL TOTAL A PAGAR ES", TotalPagar)