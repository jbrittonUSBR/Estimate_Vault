import re
files=[l.strip() for l in open('outputs/nov_batch_01.txt') if l.strip()]
locmap={"287":"Sanaa, Yemen","288":"Saudi Arabia","289":"Beirut, Lebanon","290":"Zaporizhzhia, Ukraine","291":"Russia/Ukraine","292":"Zaporizhzhia, Ukraine","293":"Colombia","294":"NATO Eastern Flank","295":"Russia","296":"Ukraine/Russia","297":"Kyiv, Ukraine","298":"Riyadh, Saudi Arabia","299":"Kirishi, Russia","300":"Khor Mor, Iraq","301":"Iraqi Kurdistan","302":"Saudi Arabia","303":"Saudi Arabia","304":"Khor Mor, Iraq","305":"N/A","306":"Russia","307":"Romania","308":"Saudi Arabia","309":"Baltic, Russia","310":"Brazil","311":"Sudan","312":"Yemen","313":"Bahrain","314":"United States","315":"Afghanistan","316":"Middle East"}
done=0
for f in files:
    m=re.search(r'UAS-2026-(\d+)',f)
    cid=m.group(1)
    txt=open(f,encoding='utf-8').read()
    if '(U)' in txt.split('[Source]')[-1].split('**Query:**')[0]:
        continue
    tm=re.search(r'^title:\s*"(.*)"',txt,re.M)
    title=tm.group(1) if tm else ''
    urlm=re.search(r'\[Source\]\(([^)]+)\)',txt)
    url=urlm.group(1)
    loc=locmap.get(cid,'Unknown')
    newblock=f"[Source]({url})\n\n(U) {loc} — {title}.\n\n**Query:**"
    oldblock=f"[Source]({url})\n\n**Query:**"
    assert oldblock in txt, f
    txt=txt.replace(oldblock,newblock,1)
    open(f,'w',encoding='utf-8').write(txt)
    done+=1
print("done",done)
