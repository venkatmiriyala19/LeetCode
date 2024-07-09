class Solution {
    public double averageWaitingTime(int[][] customers) {
        
        int run=customers[0][0]+customers[0][1];
        double waitTime=run-customers[0][0];
        for(int i=1;i<customers.length;i++){
            run=Math.max(run+customers[i][1],customers[i][0]+customers[i][1]);
            waitTime=waitTime+(run-customers[i][0]);
            // System.out.println(waitTime);
        }
        
        return (waitTime/customers.length);

        
    }
}