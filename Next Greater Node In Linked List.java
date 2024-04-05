class Solution {
    public int[] nextLargerNodes(ListNode head) {
        ArrayList<Integer> list=new ArrayList<>();
        ListNode current=head;
        ListNode inner=current;
        while(current.next!=null){
            inner=current;
            while(inner!=null){
                if (inner.val>current.val){
                    list.add(inner.val);
                    // current=current.next;
                    break;
                }
                inner=inner.next;
            }
            if (inner==null){
                list.add(0);
            }
            current=current.next;
        }
        list.add(0);
        int[] intArray = new int[list.size()];
        for (int i = 0; i < list.size(); i++) {
            intArray[i] = list.get(i);
        }
        return intArray;
    }
}
