#include <QDebug>
#include <QFileDialog>
#include <QTextStream> 
#include "pivot.h"
#include "ui_pivot.h"

Pivot::Pivot(QWidget *parent) : QMainWindow(parent),
    ui(new Ui::Pivot)
{
    ui->setupUi(this);
}

Pivot::~Pivot()
{
    delete ui;
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
        }
    }

}

//Private Functions

void Pivot::OpenFiles()
{
    QStringList files = QFileDialog::getOpenFileNames(
                              this,
                              "Select one or more files to open",
                              "",
                              "Data (*.txt *.csv)");
    
    for(int i=0;i<files.size();i++)
    {
        qDebug()<<files[i];
        OpenOneFile(files[i]);
    }

}
void Pivot::OpenOneFile(QString FilePath)
{
    qDebug()<<"Pivot::OpenOneFile";
    QFile dictionaryFile(FilePath);
    dictionaryFile.open(QFile::ReadOnly);
    QTextStream inputStream(&dictionaryFile);
    
    int count=2;
    QString line;
    while (!inputStream.atEnd() && count>0) 
    {
        line = inputStream.readLine();
        qDebug()<<line<<"\n";
        count--;
    }
}
