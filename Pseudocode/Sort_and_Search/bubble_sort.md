```
// Bubble Sort

FUNCTION BubbleSort(BYREF arr : ARRAY OF INTEGER) RETURNS ARRAY OF INTEGER
    DECLARE i : INTEGER
    DECLARE n : INTEGER
    i ← 0

    FOR i ← 0 TO LENGTH(arr)-1
        n ← 0
        FOR n ← 0 TO LENGTH(arr)-2-i
            IF arr[n]>arr[n+1]
            THEN
                arr[n],arr[n+1] ← arr[n+1],arr[n]
            ENDIF
        NEXT n
    NEXT i
    RETURN arr

ENDFUNCTION
```