package elem.Cuerpo;

import elem.Anillo;

public abstract class Cuerpo<T> implements Anillo<T>{

	public abstract T division(T e1, T e2);

	public abstract T getUno();

}
