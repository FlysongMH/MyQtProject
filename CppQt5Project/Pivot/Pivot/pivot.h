#ifndef PIVOT_H
#define PIVOT_H

#include <QMainWindow>
#include "base_define.h"

namespace Ui {
class Pivot;
}

class Pivot : public QMainWindow
{
    Q_OBJECT
    
public:
    explicit Pivot(QWidget *parent = NULLptr);
    ~Pivot();
    
private:
    Ui::Pivot *ui;
};

#endif // PIVOT_H
