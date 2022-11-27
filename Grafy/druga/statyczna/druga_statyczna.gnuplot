set terminal epslatex
set output './Grafy/druga/statyczna/graf.tex'
    set title "Otrzymane wyniki za pomocą metody statycznej"
    set xlabel 'Masa ciężarków[g]'
    set ylabel 'Wydłużenie[cm]'
    set grid
    plot './Grafy/druga/statyczna/data.csv' title "" with linespoints, 0.103*x + -0.258