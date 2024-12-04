from rest_framework_xml.renderers import XMLRenderer

class CustomXMLRenderer(XMLRenderer):
    root_tag_name = 'Data'

    def _to_xml(self, xml, data):
        if isinstance(data, (list, tuple)):
            for item in data:
                xml.startElement("RestingECG", {})
                self._to_xml(xml, item)
                xml.endElement("RestingECG")
        elif isinstance(data, dict):
            for key, value in data.items():
                if key == "TestDemographics":
                    xml.startElement("TestDemographics", {})
                    if isinstance(value, list):
                        for demo in value:
                            self._to_xml(xml, demo)
                    xml.endElement("TestDemographics")
                elif key == "ECGMeasurements":
                    xml.startElement("ECGMeasurements", {})
                    if isinstance(value, list):
                        for measurement in value:
                            self._to_xml(xml, measurement)
                    xml.endElement("ECGMeasurements")
                else:
                    xml.startElement(key, {})
                    self._to_xml(xml, value)
                    xml.endElement(key)
        elif data is None:
            pass
        else:
            xml.characters(str(data))