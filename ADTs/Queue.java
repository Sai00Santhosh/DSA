package ADTs;
import java.util.ArrayList;

public class Queue {

    ArrayList<Integer> queue = new ArrayList<Integer>();

    public void enqueue(int val){
        queue.add(val);
    }
    
    public void dequeue() throws Exception{
        if (queue.isEmpty()){
            throw new Exception("Queue is Empty");
        } else{
            queue.remove(0);
        }
    }

    public boolean isEmpty(){
        return queue.isEmpty();
    }

    public int size(){
        return queue.size();
    }

    public void printQueue(){
        System.out.println(queue);
    }
}
