Screpr move files. To find out what file need to be moved, Screpr parse config json with user defined regex.

There are two use cases:
  1. As a side module to use in the bigger program
  2. As a command line tool

1. The user needs to pass arguments to a screpr function of base_screpr module like base_screpr.screpr(work_dir, cfg_path, \*args, \*\*kwargs)
  work_dir - path to folder, which contains files to be sorted
  cfg_path - path to json config file, to let screpr know where you want to see your files at the end
  kwargs - user can path arguments as 'mode' (move or safe) and 'log' (true or false)
 
 2. Run base_screpr in a command line with arguments.
 Required: working folder, json config file location
 Additional: -l for log, -s for safe mode, -h to read help
 
