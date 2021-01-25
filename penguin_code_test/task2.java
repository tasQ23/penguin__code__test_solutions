import java.util.Scanner;

public class Janitor{


public static int efficientJanitor(int n, float weight[]){
    float sum=0;
    int count=0;
    for(int i=0;i<n;i++){
      sum=sum+weight[i];
      if(sum==3.00){
          count++;
          sum=0;
      }
      else if(sum>3.00){
          count++;
          sum=weight[i];
      }
      if(i==(n-1)){
         count++;
          }
      }

    return count;
}

     public static void main(String []args){
        Scanner scanner = new Scanner(System.in);
        //Taking in number of bags
        int bags = scanner.nextInt();
        //System.out.println(bags);
        float[] weightArray = new float[bags];
        //Taking in weights of each bag.
        for(int i=0;i<bags;i++){
            weightArray[i]= scanner.nextFloat();
            //System.out.println(weightArray[i]);
        }
        scanner.close();
        System.out.println("The minimum number of trips the janitor makes:");
        System.out.println(efficientJanitor(bags, weightArray));
     }
}
