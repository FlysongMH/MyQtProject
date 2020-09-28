#ifndef PIVOT_H
#define PIVOT_H

//数据透视表界面，管理数据库与窗口界面的交互等


#include <QWidget>
#include <QtWidgets>
#include <QMainWindow>
#include <QLabel>
#include <QFileDialog>
#include <QTextStream>
#include <QDragEnterEvent>
#include "database.h"

namespace Ui {
class Pivot;
}

class Pivot : public QMainWindow
{
    Q_OBJECT
//********** 构造与析构 **********
public:
    explicit Pivot(QWidget *parent = NULLptr);
    ~Pivot() override;
    
//********** 普通成员函数 **********
private:
    void OpenFiles();
    void OpenOneFile(const QString &FilePath);

//********** 信号定义 **********
private slots:
    void on_file_Open_triggered();
    void on_file_Save_triggered();
    void on_file_Close_triggered();

    void on_act_Open_triggered();

//********** 鼠标拖放动作 重载 **********
protected:
    void dragEnterEvent(QDragEnterEvent *event) override;
    void dropEvent(QDropEvent *event) override;
//    void mousePressEvent(QMouseEvent *event) override;



//********** 成员变量 **********
private:
    Ui::Pivot *ui;
    DataBase  *m_database;

};

#endif // PIVOT_H
