```
// Insertion Sort

FUNCTION InsertionSort(arr : ARRAY OF INTEGER) RETURNS ARRAY OF INTEGER
    DECLARE i : INTEGER
    DECLARE n : INTEGER
    DECLARE Swap : BOOLEAN
    
    FOR i ← 1 TO LENGTH(arr)-1
        n ← i
        Swap ← TRUE
        REPEAT
            
            IF n=0
            THEN
                Swap ← FALSE
            ELSE
                IF arr[n] < arr[n-1]
                THEN
                    arr[n], arr[n-1] ← arr[n-1], arr[n]
                    n ← n-1
                ELSE
                    Swap ← FALSE
                ENDIF
            ENDIF
        UNTIL Swap ← FALSE
    
    RETURN arr
```