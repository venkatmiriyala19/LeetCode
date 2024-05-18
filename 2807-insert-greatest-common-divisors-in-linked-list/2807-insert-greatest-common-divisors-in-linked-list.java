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
    public ListNode insertGreatestCommonDivisors(ListNode head) {
        if(head==null || head.next==null){
            return head;
        }
        ListNode current=head.next;
        ListNode prev=head;
        while(current!=null){
            int a=GCD(prev.val,current.val);
            ListNode temp=new ListNode(a);
            prev.next=temp;
            temp.next=current;
            prev=current;
            current=current.next;
        }
        return head;
        
    }
    public int GCD(int i,int j){
        // HashSet<Integer> set=new HashSet<>();
        // HashSet<Integer> set2=new HashSet<>();

        // for(int a=1;a<=i;a++){
        //     if(i%a==0){
        //         set.add(a);
        //     }
        // }
        // for(int a=1;a<=j;a++){
        //     if(j%a==0){
        //         set2.add(a);
        //     }
        // }
        // int max=0;
        // for(Integer ele:set){
        //     if(set2.contains(ele)){
        //         if (ele>max){
        //             max=ele;
        //         }
        //     }
        // }
        // return max;
        while(j!=0){
            int temp=j;
            j=i%j;
            i=temp;
        }
        return i;

    }
}