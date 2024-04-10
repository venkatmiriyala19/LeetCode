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
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        if (list1!=null && list2!=null){
        ListNode curr1=list1;
        ListNode curr2=list2;
        ArrayList<Integer> list=new ArrayList<>();
        while(curr1.next!=null){
            list.add(curr1.val);
            curr1=curr1.next;
        }
        list.add(curr1.val);
        curr1.next=list2;
        while(curr2!=null){
            list.add(curr2.val);
            curr2=curr2.next;
        }
        curr1=list1;
        Collections.sort(list);
        for(Integer element:list){
            curr1.val=element;
            curr1=curr1.next;
        }
        return list1;
        }
        if (list1==null){
            return list2;
        }
        return list1;
    }
}
