class Solution {
    public ListNode mergeInBetween(ListNode list1, int a, int b, ListNode list2) {
        ListNode current1=list1;
        ListNode prev1=list1;
        ListNode current2=list2;
        
        while(current2.next!=null){
            current2=current2.next;
        }
        while(a>1){
            prev1=prev1.next;
            a--;
        }
        while(b>=0){
            current1=current1.next;
            b--;
        }
        prev1.next=list2;
        current2.next=current1;
        return list1;
    }

}
