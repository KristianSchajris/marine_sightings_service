import dicttoxml
from fastapi.responses import Response

class XMLAdapter:
    def __init__(self, data: dict):
        self.data = data

    def to_xml(self) -> str:
        xml = dicttoxml.dicttoxml(self.data, custom_root='response', attr_type=False)
        return xml.decode()

    def get_response(self) -> Response:
        xml_data = self.to_xml()
        return Response(content=xml_data, media_type="application/xml")