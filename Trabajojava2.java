package trabajo.programacion.java.pkg2;

import java.util.Scanner;
// Se importa esta clase para que el usuario pueda asignar los valores que desee

public class Trabajojava2 {

    public static void main(String[] args) {

        int vuelos[][] = new int[4][3];
        for (int f = 0; f < 4; f++) {
            for (int c = 0; c < 3; c++) {
                System.out.println("Ingrese la cantidad de asientos del vuelo " + f + " horario " + c);
                Scanner valor = new Scanner(System.in);
                vuelos[f][c] = valor.nextInt();
                /*
                Los "for" se utilizan para asignarle Valores a la matriz, que guarda la cantidad de asientos 
                que hay en distintos vuelos y distintos horarios de esos vuelos
                 */
            }
        }
        String seguir = "";
        Scanner valor2 = new Scanner(System.in);
        int ciudad, horario, asientos;
        System.out.println("RESERVACIONES");
        while (!seguir.equalsIgnoreCase("terminar")) {
            System.out.println("Ingrese el numero de la cuidad: ");
            ciudad = valor2.nextInt();
            System.out.println("Ingrese el numero del horario: ");
            horario = valor2.nextInt();
            System.out.println("Ingrese la cantidad de asientos que requiere: ");
            asientos = valor2.nextInt();
            /*
            Se crean tres variables que gurdan: la cuidad destino, el horario y 
            la cantidad de asientos que el usuario quiera reservar
             */
            if (ciudad >= 0 && ciudad <= 3) {
                if (horario >= 0 && horario <= 2) {

                    if (vuelos[ciudad][horario] >= asientos) {
                        System.out.println("Se han reservado " + asientos + " asientos Exitosamente");
                        vuelos[ciudad][horario] = vuelos[ciudad][horario] - asientos;
                    } else {
                        System.out.println("No hay asientos disponibles");
                        /*
                        Se usan condicionales para que el usuario no coloque un
                        valor que no este dentro de los parametros del programa 
                        
                         */
                    }
                }
            } else {
                System.out.println("Horario no Existe");

                System.out.println("ciudad no existe");
            }
            System.out.println("Al terminar con su reservacion Coloque 'Terminar' para acabar con su "
                    + "reservacion, de lo contrario coloque cualquier palabra/simbolo ");
            seguir = valor2.next();

        }

    }
}
