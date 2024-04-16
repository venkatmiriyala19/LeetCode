/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode swapPairs(ListNode head) {
        if (head==null || head.next==null){
            return head;
        }
        ListNode prev=head;
        ListNode current=head.next;
        int count=0;
        while(prev!=null){
            count++;
            prev=prev.next;
        }
        prev=head;
        if (count%2==0){
        // ListNode 
        while(current.next!=null){
            int temp=prev.val;
            prev.val=current.val;
            current.val=temp;
            prev=current.next;
            current=prev.next;
        }
        int temp=prev.val;
            prev.val=current.val;
            current.val=temp;
        }
        else{
            while(prev.next!=null){
            int temp=prev.val;
            prev.val=current.val;
            current.val=temp;
            prev=current.next;
            current=prev.next;
        }
        }
        return head;
        
    }
}
