class Solution {
    private int Leftsum(TreeNode root,int direction){
        if (root==null)return 0;
        int sum=0;
        if (root.left==null && root.right==null && direction==-1)return root.val;
        sum+=Leftsum(root.left,-1);
        sum+=Leftsum(root.right,1);
        return sum;
    }
    public int sumOfLeftLeaves(TreeNode root) {
        return Leftsum(root,0);
    }
}
