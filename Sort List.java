class Solution {
    public ListNode sortList(ListNode head) {
     ListNode current=head;
     ArrayList<Integer> list=new ArrayList<>();
     while(current!=null){
        list.add(current.val);
        current=current.next;
     }
     Collections.sort(list);
     current=head;
     for(Integer element:list){
        current.val=element;
        current=current.next;
     }
     return head;
    }
}
