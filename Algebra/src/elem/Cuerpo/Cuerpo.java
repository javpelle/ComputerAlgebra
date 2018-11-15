package elem.Cuerpo;

import elem.Anillo;

public abstract class Cuerpo<T> implements Anillo<T>{

	public abstract boolean igual(T e1, T e2);

	public abstract T suma(T e1, T e2);

	public abstract T resta(T e1, T e2);

	public abstract T producto(T e1, T e2);

	public abstract T division(T e1, T e2);

	public abstract T getCero();

	public abstract T getUno();

}
