package elem.polinomio;

import java.util.ArrayList;

public class Polinomio<T> {
	
	// en Z[x], 4x^2 -x +3 queda polinomio = [3, -1, 4]
	private ArrayList<T> polinomio;
	
	public Polinomio (ArrayList<T> polinomio) {
		this.polinomio = polinomio;
	}
	
	public Polinomio (T e) {
		polinomio = new ArrayList<T>();
		polinomio.add(e);
	}
	
	/**
	 * 
	 * @param e Array donde T[0] es coeficiente más significativo
	 * por ejemplo [2, 0, 1] es 2x^2 + 1 y se guarda en 
	 * polinomio como [1, 0, 2]
	 */
	public Polinomio (T[] e) {
		polinomio = new ArrayList<T>();
		for (int i = e.length - 1; i >= 0; --i) {
			polinomio.add(e[i]);
		}
	}
	
	public int size() {
		return polinomio.size();
	}
	
	public T get(int i) {
		return polinomio.get(i);
	}
	
	public void set(int i, T e) {
		polinomio.set(i, e);
	}
	
	public void add(T e) {
		polinomio.add(e);
	}
	
	public String toString() {
		String s = "";
		for (int i = polinomio.size() - 1; i > 0; --i) {
			s += "+(" + polinomio.get(i).toString() + ")x^" + String.valueOf(i) + " ";
		}
		return s + "+(" + polinomio.get(0).toString() + ")";
	}
	
	
	
}
