class Solution {
    public boolean isPalindrome(ListNode head) {
        ArrayList<Integer> list1=new ArrayList<>();
        ArrayList<Integer> list2=new ArrayList<>();
        ListNode current=head;
        while(current!=null){
            list1.add(current.val);
            current=current.next;
        }
        current=head;
        ListNode prev=null;
        while(current!=null){
            ListNode temp=current.next;
            current.next=prev;
            prev=current;
            current=temp;
        }
        head=prev;
        current=prev;
        while(current!=null){
            list2.add(current.val);
            current=current.next;
        }
        System.out.println(list1);
        System.out.println(list2);
        for (int i=0;i<list1.size();i++){
            if (list1.get(i)!=list2.get(i)){
                return false;

            }
        }
        return true;

        
    }
}
