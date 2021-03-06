package main;

import elem.dfu.PolinomioEnteros;
import elem.dominioEuclideo.Enteros;
import elem.polinomio.Polinomio;

public class Main {

	public static void main(String args[]) {
		
		Integer[] a = new Integer[] {3, 5, 7}; Integer[] b = new Integer[] {4, 5, 33};
		Integer elem = (new Enteros()).chinoRestos(a, b);
		System.out.println(elem.toString());

		/**
		 * Complejo uno = new Complejo(3.0, 2.0); Complejo dos = new Complejo(1.0,
		 * -2.0); System.out.println(uno.division(dos).toString());
		 **/
		
		PolinomioEnteros dfu = new PolinomioEnteros(new Enteros());

		Polinomio<Integer> p = new Polinomio<Integer>(new Integer[] { 2, 2 });
		Polinomio<Integer> s = new Polinomio<Integer>(new Integer[] { 1, 0, 2 });
		Polinomio<Integer> q = dfu.producto(p, s);

		System.out.println(q.toString());

	}

}
