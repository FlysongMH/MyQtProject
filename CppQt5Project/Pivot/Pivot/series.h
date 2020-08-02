#ifndef SERIES_H
#define SERIES_H
#include <typeinfo>
#include "base_define.h"

//数据序列模板类, 支持不同的数据类型T
template<typename T >
class Series
{
public:
    Series();
    Series(UINT32 length);
    Series(UINT32 length, QString head);
    ~Series();
    
    //数据修改追加，暂不支持删除
    void set_head(QString head){m_head = head;}
    void modify(UINT32 index, T value);
    void pushback(T value);
    
private:
    void set_datatype();
private:
    DataType    m_dtype;
    UINT32      m_length;
    QString     m_head;
    vector<T>   m_data;
    
};

#endif // SERIES_H


