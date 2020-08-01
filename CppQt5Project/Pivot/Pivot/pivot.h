#ifndef PIVOT_H
#define PIVOT_H

#include <QWidget>
#include <QtWidgets>
#include <QMainWindow>
#include <QLabel>
#include <QDragEnterEvent> 
#include "data.h"

namespace Ui {
class Pivot;
}

class Pivot : public QMainWindow
{
    Q_OBJECT
    
public:
    explicit Pivot(QWidget *parent = NULLptr);
    ~Pivot() override;
    
private slots:
    void on_file_Open_triggered();
    void on_file_Save_triggered();
    void on_file_Close_triggered();
    
    void on_act_Open_triggered();
    
protected:
    void dragEnterEvent(QDragEnterEvent *event) override;
    void dropEvent(QDropEvent *event) override;
//    void mousePressEvent(QMouseEvent *event) override;
    
private:
    void OpenFiles();
    void OpenOneFile(QString FilePath);
    
private:
    Ui::Pivot *ui;
};

#endif // PIVOT_H
