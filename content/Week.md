
```dataview
TABLE WITHOUT ID length(rows) AS "Notes created (last 5 days)"
FROM ""
WHERE file.cday >= date(today) - dur(5 days) AND type = "news-card"
GROUP BY true
```


C:\Users\JBritton\.opencode
C:\Users\JBritton\Threat_Estimate_2027
oc_sk_51f505181835_IDiCpTdy-R_VnOjiV5DWimmKGQ3rcPQM

```dataview
TABLE type, file.cday AS created, file.folder
FROM ""
WHERE file.cday >= date(today) - dur(5 days) AND type = "news-card"
SORT file.cday DESC, file.name ASC
```



