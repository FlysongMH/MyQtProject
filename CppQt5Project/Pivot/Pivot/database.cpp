#include "database.h"

DataBase::DataBase()
{
    
}

DataBase::~DataBase()
{
    
    for(int i =0; i<m_data.size(); i++)
    {
        delete m_data[i];
    }
    m_data.clear();
}
