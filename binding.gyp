{
    "targets": [{
        "target_name": "native",
        "sources": [ "src/native.cpp", "src/set.cpp", "src/iterator.cpp" ],
        "include_dirs" : [ "<!(node -e \"require('nan')\")" ],
        "conditions": [
            ['OS=="linux"', {
                "cflags": [ "-std=c++11", "-Wall" ]
            }, {
                "cflags": [ "-std=c++11", "-stdlib=libc++", "-Wall" ]
            }]
        ]
    }]
}
