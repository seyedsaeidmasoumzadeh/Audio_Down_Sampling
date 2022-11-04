from io import StringIO

old_open = open
in_memory_files = {}

def open(name, mode="r", *args, **kwargs):
     if name[:1] == ":" and name[-1:] == ":":
          # in-memory file
          if "w" in mode:
               in_memory_files[name] = ""
          f = StringIO(in_memory_files[name])
          oldclose = f.close
          def newclose():
              in_memory_files[name] = f.getvalue()
              oldclose()
          f.close = newclose
          return f
     else:
          return old_open(name, mode, *args, **kwargs)