Import("env")

env.AddCustomTarget(
    name="nanopb",
    dependencies=None,

    
    actions=[
       " (cd protobuf; "
       "python ../lib/nanopb/generator/nanopb_generator.py  "
       "--strip-path --output-dir=../src update.proto)"
    ],
    title="Nanopb generate step",
    description="Rebuild .c/.h files from .proto"
    #always_build=True
)