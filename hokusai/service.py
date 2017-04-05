from hokusai.config import config
from hokusai.kubectl import Kubectl

class Service(object):
  def __init__(self, context):
    self.context = context
    self.kctl = Kubectl(self.context)
    self.cache = self.kctl.get_object('service', selector="app=%s" % config.project_name)
