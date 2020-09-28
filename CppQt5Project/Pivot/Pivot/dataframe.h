#ifndef DATABASE_H
#define DATABASE_H

//数据表格类, 处理一个数据表格

#include "dataseries.h"


//数据库类存储读取的数据，处理较小数据量时可以直接对每个表分配 行数*列数的大小，分配较大数据量时采用列存储
class DataFrame
{
public:
    DataFrame():m_row_cnt(0),m_col_cnt(0){}
    DataFrame(UINT32 RowCnt, UINT32 ColCnt);
    ~DataFrame();
    
    void resizeRow(UINT32 RowCnt){m_row_cnt=RowCnt;}
    void resizeCol(UINT32 ColCnt){m_col_cnt=ColCnt;}
    
    void set_table_name(QString table_name){m_table_name=table_name;}
    void add_sourcefile_url(QString table_name){m_table_name=table_name;}
    
private://数据源信息
    QString         m_table_name;      //表名
    QStringList     m_sourcefile_url;  //数据源文件URL列表
private:    //数据信息
    UINT32      m_row_cnt; //行数
    UINT32      m_col_cnt; //列数
    QStringList     m_header; //列名集合
    QList<Series* > m_data;     //表格数据
    
};

#endif // DATABASE_H
