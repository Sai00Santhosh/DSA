package UnionFind;

import java.util.ArrayList;

public class LazyUF implements UnionFind { // Also known as QuickUnionUF

    private ArrayList<Integer> id = new ArrayList<Integer>();
    private int count;

    public LazyUF(int N){
        count = N;
        for(int i = 0; i < N; i ++){
            id.add(i);
        }
    }

    @Override
    public void union(int p, int q) {
        int i = find(p);
        int j = find(q);
        id.set(i, j);
        count--;
    }

    @Override
    public int find(int i) {
        validate(i);
        while(i != id.get(i)){
            i = id.get(i);
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
        int n = id.size();
        if (p < 0 || p >= n) {
            throw new IllegalArgumentException("index " + p + " is not between 0 and " + (n-1));  
        }
    }

    public static void main(String[] args) {
        EagerUF UF = new EagerUF(10);
        UF.print();
        UF.union(1, 9);
    }
    
}
