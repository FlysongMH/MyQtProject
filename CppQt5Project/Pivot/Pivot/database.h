#ifndef DATA_H
#define DATA_H

//数据库类, 管理多个数据表格。支持数据透视

#include "dataframe.h"


class DataBase
{
public:
    DataBase();
    ~DataBase();

//********** 增加数据表格 **********
    void add_table(DataFrame* _DataFrame, const QString & _table_name);

//********** 删除数据表格 **********
    void remove_table(const int _table_index=0); //按照索引删除
    void remove_table(const QString & _table_name); //按照表格名删除
    void remove_table_first(); //删除第一个表格
    void remove_table_last(); //删除最后一个表格
    void remove_table_all(); //删除所有表格

//********** 修改数据表格 **********


//********** 辅助功能 **********
    //int check_table_name_duplicate(const QString & _table_name); //检查表格名是否重复
    
    
private:
    //私有数据信息，需保持大小一致
    int          m_table_cnt;        //表格数
    int          m_duplicate_cnt;       //表格名重复次数
    QStringList     m_table_name;       //表格名列表
    QList<DataFrame* > m_data;          //表格数据
};



#endif // DATA_H
