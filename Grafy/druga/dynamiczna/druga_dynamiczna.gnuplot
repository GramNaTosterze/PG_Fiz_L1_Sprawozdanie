set terminal epslatex
set output './Grafy/druga/dynamiczna/graf.tex'
    set title "Otrzymane wyniki za pomocą metody dynamicznej"
    set xlabel 'Masa ciężarków[cm]'
    set ylabel 'Czas wykonywania 20 wachań[s]'
    set grid
    plot './Grafy/druga/dynamiczna/data.csv' using 1:(($2 + $3) / 2.0) title "" with linespoints