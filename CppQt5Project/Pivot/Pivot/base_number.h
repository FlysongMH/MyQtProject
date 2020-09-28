#ifndef STDINT_H
#define STDINT_H

/* 自定义数字类型 */

// signed
typedef signed char        INT8;
typedef short              INT16;
typedef int                INT32;
typedef long long          INT64;
// unsigned
typedef unsigned char      UINT8;
typedef unsigned short     UINT16;
typedef unsigned int       UINT32;
typedef unsigned long long UINT64;

#define INT8_MIN     (-127i8 - 1)    // minimum signed 8 bit value
#define INT8_MAX       127i8         // maximum signed 8 bit value
#define UINT8_MAX      0xffui8       // maximum unsigned 8 bit value

#define INT16_MIN    (-32767i16 - 1) // minimum signed 16 bit value
#define INT16_MAX      32767i16      // maximum signed 16 bit value
#define UINT16_MAX     0xffffui16    // maximum unsigned 16 bit value

#define INT32_MIN    (-2147483647i32 - 1) // minimum signed 32 bit value
#define INT32_MAX      2147483647i32 // maximum signed 32 bit value
#define UINT32_MAX     0xffffffffui32 // maximum unsigned 32 bit value

#define INT64_MIN        (-9223372036854775807i64 - 1)
#define INT64_MAX        9223372036854775807i64
#define UINT64_MAX       0xffffffffffffffffui64

#define SHRT_MIN    (-32768)        // minimum (signed) short value
#define SHRT_MAX      32767         // maximum (signed) short value
#define USHRT_MAX     0xffff        // maximum unsigned short value

#define INT_MIN     (-2147483647 - 1) // minimum (signed) int value
#define INT_MAX       2147483647      // maximum (signed) int value
#define UINT_MAX      0xffffffff      // maximum unsigned int value

#define LONG_MIN    (-2147483647L - 1) // minimum (signed) long value
#define LONG_MAX      2147483647L      // maximum (signed) long value
#define ULONG_MAX     0xffffffffUL     // maximum unsigned long value

#define LLONG_MIN   (-9223372036854775807i64 - 1)  // minimum signed long long int value
#define LLONG_MAX     9223372036854775807i64       // maximum signed long long int value
#define ULLONG_MAX    0xffffffffffffffffui64       // maximum unsigned long long int value



#endif // STDINT_H
