package javaapplication4;

import java.util.Scanner;

public class Tabajojava1 {

    public static void main(String[] args) {
        String ciudades[] = new String[4];
        double minimas[] = new double[4];
        double maximas[] = new double[4];
        /*
        se declaran e inicializan los vectores, ciudades para almacenar los nombres de las ciudades,
        y minimas y maximas para almacenar las temperaturas mínimas y máximas respectivamente.
         */
        Scanner valor = new Scanner(System.in);
        Scanner valor2 = new Scanner(System.in);

        for (int i = 0; i < 4; i++) {
            System.out.println("Ingrese el nombre de la ciudad " + i);
            ciudades[i] = valor.next();

            System.out.println("Cual es la temperatura minima de la ciudad " + i);
            minimas[i] = valor2.nextDouble();

            System.out.println("Cual es la temperatura maxima de la ciudad " + i);
            maximas[i] = valor2.nextDouble();
            /*
            El siguiente bloque de código recorre un bucle for para pedir al usuario que 
            ingrese los nombres de las ciudades y sus temperaturas mínimas y máximas:
             */
        }

        double minima = 999999.00;
        int posmin = -1;

        for (int i = 0; i < 4; i++) {

            if (minimas[i] < minima) {
                minima = minimas[i];
                posmin = i;

            }

        }
        double maxima = -999999.00;
        int posmax = -1;
        for (int i = 0; i < 4; i++) {
            if (maximas[i] > maxima) {
                maxima = maximas[i];
                posmax = i;
            }
            /*
            se determina cuál fue la temperatura mínima y máxima registrada y 
            en qué ciudad ocurrió cada una:
             */
        }

        System.out.println("la temperatura minima registrada fue de " + minima);
        System.out.println("Fue en la ciudad: " + ciudades[posmin]);
        System.out.println("la temperatura maxima registrada fue de " + maxima);
        System.out.println("Fue en la ciudad: " + ciudades[posmax]);
        /*
        Se imprime las temperaturas mínima y máxima registradas
        y las ciudades en las que se registraron:
         */
    }

}
