from hokusai.lib.command import command
from hokusai.services.command_runner import CommandRunner

@command
def run(context, cmd, tty, tag, env, constraint, namespace=None):
  if tag is not None:
    image_tag = tag
  else:
    image_tag = context

  return CommandRunner(context, namespace=namespace).run(image_tag, cmd, tty=tty, env=env, constraint=constraint)
