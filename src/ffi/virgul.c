#include <stdint.h>
#include <math.h>

extern uint64_t f32cnt(float a, float b) {
    typedef union {
        uint32_t integer;
        float floating;
    } view;

    view start = { .floating = a };
    view end = { .floating = b };
    view pivot = { .integer = start.integer };

    uint64_t counter = 0; 

    for(; pivot.integer < end.integer; pivot.integer++)
        if (isnormal(pivot.floating)) counter++;

    return counter;
}
