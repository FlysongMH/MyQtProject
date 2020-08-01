//数据存储与处理类
#ifndef DATA_H
#define DATA_H

#include <QStringList>
#include "base_define.h"

//数据库类存储读取的数据，处理较小数据量时可以直接对每个表分配 行数*列数的大小，分配较大数据量时采用列存储
class DataBase
{
public:
    DataBase();
    DataBase(UINT32 row, UINT32 col);
    
    void setRowCnt(UINT32 RowCnt);
    void setColCnt(UINT32 ColCnt);
    
    
private:
    UINT32 m_col_cnt; //列数
    
    
    
    UINT32 m_row_cnt; //行数
    vector<double* > m_ori_data;
    
    
};

#endif // DATA_H
