#include <QDebug>
#include "dataseries.h"

Series::Series():
    m_dtype(DT_STRING),
    m_length(0),
    m_head("head"),
    m_data_int32({}),
    m_data_double({}),
    m_data_string({})
{
}
Series::Series(DataType dtype, UINT32 length):
    m_dtype(dtype),
    m_length(length),
    m_head("head"),
    m_data_int32({}),
    m_data_double({}),
    m_data_string({})
{
}
Series::Series(DataType dtype, UINT32 length, QString head):
    m_dtype(dtype),
    m_length(length),
    m_head(head),
    m_data_int32({}),
    m_data_double({}),
    m_data_string({})
{
}
Series::~Series()
{
    m_data_int32.clear();
    m_data_double.clear();
    m_data_string.clear();
}


template<typename T > 
void Series::modify(UINT32 index, T value)
{
    if(m_length<=0 || index>=m_length)
    {
        qDebug()<<"Error!,data length is "<<m_length<<" ,but index is "<<index;
        return;
    }
    if(m_dtype==DT_INT)
        m_data_int32[index] = value;
    else if(m_dtype==DT_DOUBLE)
        m_data_double[index] = value;
    else
        m_data_string[index] = value;
}
template<typename T > 
void Series::pushback(T value)
{
    if(m_dtype==DT_INT)
        m_data_int32.push_back(value);
    else if(m_dtype==DT_DOUBLE)
        m_data_double.push_back(value);
    else
        m_data_string.push_back(value);
    m_length++;
}
