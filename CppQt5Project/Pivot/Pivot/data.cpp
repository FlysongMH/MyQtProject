#include "data.h"

DataFrame::DataFrame(UINT32 RowCnt, UINT32 ColCnt):
    m_row_cnt(RowCnt),
    m_col_cnt(ColCnt)
{
    
}
DataFrame::~DataFrame()
{
    QList<Series*>::ConstIterator ci;
    for(ci=m_data.constBegin();ci!=m_data.constEnd();++ci)
    {
        delete *ci;
    }
    m_data.clear();
}
