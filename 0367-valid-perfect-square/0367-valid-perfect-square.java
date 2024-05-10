class Solution {
    public boolean isPerfectSquare(int num) {
        // System.out.print();
        double number=Math.sqrt(num);
        double rounded=Math.round(number);
        // boolean res=isInteger(num);
        if (number==rounded){
        return true;}
        return false;
        
    }
}