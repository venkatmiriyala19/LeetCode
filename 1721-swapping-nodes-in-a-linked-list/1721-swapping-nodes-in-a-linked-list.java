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
    public ListNode swapNodes(ListNode head, int k) {
        ListNode current=head;
        int count=0;
        while(current!=null){
            current=current.next;
            count++;
        }
        current=head;
        ListNode last=head;
        for(int i=1;i<k;i++){
            current=current.next;
        }
        for(int i=0;i<count-k;i++){
            last=last.next;
        }
        int temp=current.val;
        current.val=last.val;
        last.val=temp;
        return head;
        
    }
}