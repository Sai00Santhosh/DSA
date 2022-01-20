package ADTs;
import java.util.ArrayList;

public class Bag {

    ArrayList<Integer> bag = new ArrayList<Integer>();

    public void add(int val){
        bag.add(val);
    }

    public boolean isEmpty(){
        return bag.isEmpty();
    }

    public int size(){
        return bag.size();
    }

    public void printBag(){
        System.out.println(bag);
    }
    
}
