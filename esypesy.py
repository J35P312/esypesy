import xlrd
import os

wd=os.path.dirname(os.path.realpath(__file__))

files = os.listdir(wd)

for f in files:
	if f.endswith("star.xls"):
		outfile=f.replace("_star.xls",".esy")
		o=open(outfile,"w")
		wb = xlrd.open_workbook(f)
		sheet = wb.sheet_by_index(0)
		for i in range(1,sheet.nrows):
			col="{}0{}".format(sheet.cell_value(i, 13),int(sheet.cell_value(i, 14)))
			sample=sheet.cell_value(i, 0).strip()
			if sample.startswith("PCR-"):
				sample=sample.replace("PCR-","")
			elif sample == "":
				sample="NTC"
			o.write("{}/r/{}\n".format( col,sample))
		o.write("/r/")
		o.close()
		
