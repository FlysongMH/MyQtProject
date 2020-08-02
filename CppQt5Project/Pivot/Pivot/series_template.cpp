#include "series.h"

template<typename T >Series<T>::Series():
    m_length(0),
    m_head("head"),
    m_data({})
{
    setDType();
}

template<typename T >Series<T>::Series(UINT32 length):
    m_length(length),
    m_head("head"),
    m_data({})
{
    setDType();
}

template<typename T >Series<T>::Series(UINT32 length, QString head):
    m_length(length),
    m_head(head),
    m_data({})
{
    setDType();
}
template<typename T >Series<T>::~Series()
{
    m_data.clear();
}

template<typename T > void Series<T>::set_datatype()
{
    if(typeid (T)==typeid (double))
        m_dtype  = DT_DOUBLE;
    else if(typeid (T)==typeid (int))
        m_dtype  = DT_INT;
    else
        m_dtype  = DT_STRING;
}

template<typename T > void Series<T>::modify(UINT32 index, T value)
{
    if(m_length>0 && index<m_length)
        m_data[index] = value;
}
template<typename T > void Series<T>::pushback(T value)
{
    m_data.push_back(value);
    m_length++;
}
