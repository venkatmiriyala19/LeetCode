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
    public boolean evaluateTree(TreeNode root) {
        int val=root.val;
        if (val==3){
            return evaluateTree(root.left) && evaluateTree(root.right);
        }
        else if(val==2){
            return evaluateTree(root.left) || evaluateTree(root.right);
        }
        else if(val==1)
            return true;
        else
            return false;
    }
}