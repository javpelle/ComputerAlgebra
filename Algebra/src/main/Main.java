package main;

import elem.Elem;
import elem.Entero;
import elem.dominioEuclideo.Enteros;

public class Main {

	public static void main(String args[]) {
		Entero[] a = new Entero[] {new Entero(3), new Entero(5), new Entero(7)};
		Entero[] b = new Entero[] {new Entero(4), new Entero(5), new Entero(33)};
		Elem elem = (new Enteros()).chinoRestos(a, b);
		System.out.println(elem.toString());

	}

}
