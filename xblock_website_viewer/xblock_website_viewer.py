"""Jupyter Notebook Viewer XBlock"""

import logging
import pkg_resources
from urllib import urlencode

from django.core.urlresolvers import reverse

from xblock.core import XBlock
from xblock.fields import Scope, String, Integer
from xblock.fragment import Fragment
from xblockutils.studio_editable import StudioEditableXBlockMixin

log = logging.getLogger(__name__)


class WebsiteViewerXBlock(XBlock, StudioEditableXBlockMixin):
    """iframe used with endpoint to render proctortrack website"""

    display_name = String(
        display_name="Display Name", default="WebViewer",
        scope=Scope.settings,
        help="Name of this XBlock" 
    )

    url = String(
        help="URL to the site",
        scope=Scope.content,
        display_name="URL",
        default="https://www.proctortrack.com"
    )

    xblock_height = Integer(
        help="Height of this XBlock (px)",
        scope=Scope.content,
        display_name="Height",
        default=600
    )

    xblock_width = Integer(
        help="Width of this XBlock (px)",
        scope=Scope.content,
        display_name="Width",
        default=1000                                                                                                                                                                                                    )

    editable_fields = ('display_name', 'url', 'xblock_height', 'xblock_width')

    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    def student_view(self, context=None):
        full_url = self.url
        log.debug("Full URL: {}".format(full_url))
        base_html = self.resource_string('static/html/student_view.html')\
            .format(self.xblock_height, self.xblock_width ,full_url)
        
        frag = Fragment(base_html)
        return frag


