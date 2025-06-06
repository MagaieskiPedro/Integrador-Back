import io
import csv
import openpyxl
from rest_framework import renderers

SENSOR_DATA_FILE_HEADERS = ["id","sensor","mac_address","unidade_med","latitude","longitude","status"]


class ExcelSensorDataRenderer(renderers.BaseRenderer):

    media_type = "application/vnd.ms-excel"
    format = "xlsx"

    def render(self, data, accepted_media_type=None, renderer_context=None):    

        workbook = openpyxl.Workbook()
        buffer = io.BytesIO()
        worksheet = workbook.active
        worksheet.append(SENSOR_DATA_FILE_HEADERS)

        for student_data in data:
            worksheet.append(list(student_data.values()))

        workbook.save(buffer)

        return buffer.getvalue()
    
class CSVSensorDataRenderer(renderers.BaseRenderer):

    media_type= "text/csv"
    format= "csv"

    def render(self, data, accepted_media_type=None, renderer_context=None):
        csv_buffer = io.StringIO()
        csv_writer = csv.DictWriter(csv_buffer,fieldnames=SENSOR_DATA_FILE_HEADERS, extrasaction="ignore")
        csv_writer.writeheader()

        for sensor_data in data:
            csv_writer.writerow(sensor_data)
        
        return csv_buffer.getvalue()