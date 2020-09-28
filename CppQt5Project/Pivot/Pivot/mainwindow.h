#ifndef MAINWINDOW_H
#define MAINWINDOW_H

//数据透视表界面，管理数据库与窗口界面的交互等

#include <QMainWindow>
#include <QWidget>
#include <QtWidgets>
#include <QLabel>
#include <QFileDialog>
#include <QTextStream>
#include <QDragEnterEvent>
#include "database.h"

namespace Ui {
class MainWindow;
}

class MainWindow : public QMainWindow
{
    Q_OBJECT
//********** 构造与析构 **********
public:
    explicit MainWindow(QWidget *parent = nullptr);
    ~MainWindow() override;
    
//********** 普通成员函数 **********
    
    
//********** 信号定义 **********
signals:
    
    
//********** 鼠标拖放动作 重载 **********
protected:
//    void dragEnterEvent(QDragEnterEvent *event) override;
//    void dropEvent(QDropEvent *event) override;
//    void mousePressEvent(QMouseEvent *event) override;
    
    
//********** 成员变量 **********
private:
    Ui::MainWindow *ui;
    DataBase  *m_database;
};

#endif // MAINWINDOW_H
