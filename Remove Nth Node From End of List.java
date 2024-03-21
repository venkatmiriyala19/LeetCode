class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
       
        if (head.next==null){
            return null;
        }
        // else if()
        ListNode current=head;
        int count=0;
        while(current!=null){
            current=current.next;
            count++;
        }
        if (count==n){
            return head.next;
        }
        count=count-n;
        current=head;
        while(count>1){
            count--;
            current=current.next;
        }
        if(current.next.next!=null)
        {current.next=current.next.next;}
        else{
            current.next=null;
        }
        return head;
    }
}
