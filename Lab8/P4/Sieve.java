import java.util.Arrays;
import java.util.Scanner;
import java.util.function.IntPredicate;
import java.util.stream.IntStream;

public class Sieve{

    private static void sieve(int n){
        boolean prime[]= new boolean[n+1];
        Arrays.fill(prime,true);

        prime[0]=false;
        prime[1]=false;

        if(n==1)return;

        IntStream m = IntStream.range(2,n+1);

        StringBuilder result=new StringBuilder("");

        IntPredicate filtering = t ->
        {
            if(prime[t])
            {
                result.append(t+" ");
                if(t*t<=n)
                {
                    prime[t*t]=false;
                    IntStream.range(t, (n / t) + 1).map(p -> t * p).reduce((a, b) -> {prime[b]=false;return b;});
                }
                return true;
            }
            return false;
        };
        int s[]= m.filter(filtering).toArray();
        System.out.println(result);

    }

    public static void main(String[] args){

        Scanner myObj = new Scanner(System.in);
        Integer n = myObj.nextInt();

        sieve(n);
    }
}