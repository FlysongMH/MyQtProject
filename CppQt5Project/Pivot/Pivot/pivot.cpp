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
