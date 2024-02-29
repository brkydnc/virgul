from cffi import FFI

ffibuilder = FFI()

ffibuilder.cdef("""
    uint64_t f32cnt(float a, float b);
""")

ffibuilder.set_source(
    "_virgul_cffi",
"""
    #include "virgul.h"
""",
    sources=['src/ffi/virgul.c'],
    include_dirs=['src/ffi'],
    libraries=["m"],
)

if __name__ == "__main__":
    ffibuilder.compile(verbose=True)
