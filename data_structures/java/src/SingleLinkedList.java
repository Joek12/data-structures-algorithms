public class SingleLinkedList {

    static class Node{
        protected int value;
        protected Node next;
        protected Node previous;

        public Node(int value){
            this.value = value;
            this.next = null;
            this.previous = null;
        }

        public Node(){
            this.next = null;
            this.previous = null;
        }

        public Node(Node prevNode, int value){
            this.next = prevNode;
            this.value = value;
        }

        public int getValue() {
            return value;
        }

        public Node getNext() {
            return next;
        }

        public Node getPrevious() {
            return previous;
        }

        public void setNext(Node next) {
            this.next = next;
        }

        public void setPrevious(Node previous) {
            this.previous = previous;
        }

        public void setValue(int value) {
            this.value = value;
        }
    }

    static class IndexError extends Throwable {
        public IndexError(){
            super();
        }

        public IndexError(String message){
            super(message);
        }

        public IndexError(Throwable cause){
            super(cause);
        }
    }

    Node head;
    int length;

    public SingleLinkedList(int[] arr){
        this.head = new Node();
        Node curr = this.head;
        for(int i: arr){
            curr.setValue(i);
            curr.setNext(new Node());
            curr = curr.getNext();
        }
    }

    public SingleLinkedList(){
        this.head = null;
        this.length = 0;
    }

    public SingleLinkedList(int len){
        this.head = new Node();
        Node curr = this.head;
        for(int i = 0; i < len; i++){
            curr.setNext(new Node());
            curr = curr.getNext();
        }
    }

    public int get(int index) throws IndexError{
        Node curr = traverse(index);
        return curr.getValue();
    }

    public void append(int value){

        if (this.head == null){
            this.head = new Node(value);
            this.length = 1;
            return;
        }

        Node curr = this.head;

        while(curr.next != null){
            curr = curr.getNext();
        }
        curr.setNext(new Node(value));
        this.length += 1;
    }

    protected Node traverse(int index) throws IndexError{

        Node curr = this.head;

        if (index > this.length - 1)
            throw new IndexError("List index out of range");

        for (int i = 0; i < index - 1; i++){
            if (curr.next == null)
                throw new IndexError("List index out of range");
            curr = curr.next;
        }

        return curr;
    }

    public void insert(int index, int value) throws IndexError{
        if (this.head == null){
            this.head = new Node(value);
            this.length = 1;
            return;
        }

        Node curr = traverse(index);
        Node temp = null;
        if (curr.getNext() != null)
            temp = curr.getNext();

        curr.setNext(new Node(value));
        curr.getNext().setNext(temp);
        this.length++;
    }

    public void pop() throws IndexError{
        Node curr = traverse(this.length - 1);
        curr.setNext(null);
        this.length--;
    }

    public static void main(String[] args) throws IndexError{
        SingleLinkedList list = new SingleLinkedList();
        list.append(3);
        list.append(5);
        System.out.println(list.get(0));
        list.pop();
        System.out.println(list.get(0));
    }
}
