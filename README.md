# ODL\_TEST
Test repository for opendaylight project:

1. generate.py :- Example code to generate JSON type file like  rpc\_add-mapping\_ipv4\_elp.json (Link below). It uses the hierarchy of python classes generated by the Pyangbind plugin for the YANG modules.
(Link: https://git.opendaylight.org/gerrit/gitweb?p=integration/test.git;a=blob;f=csit/variables/lispflowmapping/Be/rpc\_add-mapping\_ipv4\_elp.json )

2. pyangbind-example.yang :- YANG file containing groupings, leafs, types, containers etc. It containes all the YANG models which are required to generate the above JSON file. 

3. output.json :- Output JSON file by generate.py

Commands to generate JSON:

1. Install Pyangbind plugin from (https://github.com/robshakir/pyangbind). 
2. Get the recent version only (https://github.com/robshakir/pyangbind/issues/31).
3. get the plugindir path using below command:
```
	/usr/bin/env python -c 'import pyangbind; import os; print "%s/plugin" % os.path.dirname(pyangbind.__file__)'
```
4. Use following command to run generate.py
```
pyang --plugindir <path-to-pyangbind-plugindir> -f pybind pyangbind-example.yang -o bindings.py
```
5. Then Run, 
```
python generate.py
```
