```
// Linear Search

PROCEDURE LinearSearch(arr : ARRAY OF INTEGER)
    DECLARE item : INTEGER
    DECLARE Upperbound : INTEGER
    DECLARE Lowerbound : INTEGER
    DECLARE Found : BOOLEAN

    INPUT item
    Found ← FALSE
    Lowerbound ← 0
    Upperbound ← LENGTH(arr) - 1
    REPEAT
        IF arr[Lowerbound] = item
            THEN
                Found ← TRUE
            ELSE
                Lowerbound ← Lowerbound+1
        ENDIF
    UNTIL (Found = TRUE) OR (Lowerbound > Upperbound)

    IF Found
        THEN
            OUTPUT "Item found in position "
            //Add this line if u want:
            OUTPUT Lowerbound
        ELSE
            OUTPUT "Item not found"
    ENDIF
ENDPROCEDURE

//DECLARE mrarr : ARRAY[0:7] OF INTEGER
//mrarr ← [1,123,45,12,5,6,7,23]
//
//CALL LinearSearch(mrarr)
```