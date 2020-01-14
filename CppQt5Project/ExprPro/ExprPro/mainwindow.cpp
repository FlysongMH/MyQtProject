#include "mainwindow.h"
#include "ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    ui->label->setText("");
    oldNumber = 0.0;
    newNumber = 0.0;
    OpSymbol = OP_NULL;
    bRefreshDisplay = false;
    bHavePoint = false;
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::on_pushButton_0_clicked()
{
    QString number = bRefreshDisplay? "": ui->label->text();
    ui->label->setText(number + QString("0"));
    bRefreshDisplay = false;
}
void MainWindow::on_pushButton_1_clicked()
{
    QString number = bRefreshDisplay? "": ui->label->text();
    ui->label->setText(number + QString("1"));
    bRefreshDisplay = false;
}
void MainWindow::on_pushButton_2_clicked()
{
    QString number = bRefreshDisplay? "": ui->label->text();
    ui->label->setText(number + QString("2"));
    bRefreshDisplay = false;
}
void MainWindow::on_pushButton_3_clicked()
{
    QString number = bRefreshDisplay? "": ui->label->text();
    ui->label->setText(number + QString("3"));
    bRefreshDisplay = false;
}
void MainWindow::on_pushButton_4_clicked()
{
    QString number = bRefreshDisplay? "": ui->label->text();
    ui->label->setText(number + QString("4"));
    bRefreshDisplay = false;
}
void MainWindow::on_pushButton_5_clicked()
{
    QString number = bRefreshDisplay? "": ui->label->text();
    ui->label->setText(number + QString("5"));
    bRefreshDisplay = false;
}
void MainWindow::on_pushButton_6_clicked()
{
    QString number = bRefreshDisplay? "": ui->label->text();
    ui->label->setText(number + QString("6"));
    bRefreshDisplay = false;
}
void MainWindow::on_pushButton_7_clicked()
{
    QString number = bRefreshDisplay? "": ui->label->text();
    ui->label->setText(number + QString("7"));
    bRefreshDisplay = false;
}
void MainWindow::on_pushButton_8_clicked()
{
    QString number = bRefreshDisplay? "": ui->label->text();
    ui->label->setText(number + QString("8"));
    bRefreshDisplay = false;
}
void MainWindow::on_pushButton_9_clicked()
{
    QString number = bRefreshDisplay? "": ui->label->text();
    ui->label->setText(number + QString("9"));
    bRefreshDisplay = false;
}
void MainWindow::on_pushButton_point_clicked()
{
    if(bHavePoint) return;
    QString number = bRefreshDisplay? "": ui->label->text();
    ui->label->setText(number + QString("."));
    bHavePoint = true;
}
//计算+ - * /
void MainWindow::on_pushButton_add_clicked()
{
    oldNumber = ui->label->text().toDouble();
    OpSymbol = OP_Add;
    ui->label->setText("");
}
void MainWindow::on_pushButton_minus_clicked()
{
    oldNumber = ui->label->text().toDouble();
    OpSymbol = OP_Minus;
    ui->label->setText("");
}
void MainWindow::on_pushButton_multi_clicked()
{
    oldNumber = ui->label->text().toDouble();
    OpSymbol = OP_Multi;
    ui->label->setText("");
}
void MainWindow::on_pushButton_divi_clicked()
{
    oldNumber = ui->label->text().toDouble();
    OpSymbol = OP_Divi;
    ui->label->setText("");
}
/*
求值"="运算，新输入值设置为newnumber
将oldNumber与newNumber运算，
然后替换：oldNumber=result
*/
void MainWindow::on_pushButton_eval_clicked()
{
    if (!bRefreshDisplay)
        newNumber = ui->label->text().toDouble();
    evalOnce();
    ui->label->setText(QString::number(oldNumber));
    bRefreshDisplay = true;
}

void MainWindow::evalOnce()
{
    double result = oldNumber;
    if (OpSymbol == OP_NULL)
    {
        return;
    }
    else if (OpSymbol == OP_Add)
    {
        result = oldNumber+newNumber;
    }
    else if (OpSymbol == OP_Minus) 
    {
        result = oldNumber-newNumber;
    }
    else if (OpSymbol == OP_Multi) 
    {
        result = oldNumber*newNumber;
    }
    else if (OpSymbol == OP_Divi && newNumber!=0) 
    {
        result = oldNumber/newNumber;
    }
    oldNumber = result;
}

//
void MainWindow::on_pushButton_del_clicked()
{
    QString number = ui->label->text();
    QString newNumber="";
    if(number.length() > 1)
    {
        newNumber = number.left(number.length()-1);
    }
    ui->label->setText(newNumber);
}
void MainWindow::on_pushButton_clear_clicked()
{
    ui->label->setText("");
    oldNumber = 0.0;
    newNumber = 0.0;
    OpSymbol = OP_NULL;
    bRefreshDisplay = true;
}
