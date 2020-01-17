import subprocess

class LocalHostTarget(object):

    def _run(self, cmd):
        #print('cmd to be executed: %s' % cmd)
        #To execute multiple commands in a single string, use shell=True and never split the command string into multiple arguments
        completed_proc = subprocess.run(cmd, shell=True, timeout=300, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        return completed_proc.returncode, completed_proc.stdout
 
    def run(self, cmd):
        return self._run(cmd)

    def copy_to(self, source, destination_dir):
        mkdir_cmd = 'mkdir -p %s' % destination_dir
        self._run(mkdir_cmd)
        copy_to_cmd = 'cp -r %s %s' % (source, destination_dir)
        self._run(mkdir_cmd)
