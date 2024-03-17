class Solution {
    public ListNode mergeNodes(ListNode head) {
        ListNode dummy=new ListNode(-1);
        dummy.next=head;
        ListNode prev=dummy;
        ListNode current=head.next;
        int a=0;
        while(current!=null){
            // System.out.println(current.val);
            if (current.val!=0){
                a+=current.val;
                current=current.next;
                continue;
            }
            else{
                System.out.println(a);
                ListNode temp=new ListNode(a);
                prev.next=temp;
                prev=temp;
                a=0;
            }
            current=current.next;
        }
        return dummy.next;
        
    }
}
