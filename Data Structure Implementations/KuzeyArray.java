package com.kuzey;
public class KuzeyArray {
    private int[] numbers;
    private int count = 0;

    public KuzeyArray(int length){
       numbers = new int[length];
    }

    public void insert(int number){
        if (count == numbers.length){  // If the array is full
            int[] numbers2 = new int[numbers.length+1]; // New array with one more space
            // Copying the array and creating a temporary array
            for (int i = 0; i < numbers.length; i++){
                numbers2[i] = numbers[i];
            }
            numbers = numbers2;
        }
        numbers[count] = number;
        count++;
    }

    public int indexOf(int value){
        for (int i = 0; i < numbers.length; i++) //Traversing the array and looking for the target value.
            if (numbers[i] == value) // If we find the value
                return i;
            return -1; // There is no such value, we therefore return -1.
    }

    public void removeAt(int index) {
        if (index >= 0 && index < count) {
            for (int i = index; i < count - 1; i++) {
                numbers[i] = numbers[i + 1]; // Setting each value equal to the next index's value. 
            }
            count--; //The length of the array will decrease by 1.
            numbers[count] = 0; 
        }
        else { // If the given index is not valid
            throw new IllegalArgumentException();
        }
    }

    public void print(){
        for (int i = 0; i < count; i++){
            System.out.println(numbers[i]); //Printing the array in order
        }
    }

    public int max(){
        int biggest = numbers[0]; //Initial value for "biggest"
        for (int i : numbers){
            if (i > biggest) //If any number exceeds the biggest value so far, we change it.
                biggest = i;
        }
        return biggest;
    }

    public KuzeyArray intersect(KuzeyArray comparison1) {
        var yeni = new KuzeyArray(0);

        for (int i = 0; i < count; i++) {
            if(comparison1.indexOf(numbers[i])>-1){
                yeni.insert(numbers[i]);
            }
        }
        return yeni;
    }

    public void reverse(){
        int[] holder1 = new int[numbers.length];

        for (int i=count-1; i>-1; i--){
            holder1[count-i-1] = numbers[i];
        }
        numbers = holder1;
    }
}
