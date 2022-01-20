package TreeRepresentation;

public class BinarySearchTree {

    private class Node{
        private Node left, right;
        private int value;

        public Node(int value){
            this.value = value;
            left = right = null;
        }
    }
    Node root;

    BinarySearchTree(){
        root = null;
    }

    public Node insert(Node root, int val){
        if (root == null){
            root = new Node(val);
            return root;
        } 
        if (val >= root.value){
            root.right = insert(root.right, val);
        } 
        else if (val < root.value){
            root.left = insert(root.left, val);
        }
        return root;
    }

    Node delete(Node root, int key)  { 
        if (root == null)  return root; 
   
        if (key < root.value) 
            root.left = delete(root.left, key); 
        else if (key >= root.value) 
            root.right = delete(root.right, key); 
        else  { 
            if (root.left == null) 
                return root.right; 
            else if (root.right == null) 
                return root.left; 
   
            root.value = min(root.right); 

            root.right = delete(root.right, root.value); 
        } 
        return root; 
    } 

    public int min(Node root)  { 
        int min = root.value; 
        while (root.left != null)  { 
            min = root.left.value; 
            root = root.left; 
        } 
        return min; 
    }

    public int max(Node root)  { 
        int max = root.value; 
        while (root.right != null)  { 
            max = root.right.value; 
            root = root.right; 
        } 
        return max; 
    }

    public int rank(Node root){
        return 0; //TODO
    }

    public int floor(Node root){
        return 0; //TODO
    }

    public int ceiling(Node root){
        return 0; //TODO
    }

    public void in_order_traversal(Node root){
        //TODO
    }

    public void pre_order_traversal(Node root){
        //TODO
    }

    public void post_order_traversal(Node root){
        //TODO
    }

}
