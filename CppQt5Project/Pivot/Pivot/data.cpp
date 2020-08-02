#include "data.h"

DataBase::DataBase()
{
    m_row_cnt = 0;
    m_col_cnt = 0;
}

void DataBase::setRowCnt(UINT32 RowCnt)
{
    m_row_cnt = RowCnt;
}

void DataBase::setColCnt(UINT32 ColCnt)
{
    m_col_cnt = ColCnt;
}
