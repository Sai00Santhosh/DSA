package ADTs;
import java.util.ArrayList;

public class Stack {

    ArrayList<Integer> stack = new ArrayList<Integer>();

    public void push(int val){
        stack.add(val);
    }

    public int pop() throws Exception{

        if (stack.isEmpty()){
            throw new Exception("Stack is Empty");
        } else{
            int val = stack.get(stack.size() - 1);
            stack.remove(stack.size() - 1);
            return val;
        }

    }

    public boolean isEmpty(){
        return stack.isEmpty();
    }

    public int size(){
        return stack.size();
    }

    public void printStack(){
        System.out.println(stack);
    }
    
}
