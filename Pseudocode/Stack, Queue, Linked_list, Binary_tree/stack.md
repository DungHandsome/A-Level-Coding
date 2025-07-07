# Stack Operation
- First in, Last out
- The one come first will be removed last
- Make use of Base pointer and Top pointer:
    - Base pointer point to the first item
    - Top poointer point to the last item
- Operation:
    - Push: Add to the stack
    - Pop: Remove from the stack

## Example:
- Given a stack (Array size = 6)
- I have a stack implemented as an array of size 6: stack = [4, 7, 12, 9, –, –] with:
    - basePointer = 0
    - topPointer = 3 (i.e., stack[3] = 9)
- Perform the following operations:
    - Push 15
    - Pop
    - Push 6

```
DECLARE Stack : ARRAY[0:5] OF INTEGER
DECLARE basePointer : INTEGER
DECLARE topPointer : INTEGER


basePointer ← 0
topPointer ← 3

PROCEDURE Push(BYREF Stack : ARRAY , BYREF topPointer : INTEGER , Item : INTEGER)
    IF topPointer = LENGTH(Stack)-1 // 5
        THEN
            OUTPUT "Can't push, the stack is already full"
        ELSE
            topPointer ← topPointer + 1
            Stack[topPointer] ← Item
    ENDIF

PROCEDURE Pop(BYREF Stack: ARRAY , BYREF topPointer : INTEGER , basePointer)
    IF topPointer = basePointer - 1 // Stack empty
        THEN
            OUTPUT "Can't pop, the stack is already empty"
        ELSE
            Stack[topPointer] ← -9999999 //Useless value
            topPointer ← topPointer - 1
    ENDIF

Push(Stack, topPointer, 15)
Pop(Stack, topPointer, basePointer)
Push(Stack, topPointer, 6)

OUTPUT Stack
```