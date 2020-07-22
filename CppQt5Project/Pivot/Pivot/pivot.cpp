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
