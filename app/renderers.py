import io
import csv
import openpyxl
from rest_framework import renderers

SENSOR_DATA_FILE_HEADERS = ["id","sensor","mac_address","unidade_med","latitude","longitude","status"]
AMBIENTE_DATA_FILE_HEADERS = ["sig","descricao","ni","responsavel"]
HISTORICO_DATA_FILE_HEADERS = ["valor","timestamp","sensor","ambiente"]

# Cria arquivo excel listando dados do SENSOR a partir de tabela com cabeçalho definido em SENSOR_DATA_FILE_HEADERS
class ExcelSensorDataRenderer(renderers.BaseRenderer):

    media_type = "application/vnd.ms-excel"
    format = "xlsx"

    def render(self, data, accepted_media_type=None, renderer_context=None):    

        workbook = openpyxl.Workbook()
        buffer = io.BytesIO()
        worksheet = workbook.active
        worksheet.append(SENSOR_DATA_FILE_HEADERS)

        for sensor_data in data:
            worksheet.append(list(sensor_data.values()))

        workbook.save(buffer)

        return buffer.getvalue()
    
# Cria arquivo excel listando dados do AMBIENTE a partir de tabela com cabeçalho definido em AMBIENTE_DATA_FILE_HEADERS
class ExcelAmbienteDataRenderer(renderers.BaseRenderer):
    media_type = "application/vnd.ms-excel"
    format = "xlsx"

    def render(self, data, accepted_media_type=None, renderer_context=None):    

        workbook = openpyxl.Workbook()
        buffer = io.BytesIO()
        worksheet = workbook.active
        worksheet.append(AMBIENTE_DATA_FILE_HEADERS)

        for ambiente_data in data:
            worksheet.append(list(ambiente_data.values()))

        workbook.save(buffer)

        return buffer.getvalue()

# Cria arquivo excel listando dados do HISTORICO a partir de tabela com cabeçalho definido em HISTORICO_DATA_FILE_HEADERS    
class ExcelHistoricoDataRenderer(renderers.BaseRenderer):
    media_type = "application/vnd.ms-excel"
    format = "xlsx"

    def render(self, data, accepted_media_type=None, renderer_context=None):    

        workbook = openpyxl.Workbook()
        buffer = io.BytesIO()
        worksheet = workbook.active
        worksheet.append(HISTORICO_DATA_FILE_HEADERS)

        for historico_data in data:
            worksheet.append(list(historico_data.values()))

        workbook.save(buffer)

        return buffer.getvalue()

# Cria um arquivo CSV a partir dos dados de sensor com o cabeçalho definido em SENSOR_DATA_FILE_HEADERS
# class CSVSensorDataRenderer(renderers.BaseRenderer):

#     media_type= "text/csv"
#     format= "csv"

#     def render(self, data, accepted_media_type=None, renderer_context=None):
#         csv_buffer = io.StringIO()
#         csv_writer = csv.DictWriter(csv_buffer,fieldnames=SENSOR_DATA_FILE_HEADERS, extrasaction="ignore")
#         csv_writer.writeheader()

#         for sensor_data in data:
#             csv_writer.writerow(sensor_data)
        
#         return csv_buffer.getvalue()