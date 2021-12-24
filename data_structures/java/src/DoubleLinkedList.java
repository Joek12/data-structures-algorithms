public class DoubleLinkedList extends SingleLinkedList{


    Node head;

    public DoubleLinkedList(int[] arr){
        this.head = new Node();
        Node curr = this.head;
        for(int i: arr){
            curr.setValue(i);
            curr.setNext(new Node());
            curr.getNext().setPrevious(curr);
            curr = curr.getNext();
        }
        this.length = arr.length;

    }
    public DoubleLinkedList(int len){
        this.head = new Node();
        Node curr = this.head;
        for(int i = 0; i < len; i++){
            curr.setNext(new Node());
            curr.getNext().setPrevious(curr);
            curr = curr.getNext();
        }
        this.length = len;
    }
    public DoubleLinkedList(){
        this.head = null;
        this.length = 0;
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
        curr.setNext(new Node(curr, value));
        this.length++;

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

        curr.setNext(new Node(curr, value));
        curr.getNext().setNext(temp);
        temp.setPrevious(curr.getNext());
        this.length++;
    }
}
