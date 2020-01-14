#include "mainwindow.h"
#include "ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    const bool __sortingEnabled = ui->listWidget->isSortingEnabled();
    ui->listWidget->setSortingEnabled(false);
    for(int currenRow=0; currenRow<10; currenRow++)
    {
        ui->listWidget->addItem(tr("%1").arg(currenRow));
    }
    ui->listWidget->setSortingEnabled(__sortingEnabled);
    
    
}

MainWindow::~MainWindow()
{
    delete ui;
}


void MainWindow::on_listWidget_itemDoubleClicked(QListWidgetItem *item)
{
    int currenRow = ui->listWidget->currentRow();
    ui->listWidget->takeItem(currenRow);
    
}
