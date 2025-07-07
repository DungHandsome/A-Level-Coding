# Queue
- First in First out
- First item come in will be removed first

## Example:
Given queue of [63, 51, 66, 47, 10, 22] with:
- frontPointer = 4 (i.e., queue[4] = 10)
- backPointer = 0 (i.e., queue[0] = 63)
- perform the following operations:
    - Dequeue
    - Enqueue 51
    - Enqueue 66

My Complex Version:

```
DECLARE Queue : ARRAY[0:5] OF INTEGER
DECLARE frontPointer : INTEGER
DECLARE backPointer : INTEGER
// Let -999999 be None

frontPointer ← 0
backPointer ← 4

PROCEDURE Enqueue(BYREF Queue : ARRAY, BYREF backPointer : INTEGER, frontPointer, Item : INTEGER)
    IF backPointer = frontPointer - 1 OR backPointer = frontPointer + LENGTH(Queue) - 1
        THEN
            OUTPUT "The queue is full"
        ELSE
            IF backPointer = LENGTH(Queue) - 1
                THEN
                    backPointer ← 0
                ELSE
                    backPointer ← backPointer + 1
            ENDIF
            Queue[backPointer] ← Item
    ENDIF

PROCEDURE Dequeue(BYREF Queue : ARRAY, BYREF frontPointer : INTEGER, backPointer)
    IF Queue[frontPointer] = -999999
        THEN
            OUTPUT "The queue is empty"
        ELSE
            Queue[frontPointer] ← -999999
            IF frontPointer = LENGTH(Queue) - 1
                THEN
                    frontPointer ← 0
                ELSE
                    frontPointer ← frontPointer + 1
            ENDIF
    ENDIF

Dequeue(Queue, frontPointer, backPointer)
Enqueue(Queue, backPointer, frontPointer, 51)
Enqueue(Queue, backPointer, frontPointer, 66)
```