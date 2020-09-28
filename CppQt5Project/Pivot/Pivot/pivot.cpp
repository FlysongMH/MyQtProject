#include <QDebug>
#include <QTime>
#include "pivot.h"
#include "ui_pivot.h"

Pivot::Pivot(QWidget *parent) : 
    QMainWindow(parent),
    ui(new Ui::Pivot),
    m_database(new DataBase)
{
    ui->setupUi(this);
    
//    m_database = new DataBase();
}

Pivot::~Pivot()
{
    delete ui;
    delete m_database;
}

//菜单栏动作
void Pivot::on_file_Open_triggered()
{
    OpenFiles();
}

void Pivot::on_file_Save_triggered()
{
    
}

void Pivot::on_file_Close_triggered()
{
    
}
//工具栏动作
void Pivot::on_act_Open_triggered()
{
    OpenFiles();
}

//主窗口的拖拽
void Pivot::dragEnterEvent(QDragEnterEvent *event)
{
    if(event->mimeData()->hasUrls())
    {
        event->acceptProposedAction();
    }
    else
    {
        event->ignore();
    }
}

void Pivot::dropEvent(QDropEvent *event)
{
    qDebug()<<"Pivot::dropEvent";
    const QMimeData* qm=event->mimeData();  //获取MIMEData
    for(int i=0; i<qm->urls().size();i++)
    {
        QString OneUrl = qm->urls()[i].toLocalFile();
        if(!OneUrl.right(3).compare("txt") || !OneUrl.right(3).compare("csv"))
        {
            qDebug()<<OneUrl;
            OpenOneFile(OneUrl);
        }
    }

}
