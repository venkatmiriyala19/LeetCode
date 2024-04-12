class Solution {
    public ListNode deleteMiddle(ListNode head) {
        if (head==null || head.next==null){
            return null;
        }
        else if(head.next.next==null){
            head.next=null;
            return head;
        }
        ListNode slow=head;
        ListNode fast=head;
        while(fast!=null && fast.next!=null){
            slow=slow.next;
            fast=fast.next.next;
        }
        slow.val=slow.next.val;
        slow.next=slow.next.next;
        return head;
        
    }
}
