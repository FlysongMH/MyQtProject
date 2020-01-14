#ifndef PIVOT_H
#define PIVOT_H

#include <QMainWindow>

namespace Ui {
class Pivot;
}

class Pivot : public QMainWindow
{
    Q_OBJECT
    
public:
    explicit Pivot(QWidget *parent = 0);
    ~Pivot();
    
private:
    Ui::Pivot *ui;
};

#endif // PIVOT_H
