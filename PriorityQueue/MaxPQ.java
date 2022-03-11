package PriorityQueue;
import java.util.ArrayList;
import java.util.Collections;

public class MaxPQ {

    ArrayList<Integer> pq = new ArrayList<Integer>();

    public boolean isEmpty(){
        return pq.isEmpty();
    }

    public int size(){
        return pq.size();
    }

    public void insert(int val){
        if(size() == 0){
            pq.add(val);
        } else{
            pq.add(val);
            swim(val);
        }
        
    }

    public int delMax(){
        int max = pq.get(1);
        exch(1, pq.get(size() - 1));
        sink(1);
        pq.remove(size());
        return max;
    }

    public int max() throws Exception{
        if(isEmpty()){
            throw new Exception("No element in Priority Queue");
        } else{
            return pq.get(0);
        }
    }

    // Helper Funtions

    private void swim(int k) {
        while (k > 1 && less(k/2, k)) {
            exch(k, k/2);
            k = k/2;
        }
    }

    private void sink(int k) {
        while (2*k <= pq.size()) {
            int j = 2*k;
            if (j < pq.size() && (j < j+1)) j++;
            if (!(k < j)) break;
            exch(k, j);
            k = j;
        }
    }

    private boolean less(int i, int j){
        return pq.get(i).compareTo(pq.get(j)) < 0;
    }
    
    private void exch(int i, int j) {
        Collections.swap(pq, i, j);
    }

    public void printMaxPQ(){
        System.out.println(pq);
    }

}
