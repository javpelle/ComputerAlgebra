package elem;

public interface Anillo <T> {
	
	public boolean igual(T e1, T e2);

	public T suma(T e1, T e2);

	public T resta(T e1, T e2);

	public T producto(T e1, T e2);

	public T getCero();

}
