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
    public ListNode mergeKLists(ListNode[] lists) {
        ArrayList<Integer> list=new ArrayList<>();
        for(ListNode ele:lists){
            ListNode current=ele;
            while(current!=null){
                list.add(current.val);
                current=current.next;
            }
        }
        Collections.sort(list);
        ListNode head=new ListNode(10);
        ListNode current=head;
        for (Integer elem:list){
            // System.out.println(elem);
            ListNode newNode=new ListNode(elem);
            current.next=newNode;
            current=current.next;
        }
        return head.next;
        
    }
}
