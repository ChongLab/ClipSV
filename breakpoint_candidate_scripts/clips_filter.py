#!/usr/bin/env python	
import sys,re
	
def clips_filter(chromosome,minimap2_sv,coverage):
	out_SV=open(minimap2_sv.split('.')[0]+'.filter.SV','w')	
	out_INDEL=open(minimap2_sv.split('.')[0]+'.filter.INDEL','w')
	info={}
	with open(minimap2_sv) as f:
		while True:
			l=f.readline().rstrip()
			if not l: break
			line=l.split('\t')
			if line[0]!=chromosome:
				continue
			name='\t'.join(line[0:5])
			if name in info:
				info[name][5]+=1
			else:
				info[name]=line[0:5]+[1]
	total=[]
	for i in info:
		if info[i][5]>=coverage:
			total.append(info[i])
	total_sorted=sorted(total,key=lambda x: (x[0], int(x[1]),int(x[2])))
	for x in range(len(total_sorted)):
		if int(total_sorted[x][4])<50:
			out_INDEL.write(('\t'.join(str(n) for n in total_sorted[x][0:5]))+'\n')
		else:
			out_SV.write(('\t'.join(str(n) for n in total_sorted[x][0:5]))+'\n')
	
