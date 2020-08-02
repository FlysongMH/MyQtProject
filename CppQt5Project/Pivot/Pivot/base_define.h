#ifndef BASE_DEFINE_H
#define BASE_DEFINE_H

//std header
#include <vector>
#include <QStringList>

//self defined header
#include "base_number.h"

using namespace std;

#define NULL        0
#define NULLptr     nullptr

typedef std::vector<int >                vint;
typedef std::vector<std::vector<int > >       vvint;
typedef std::vector<double >             vdouble;
typedef std::vector<std::vector<double > >    vvdouble;


//支持存储的数据类型
enum DataType
{
    DT_DOUBLE,
    DT_INT,
    DT_STRING,
    DT_NULL,
};


#endif // BASE_DEFINE_H
