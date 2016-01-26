import json
from bindings import pyangbind_example
from pyangbind.lib.serialise import pybindJSONEncoder

"""
pyang --plugindir /usr/local/lib/python2.7/dist-packages/pyangbind/plugin -f pybind pyangbind-example.yang > bindings.py
python generate.py
"""
### Generate rpc_add-mapping_ipv4_elp.json

Object = pyangbind_example()
## - replaced by _

## Add mapping record
Object.input.mapping_record.authoritative = True
Object.input.mapping_record.mapVersion = 10
Object.input.mapping_record.action = "NoAction"
Object.input.mapping_record.recordTtl = 1440

## List

## Add first item ISP1 to the list
Object.input.LocatorRecord.add("ISP1")
Object.input.LocatorRecord["ISP1"].priority = 1
Object.input.LocatorRecord["ISP1"].weight = 1
Object.input.LocatorRecord["ISP1"].multicastPriority = 255
Object.input.LocatorRecord["ISP1"].multicastWeight = 0
Object.input.LocatorRecord["ISP1"].localLocator = True
Object.input.LocatorRecord["ISP1"].rlocProbed = False
Object.input.LocatorRecord["ISP1"].routed = False

## Add address_type to current locator record
Object.input.LocatorRecord["ISP1"].rloc.address_type = "ietf-lisp-address-types:explicit-locator-path-lcaf"

### Add hops
Object.input.LocatorRecord["ISP1"].rloc.explicit_locator_path.hop.add("Hop 1")
Object.input.LocatorRecord["ISP1"].rloc.explicit_locator_path.hop["Hop 1"].address = "20.20.20.20"
Object.input.LocatorRecord["ISP1"].rloc.explicit_locator_path.hop["Hop 1"].lrs_bits = "lookup rloc-prob strict"


Object.input.LocatorRecord["ISP1"].rloc.explicit_locator_path.hop.add("Hop 2")
Object.input.LocatorRecord["ISP1"].rloc.explicit_locator_path.hop["Hop 2"].address = "30.30.30.30"
Object.input.LocatorRecord["ISP1"].rloc.explicit_locator_path.hop["Hop 2"].lrs_bits = "lookup strict"
print json.dumps(Object.get(filter=True), \
		        cls=pybindJSONEncoder, indent=4)
