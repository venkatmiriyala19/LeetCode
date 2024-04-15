/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    int sum=0;
    int totalSum=0;
    public void leafSum(TreeNode root,int sum){
        if (root==null)return ;
        sum=sum*10+root.val;
        if (root.left==null && root.right==null){
            totalSum+=sum;
            return ;
        }
        leafSum(root.left,sum);
        leafSum(root.right,sum);
    }
    public int sumNumbers(TreeNode root) {
        leafSum(root,sum);
        return totalSum;
    }
}
