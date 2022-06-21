package com.kuzey;
import java.util.NoSuchElementException;

public class LinkedList {

    private Node first;
    private Node last;
    private int size;

    public class Node {
        private int value;
        private Node next;

        public Node(int value) {
            this.value = value;
        }
    }

    public int size(){
        return size;
    }

    public int indexOf(int value){
        int counter = 0;
        var temp = first;
        while(temp!= null){
            if (temp.value == value) {
                return counter;
            }
            temp = temp.next;
            counter++;
        }
        return -1;
    }

    
    public boolean contains(int value) {
        return indexOf(value) != -1; //If there exists such item, return true
    }

    public void addLast(int item){
        var bruh = new Node(item); // Should have named the variable better...

        if (isEmpty()){
            first = bruh;
            last = bruh;
        }
        else {
            last.next = bruh;
            last = bruh;
        }
        size++;
    }


    public void addFirst(int item){ // Adding a node in the beginning
        var bruh = new Node(item);
        if (isEmpty()){
            first = bruh;
            last = bruh;
        }
        else{
            bruh.next = first;
            first = bruh;
        }
        size++;

    }

    public void removeFirst(){
        if (isEmpty()){ //If already empty
            throw new NoSuchElementException();
        }

        if (first == last){ // Meaning that there's only 1 element
            first = last = null;
            size=0;
        }else {

            var second = first.next;
            first.next = null;

            first = second;
            size--;
        }
    }

    public void removeLast(){
        if(first == null) // If there are no elements in the list
            throw new NoSuchElementException();
        if(first == last){ //If there's only 1 element
            first = last = null;
            size=0;
            return;
        }

        var previous = getPrevious(last);
        previous.next = null;
        last = previous;
        size--;
    }

    public int[] toArray(){
        var array = new int[size];
        var temp = first;
        for (int i = 0; i < size; i++){
            array[i] = temp.value; //Copying the values inside the linkedlist into the newly created array
            temp = temp.next;
        }
        return array;
    }

    private Node getPrevious(Node node){
        var temp = first;
        while (temp !=null){
            temp = temp.next;
            if(temp.next==node){
                return temp;}
        }
        return null;

    }

    public void reverse(){
        Node next;
        Node prev = null;
        var current = first;
        while(current != null){
            next = current.next;
            current.next = prev;
            prev = current;
            current = next;
        }
        first = last;

    }

    private boolean isEmpty(){
        return first == null;
    }
}



