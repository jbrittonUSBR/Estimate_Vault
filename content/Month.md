```dataview
TABLE type, file.cday AS created, file.folder
FROM ""
WHERE file.cday.month = 11 
  AND file.cday.year = 2026 
  AND type = "news-card"
SORT file.cday DESC, file.name ASC
```



