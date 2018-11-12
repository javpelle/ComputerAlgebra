package main;

import elem.Elem;
import elem.Entero;
import elem.dominioEuclideo.Enteros;

public class Main {

	public static void main(String args[]) {
		Entero a = new Entero(111);
		Entero b = new Entero(37);
		Elem[] elems = (new Enteros()).euclidesExtendido(a, b);
		for (int i = 0; i < 3; ++i) {
			System.out.println(elems[i].toString());
		}

	}

}
