package elem.dominioEuclideo;

import java.util.ArrayList;

import elem.Anillo;

public abstract class DominioEuclideo <T> implements Anillo<T>{

	public abstract T getUno();
	
	public abstract T division(T e1, T e2);
	
	public abstract T restoDiv(T e1, T e2);

	public abstract int norma(T e);


	public T mcd(T e1, T e2) {
		if (igual(e2, getCero())) {
			return e1;
		} else {
			return mcd(e2, restoDiv(e1, e2));
		}
	}

	/**
	 * 
	 * @param e1
	 * @param e2
	 * @return Devuelve un array de tamaño 3 [mcd, s, t] tal que mcd(e1,e2) = e1·s +
	 *         e2·t
	 */
	public ArrayList<T> euclidesExtendido(T e1, T e2) {
		if (igual(e2, getCero())) {
			ArrayList<T> aux = new ArrayList<T>();
			aux.add(e1);
			aux.add(getUno());
			aux.add(getCero());
			return aux;
		} else {
			ArrayList<T> elems = euclidesExtendido(e2, restoDiv(e1, e2));
			ArrayList<T> aux = new ArrayList<T>();
			aux.add(elems.get(0));
			aux.add(elems.get(2));
			aux.add(resta(elems.get(1), (producto((division(e1, e2)), elems.get(2)))));
			return aux;
		}
	}
	
	public T chinoRestos(T [] coprimes, T [] elems) {
		if (coprimes.length != elems.length) {
			return null;
		} else {
			// Inicialización
			T m = clone(coprimes[0]);
			for (int i = 1; i < coprimes.length; ++i) {
				m = producto(m, coprimes[i]);
			}
			// Computo algoritmo
			T result = getCero();
			for (int i = 0; i < coprimes.length; ++i) {
				T n = division(m, coprimes[i]);
				ArrayList<T> auxExtendido = euclidesExtendido(n, coprimes[i]);
				T c = restoDiv(producto(auxExtendido.get(1), elems[i]), coprimes[i]);
				result = suma(result, producto(c,n));
			}
			return result;
		}
	}

}
