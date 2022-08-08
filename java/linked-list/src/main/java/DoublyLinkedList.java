public class DoublyLinkedList<T> {
	private Node<T> head;
	private Node<T> tail;
    private int size = 0;
	
	private static class Node<T> {
        private T value;
        private Node<T> next;
        private Node<T> previous;
        
		public Node(T value) {
			this.value = value;
			this.next = null;
			this.previous = null;
		}
	}

    public void push(T value) {
        Node<T> node_new = new Node<>(value);
        if ( size > 0 ) {
            Node<T> node_old = tail;
            node_new.previous = node_old;
            node_old.next = node_new;
        } else {
            head = node_new;
        }
        tail = node_new;
        size += 1;
    }
    
    public T pop() {
        Node<T> node_old = tail;
        if ( size > 1 ) {
            Node<T> node_new = node_old.previous;
            node_new.next = null;
            tail = node_new;
        } else {
            head = null;
            tail = null;
        }
        size -= 1;
        return node_old.value;
    }
    
    public T shift() {
        Node<T> node_old = head;
        if ( size > 1 ) {
            Node<T> node_new = node_old.next;
            node_new.previous = null;
            head = node_new;
        } else {
            head = null;
            tail = null;
        }
        size -= 1;
        return node_old.value;
    }
    
    public void unshift(T value) {
        Node<T> node_new = new Node<>(value);
        if ( size > 0 ) {
            Node<T> node_old = head;
            node_new.next = node_old;
            node_old.previous = node_new;
        } else {
            tail = node_new;
        }
        head = node_new;
        size += 1;
    }
}
