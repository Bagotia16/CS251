package readwrite;
class node{
    int value;
    node left;
    node right;
    
    node(int value){
        this.value = value;
        left = null;
        right = null;
    }
}
public class Tree {
    node root;

    public void write(int n) {
        root = add(root, n);
    }

    public int read(int n) {
        if(root == null) return -1;
        return findNode(root, n);
    }

    private node add(node r, int n) {
        if(r == null){
            return new node(n);
        }

        if(n<r.value){
            r.left = add(r.left, n);
        }else if(n > r.value){
            r.right = add(r.right, n);
        }else{
            return r;
        }
        
        return r;
    }

    private int findNode(node r, int n){
        if(n == r.value){
            return n;
        }
        else if(r.right == null || r.left == null){
            return r.value;
        }

        return n<r.value ? findNode(r.left, n)
                         : findNode(r.right, n);
    }

    public static void main(String[] args) {
        //MAIN function
    }
}