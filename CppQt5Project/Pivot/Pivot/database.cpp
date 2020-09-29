#include "database.h"

DataBase::DataBase()
{
    m_table_cnt=0;
    m_duplicate_cnt=0;
}

DataBase::~DataBase()
{

    for(int i =0; i<m_data.size(); i++) {delete m_data[i];}
    m_data.clear();
}

//增加一个表格
void DataBase::add_table(DataFrame* _DataFrame, const QString & _table_name)
{
    QString new_table_name = _table_name;
    //检查表格名是否重复
    if(m_table_name.indexOf(new_table_name) >=0 )
    {
        m_duplicate_cnt++;
        new_table_name.append("_");
        new_table_name.append(m_duplicate_cnt);
    }
    
    m_table_cnt++;
    m_table_name.append(new_table_name);
    m_data.append(_DataFrame);
}

//按照索引删除表格
void DataBase::remove_table(const int _table_index)
{
    if(m_table_cnt <= _table_index) return;

    m_table_cnt--;
    m_table_name.removeAt(_table_index);
    delete m_data[_table_index];
    m_data.removeAt(_table_index);
}
//按照表格名删除表格
void DataBase::remove_table(const QString & _table_name)
{
    int _table_index = m_table_name.indexOf(_table_name);
    if(_table_index < 0) return;

    m_table_cnt--;
    m_table_name.removeAt(_table_index);
    delete m_data[_table_index];
    m_data.removeAt(_table_index);
}
void DataBase::remove_table_first()
{
    remove_table(0);
}
void DataBase::remove_table_last()
{
    remove_table(m_data.size()-1);
}
void DataBase::remove_table_all()
{
    m_table_cnt = 0;
    m_table_name.clear();
    for(int i =0; i<m_data.size(); i++) {delete m_data[i];}
    m_data.clear();
}
