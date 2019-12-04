# call-graphs
Call graphs of various C systems for research purposes

The call graphs contain various projects in the **C** language. Call graphs have been produced with [cscout](https://github.com/dspinellis/cscout). Other languages are welcome (see Contributing Section).

### Contents

Currently the project contains call graphs for the following systems

  * apr
  * apr-util
  * httpd
  * linux
  * lxc
  * nginx
  * vim
  
Each directory contains the following contents
  1. cgraph.txt: Function and macro call graph
  2. fgraph_I.txt: Include graph
  3. fgraph_C.txt: Compile time dependency graph
  4. fgraph_F_D.txt: Control dependency graph
  5. fgraph_G.txt: Data dependency graph
  6. metrics.txt: Metrics file
  
### Contributing

If you want to contribute please submit a PR. Your change should include a directory and all these call graphs if you are using C or at least one call graph if you are using another language.


