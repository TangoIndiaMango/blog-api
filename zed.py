import aspose.cells
from aspose.cells import Workbook

workbook = Workbook("Context_Dataset.xlsx")
workbook.save("context.json")