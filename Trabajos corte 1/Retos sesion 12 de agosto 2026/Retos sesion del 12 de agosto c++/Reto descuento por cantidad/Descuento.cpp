#include <iostream>
#include <string>
using namespace std; 

int main ()
{   
    int cantidadProductos, precioUnitario, cantidadCompra, subtotal, valorFinal;
    string nombreProducto;
    cout<<"Ingrese la cantidad de productos que desea comprar"<<endl;
    cin>>cantidadProductos;
    int valorTotal=0;
    for (int i=0; i<cantidadProductos; i++)
    {
        cout<<"ingrese el nombre del producto "<<endl; 
        cin>>nombreProducto;

        cout<<"Ingrese el precio unitario "<<endl;
        cin>>precioUnitario;

        cout<<"Ingrese la cantidad comprada "<<endl;
        cin>>cantidadCompra;

        subtotal=precioUnitario*cantidadCompra; //operacion para encontrar el subtotal 
        valorTotal=valorTotal + subtotal; //acumula el subtotal de los productos para hallar el valor total
        
        //la razon por la que no guardo los nombres es porque el reto no estipula que sea necesario mostrarselos al cliente

    }

    if (valorTotal>300000)
    {
        cout<<"Aplicando descuento del 10%"<<endl;

        valorFinal= valorTotal-(valorTotal*0.1);

        cout<<"El valor antes del descuento era de "<<valorTotal<<"$ y despues del descuento es de "<<valorFinal<<"$ "<<endl;
    }

    else if (valorTotal<=300000 and valorTotal>=150000)
    {
        cout<<"Aplicando descuento del 5%"<<endl;

        valorFinal= valorTotal-(valorTotal*0.05);

        cout<<"El valor antes del descuento era de "<<valorTotal<<"$ y despues del descuento es de "<<valorFinal<<"$ "<<endl;
    }

    else 
    {
        cout<<"El valor de su compra es de "<<valorTotal<<"$"<<endl;
    }
    return 0;

}