# python imports
from __future__ import with_statement
import os, re

# fabric imports
from fabric.api import local, run, cd, put, env

env.host_string = "user@someserver.org"
env.password = 's3kr3tz'

def pack(target, version, revision, release_dir, tmp_dir='/tmp'):
  """
  Method to package a release for deployment
  """
  archive_name = '.'.join([target, version, revision, 'tgz'])
  full_archive_path = os.path.join(tmp_dir, archive_name)
  local('tar czf %s -C %s .' % (full_archive_path, release_dir))
  return archive_name

def upload(target, version, revision, release_dir):
  """
  Method to upload the released code to a server
  """

  # package the release for deployment
  tmp_dir = '/tmp'
  archive_name = pack(target, version, revision, release_dir, tmp_dir)

  with cd('public_html'):
    dir = run('ls')
    dir_contents = [d.strip() for d in re.split(r"\s*",dir) if d.strip()]
    if not target in dir_contents:
      run('mkdir %s' % target)

    with cd(target):
      dir = run('ls')
      dir_contents = [d.strip() for d in re.split(r"\s*",dir) if d.strip()]

      if not version in dir_contents:
        run('mkdir %s' % version)

      with cd(version):
        run('rm -rf *')
        put(os.path.join(tmp_dir, archive_name), '.')
        run('tar xzf %s' % archive_name)
        run('rm -f %s' % archive_name)
        run('mv fcgi.htaccess .htaccess')
        run('chmod 755 index.fcgi')

      run('rm -f current')
      run('ln -s %s current' % version)
