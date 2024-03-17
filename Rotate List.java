class Solution {
    public ListNode rotateRight(ListNode head, int k) {
        if (head == null || head.next == null || k == 0) {
            return head;
        }

        ListNode end = head;
        ListNode current = head;
        int length = 1;

        // Find the length of the linked list and the end node
        while (end.next != null) {
            end = end.next;
            length++;
        }

        // Calculate the actual rotation amount
        k = k % length;
        if (k == 0) {
            return head; // No need to rotate
        }

        // Move the current pointer to the (n - k)th node
        for (int i = 0; i < length - k - 1; i++) {
            current = current.next;
        }

        // Adjust the pointers to perform rotation
        end.next = head; // Connect the end to the head to form a loop
        head = current.next; // Update the head to the (n - k)th node
        current.next = null; // Set the next of the new end to null

        return head;
    }
}
