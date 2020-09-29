/*
 * Pivot类的数据导入导出功能库
*/
#include <QDebug>
#include <QTime>
#include "pivot.h"

//弹出文件对话框打开多个文件
void Pivot::OpenFiles()
{
    //通过文件对话框获取要打开的文件路径列表
    QStringList files = QFileDialog::getOpenFileNames(
                              this,
                              "Select one or more files to open",
                              "",
                              "Data (*.txt *.csv)");
    //依次打开每个文件
    for(int i=0;i<files.size();i++)
    {
        qDebug()<<files[i];
        OpenOneFile(files[i]);
    }

}
//打开一个指定文件
void Pivot::OpenOneFile(const QString &FilePath)
{
    int row_cnt=0;
    int col_cnt=0;
    QStringList heads_ori;
    QStringList heads;
    QList<DataType> dtype; //每一列的数据类型
    QTime time;
    
    //open file
    qDebug()<<"Pivot::OpenOneFile";
    QFile dictionaryFile(FilePath);
    dictionaryFile.open(QFile::ReadOnly);
    QTextStream inputStream(&dictionaryFile);
    
    //read head
    heads_ori=inputStream.readLine().split(",");
    col_cnt = heads_ori.size();
    qDebug()<<"heads:\n"<<heads_ori<<"\n";
    for(int i=0;i<col_cnt;i++)
    {
        //检查列名重复, 对重复的列名增加编号去重
        QString ori_name = heads_ori[i];
        int num=0;
        for(int j=0;j<i;j++)
        {
            if(ori_name == heads_ori[j])
                num++;
        }
        if(num>0)
            ori_name += QString::number(num);
        heads.append(ori_name);
        dtype.append(DT_INT); //初始每一列都设置为int类型
    }
    //记录数据起始位置，后续要读取两遍
    UINT32 pos_start = (UINT32)inputStream.pos();
    qDebug()<<"pos:"<<pos_start;
    

    //read table

    QString     line;
    QStringList words;
    QString     word;
    int         word_int;
    double      word_dbl;
    bool        ok;
    
    //第一遍读取, 先确定行数以及每一列的数据类型
    time.start();
    while (!inputStream.atEnd())
    {
        line = inputStream.readLine();
        words = line.split(",");
        if(words.size() != col_cnt) return; //格式错误，列数不对齐。退出后续的读取
        for(int i=0;i<col_cnt;i++)
        {
            ok = false;
            //作为32位整数处理
            if(dtype[i]==DT_INT)
            {
                word_int = words[i].toInt(&ok);
                if(ok)
                {
                    continue;
                }
                else
                {
                    dtype[i] = DT_DOUBLE;
                }
            }
            //作为浮点数处理
            if(!ok && dtype[i]==DT_DOUBLE)
            {
                word_dbl = words[i].toDouble(&ok);
                if(ok)
                {
                    continue;
                }
                else
                {
                    dtype[i] = DT_STRING;
                }
            }
            //作为字符串处理
            if(!ok)
            {
                //对String的处理
            }
        }
        row_cnt++; //读取下一行
    }
    qDebug()<<"row count:"<<row_cnt;
    qDebug()<<"Time elapsed:"<<time.elapsed();
    
    
    DataFrame *table = new DataFrame((UINT32)row_cnt, (UINT32)col_cnt);
    m_database->add_table(table, "");
    //第二遍读取, 存储数据
    inputStream.seek(pos_start);
    time.start();
    while (!inputStream.atEnd())
    {
        line = inputStream.readLine();
        words = line.split(",");
        if(words.size() != col_cnt) return; //格式错误，列数不对齐。退出后续的读取
        for(int i=0;i<col_cnt;i++)
        {
            
            if(dtype[i]<=DT_INT) //作为32位整数处理
            {
                word_int = words[i].toInt();
            }
            else if(dtype[i]<=DT_DOUBLE) //作为浮点数处理
            {
                word_dbl = words[i].toDouble();
            }
            else if(dtype[i]<=DT_STRING) //作为字符串处理
            {
                
            }
        }
        row_cnt++; //读取下一行
    }
    qDebug()<<"Time elapsed:"<<time.elapsed();
}
