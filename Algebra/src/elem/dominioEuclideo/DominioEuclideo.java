package elem.dominioEuclideo;

import elem.Elem;

public abstract class DominioEuclideo {
	
	private Elem elem;
	
	private static Elem cero;
	
	private static Elem uno;
	
	public abstract boolean igual(Elem e1, Elem e2);
	
	public abstract Elem suma(Elem e1, Elem e2);
	
	public abstract Elem resta(Elem e1, Elem e2);
	
	public abstract Elem producto(Elem e1, Elem e2);
	
	public abstract Elem division(Elem e1, Elem e2);
	
	public abstract int norma(Elem e1, Elem e2);
	
	public abstract Elem restoDiv(Elem e1, Elem e2);

	public Elem getCero() {
		return cero;
	}

	public void setCero(Elem cero) {
		this.cero = cero;
	}

	public Elem getUno() {
		return uno;
	}

	public void setUno(Elem uno) {
		this.uno = uno;
	}
	
	public Elem getElem() {
		return elem;
	}

	public void setElem(Elem elem) {
		this.elem = elem;
	}

}
