package elem.dominioEuclideo;

import elem.Elem;

public abstract class DominioEuclideo {

	public abstract boolean igual(Elem e1, Elem e2);

	public abstract Elem suma(Elem e1, Elem e2);

	public abstract Elem resta(Elem e1, Elem e2);

	public abstract Elem producto(Elem e1, Elem e2);

	public abstract Elem division(Elem e1, Elem e2);

	public abstract int norma(Elem e);

	public abstract Elem restoDiv(Elem e1, Elem e2);

	public abstract Elem getCero();

	public abstract Elem getUno();

	public Elem mcd(Elem e1, Elem e2) {
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
	public Elem[] euclidesExtendido(Elem e1, Elem e2) {
		if (igual(e2, getCero())) {
			return new Elem[] { e1, getUno(), getCero() };
		} else {
			Elem[] elems = euclidesExtendido(e2, restoDiv(e1, e2));
			return new Elem[] { elems[0], elems[2], resta(elems[1], (producto((division(e1, e2)), elems[2]))) };
		}
	}
	
	public Elem chinoRestos(Elem [] coprimes, Elem [] elems) {
		if (coprimes.length != elems.length) {
			return null;
		} else {
			// Inicialización
			Elem m = coprimes[0].clone();
			for (int i = 1; i < coprimes.length; ++i) {
				m = producto(m, coprimes[i]);
			}
			// Computo algoritmo
			Elem result = getCero();
			for (int i = 0; i < coprimes.length; ++i) {
				Elem n = division(m, coprimes[i]);
				Elem[] auxExtendido = euclidesExtendido(n, coprimes[i]);
				Elem c = restoDiv(producto(auxExtendido[1], elems[i]), coprimes[i]);
				result = suma(result, producto(c,n));
			}
			return result;
		}
	}

}
