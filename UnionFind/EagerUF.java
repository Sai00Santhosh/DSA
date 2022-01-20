package UnionFind;

import java.util.ArrayList;

public class EagerUF implements UnionFind { // Also known as QuickFindUF

    private ArrayList<Integer> id = new ArrayList<Integer>();
    private int count;

    public EagerUF(int N){
        count = N;
        for(int i = 0; i < N; i ++){
            id.add(i);
        }
    }

    @Override
    public void union(int p, int q) {
        int pid = id.get(p);
        int qid = id.get(q);

        for (int i = 0; i < id.size(); i++){
            if (id.get(i) == pid){
                id.set(i, qid);
            }
        }
        count--;
        System.out.println(id);
    }

    @Override
    public int find(int p) {
        validate(p);
        return id.get(p);
    }

    @Override
    public boolean connected(int p, int q) {
        return find(p) == find(q);
    } 

    @Override
    public int count() {
        return count;
    }

    private void validate(int p) {
        int n = id.size();
        if (p < 0 || p >= n) {
            throw new IllegalArgumentException("index " + p + " is not between 0 and " + (n-1));  
        }
    }

    public void print(){
        System.out.println(id);
    }
    
}
