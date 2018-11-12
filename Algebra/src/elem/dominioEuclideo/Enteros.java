package elem.dominioEuclideo;

import elem.Elem;
import elem.Entero;

public class Enteros extends DominioEuclideo {

	private static Entero cero = new Entero(0);
	private static Entero uno = new Entero(1);

	@Override
	public boolean igual(Elem e1, Elem e2) {
		return ((Entero) e1).getElem() == ((Entero) e2).getElem();
	}

	@Override
	public Elem suma(Elem e1, Elem e2) {
		return new Entero(((Entero) e1).getElem() + ((Entero) e2).getElem());
	}

	@Override
	public Elem resta(Elem e1, Elem e2) {
		return new Entero(((Entero) e1).getElem() - ((Entero) e2).getElem());
	}

	@Override
	public Elem producto(Elem e1, Elem e2) {
		return new Entero(((Entero) e1).getElem() * ((Entero) e2).getElem());
	}

	@Override
	public Elem division(Elem e1, Elem e2) {
		return new Entero(((Entero) e1).getElem() / ((Entero) e2).getElem());
	}

	@Override
	public int norma(Elem e) {
		return ((Entero) e).getAbsElem();
	}

	@Override
	public Elem restoDiv(Elem e1, Elem e2) {
		return new Entero(((Entero) e1).getElem() % ((Entero) e2).getElem());
	}

	@Override
	public Elem getCero() {
		return cero;
	}

	@Override
	public Elem getUno() {
		return uno;
	}

}