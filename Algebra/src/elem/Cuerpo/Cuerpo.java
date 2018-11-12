package elem.Cuerpo;

import elem.Elem;

public abstract class Cuerpo {

	public abstract boolean igual(Elem e1, Elem e2);

	public abstract Elem suma(Elem e1, Elem e2);

	public abstract Elem resta(Elem e1, Elem e2);

	public abstract Elem producto(Elem e1, Elem e2);

	public abstract Elem division(Elem e1, Elem e2);

	public abstract Elem getCero();

	public abstract Elem getUno();

}
