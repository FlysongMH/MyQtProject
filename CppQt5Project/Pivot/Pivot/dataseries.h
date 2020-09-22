#ifndef SERIES_H
#define SERIES_H
#include <typeinfo>
#include "base_define.h"
#include "base_number.h"

//数据序列类, 支持不同的数据类型T
class Series
{
public:
    Series();
    Series(DataType dtype, UINT32 length);
    Series(DataType dtype, UINT32 length, QString head);
    ~Series();
    
    //数据修改追加，暂不支持删除
    void set_head(QString head){m_head = head;}
    template<typename T > void modify(UINT32 index, T value);
    template<typename T > void pushback(T value);
    
private:
    DataType    m_dtype;
    UINT32      m_length;
    QString     m_head;
    vector<UINT32>   m_data_int32;
    vector<double>   m_data_double;
    vector<string>   m_data_string;
    
};

#endif // SERIES_H


