/*
* Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well
*/


/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

func deleteDuplicates(head *ListNode) *ListNode {
    if head == nil {
        return nil
    }

    cur := head
    for cur.Next != nil {
        if cur.Val == cur.Next.Val {
            cur.Next = cur.Next.Next
            continue
        }
        cur = cur.Next
    }

    return head
}