package readwrite;

import java.util.concurrent.locks.Condition;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

public class ProtectedTree {
    private Tree tree = new Tree();
    private int countReads;
    private int countWrites;
    final Lock lock = new ReentrantLock();
    final Condition notFull = lock.newCondition();

    public ProtectedTree(Tree tree) {
        this.tree = tree;
        this.countWrites=0;
        this.countReads=0;
    }

    public void write(int value){
        lock.lock();
        //sync logic
//        System.out.println("Writing" + value);
        System.out.println("WE");
        this.tree.write(value);

        System.out.println("WX");
        countWrites++;
        notFull.signal();

        lock.unlock();

        //sync logic
    }

    public int read(int value) throws InterruptedException {
        //sync logic
        lock.lock();
        // int l=0;

        while(countWrites <= countReads)
        {
            notFull.await();
        }
        int answer = this.tree.read(value);
//        System.out.println("Read"+ answer);
//        System.out.println("Reading "+value);
        if (answer == value)
        {
            System.out.println("RS");
            countReads++;
        }

        else
            System.out.println("RF");
        //sync logic
        lock.unlock();
        return answer;
    }

}
