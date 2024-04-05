class Solution {
    public ListNode oddEvenList(ListNode head) {
        ArrayList<Integer> odd=new ArrayList<>();
        ArrayList<Integer> even=new ArrayList<>();
        ListNode current=head;
        int a=1;
        while(current!=null){
            if (a%2!=0){
            odd.add(current.val);}
            else{
                even.add(current.val);
            }
            a++;
            current=current.next;
        }
        current=head;
        for (Integer element:odd){
            current.val=element;
            current=current.next;
        }
        for (Integer element:even){
            current.val=element;
            current=current.next;
        }
        return head;

        
    }
}
