from lxml.etree import Element
from typing import Iterable

from nexpose.models.site import Site
from nexpose.models.scan import Scan as ScanModel
from nexpose.models.scan import Template
from nexpose.modules import ModuleBase


class Scan(ModuleBase):
    def templates(self) -> Iterable[Template]:
        # TODO waiting on API 2 to be released
        return {
            Template(template_id='aggressive-discovery'),
            Template(template_id='discovery'),
            Template(template_id='dos-audit'),
            Template(template_id='exhaustive-audit'),
            Template(template_id='full-audit'),
            Template(template_id='full-audit-enhanced-logging-without-web-spider'),
            Template(template_id='full-audit-without-web-spider'),
            Template(template_id='hipaa-audit'),
            Template(template_id='internet-audit'),
            Template(template_id='linux-rpm'),
            Template(template_id='microsoft-hotfix'),
            Template(template_id='network-audit'),
            Template(template_id='pci-audit'),
            Template(template_id='pci-internal-audit'),
            Template(template_id='pentest-audit'),
            Template(template_id='sox-audit'),
            Template(template_id='web-audit'),
        }

    def site_scan(self, site: Site) -> ScanModel:
        request = Element('SiteScanRequest', attrib={
            'site-id': str(site.id),
        })

        ans = self._post(xml=request)

        return ScanModel(scan_id=int(ans.attrib['scan-id']))
