#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>

namespace Ui {
class MainWindow;
}

enum operatorSymbol
{
    OP_NULL = 0,
    OP_Add,
    OP_Minus,
    OP_Multi,
    OP_Divi
    
};

class MainWindow : public QMainWindow
{
    Q_OBJECT
    
public:
    explicit MainWindow(QWidget *parent = nullptr);
    ~MainWindow();
    
private slots:
    void on_pushButton_0_clicked();
    void on_pushButton_1_clicked();
    void on_pushButton_2_clicked();
    void on_pushButton_3_clicked();
    void on_pushButton_4_clicked();
    void on_pushButton_5_clicked();
    void on_pushButton_6_clicked();
    void on_pushButton_7_clicked();
    void on_pushButton_8_clicked();
    void on_pushButton_9_clicked();
    void on_pushButton_point_clicked();
    
    void evalOnce();
    void on_pushButton_add_clicked();
    void on_pushButton_minus_clicked();
    void on_pushButton_multi_clicked();
    void on_pushButton_divi_clicked();
    void on_pushButton_eval_clicked();

    
    void on_pushButton_del_clicked();
    void on_pushButton_clear_clicked();


private:
    Ui::MainWindow *ui;
    double oldNumber;//四则运算第1个数字
    double newNumber;//四则运算第2个数字
    operatorSymbol OpSymbol;//运算符
    bool bRefreshDisplay;
    bool bHavePoint;
};

#endif // MAINWINDOW_H
