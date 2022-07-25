REPLACE   MACRO VIEW_CREATOR (
    indatabasename VARCHAR(30),
    intablename VARCHAR(60),
    inparamsourcedbname VARCHAR(60),
    inparamtargetdbname VARCHAR(60))
    AS ( /*
    exec XA52251.VIEW_CREATOR (  'D_DW_TABLES', 'DATOS_PERSONALES','${DW_AMBIENTE}_DW_TABLES')
    
    :intablename
    */
    SELECT    loadcommand (TITLE '')
        FROM    (
        SELECT    -2 (INT),
            'REPLACE VIEW '||:inparamtargetdbname||'.'||:intablename||Chr(13)||
            'AS LOCKING '||:inparamsourcedbname||'.'||:intablename||' FOR ACCESS'||Chr(13)||
            'SELECT'
            FROM (
            SELECT 'X' V)  B2	
        
        UNION
        SELECT    ColumnId - 1000 + 16,
            UPPER(TRIM(ColumnName))||
            CASE
                WHEN columnid LT lastcol THEN ','
            ELSE '  '
            END
            FROM dbc.COLUMNSV,
                (
            SELECT    MAX(columnid) AS lastcol
                FROM dbc.COLUMNSV
                WHERE databasename=:indatabasename
                    AND  TABLENAME=:intablename	 ) XC
            WHERE databasename=:indatabasename
                AND  TABLENAME=:intablename
        
        UNION
        SELECT    10000,
            'FROM '||:inparamsourcedbname||'.'||:intablename||';'
            FROM  (
            SELECT 'X' V)  B
        ) X (seqno,loadcommand)
        ORDER BY seqno; );