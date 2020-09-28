#ifndef DATA_H
#define DATA_H

//数据库类, 管理多个数据表格。支持数据透视

#include "dataframe.h"


class DataBase
{
public:
    DataBase();
    ~DataBase();
    
    void set_table_num(UINT32 table_cnt){m_table_cnt = table_cnt;}
    void add_table(UINT32 table_cnt=1){m_table_cnt+=table_cnt;}
    void add_table(DataFrame* newDataFrame){m_table_cnt++; m_data.append(newDataFrame);}
    
private:    //私有数据信息
    UINT32          m_table_cnt;        //表格数
    QStringList     m_table_name;       //表格名
    QStringList     m_sourcefile_url;   //数据源文件URL列表

    QList<DataFrame* > m_data;          //表格数据
};



#endif // DATA_H
