package UnionFind;

import java.util.ArrayList;

public class WeightedUF_PC implements UnionFind {

    private ArrayList<Integer> parent  = new ArrayList<Integer>();
    private ArrayList<Integer> size  = new ArrayList<Integer>();
    private int count;

    public WeightedUF_PC(int N){
        count = N;
        for(int i = 0; i < N; i ++){
            parent.add(i);
            size.set(i, 1);
        }
    }

    @Override
    public void union(int p, int q) {
        int rootP = find(p);
        int rootQ = find(q);
        if (rootP == rootQ) return;

        if (size.get(rootP) < size.get(rootQ)) {
            parent.set(rootP, rootQ);
            int val = size.get(rootQ) + size.get(rootP);
            size.set(rootQ, val);
        }
        else {
            parent.set(rootQ, rootP);
            int val = size.get(rootP) + size.get(rootQ);
            size.set(rootP, val);
        }
        count--;
    }

    @Override
    public int find(int i) {
        validate(i);
        while(i != parent.get(i)){
            parent.set(i, parent.get(parent.get(i)));
            i = parent.get(i);
        }
        return i;
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
        int n = parent.size();
        if (p < 0 || p >= n) {
            throw new IllegalArgumentException("index " + p + " is not between 0 and " + (n-1));  
        }
    }
    
}
