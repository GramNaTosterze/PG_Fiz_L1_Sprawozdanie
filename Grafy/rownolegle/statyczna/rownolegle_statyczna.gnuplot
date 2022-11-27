set terminal epslatex
set output './Grafy/rownolegle/statyczna/graf.tex'
    set title "Otrzymane wyniki za pomocą metody statycznej"
    set xlabel 'Masa ciężarków[g]'
    set ylabel 'Wydłużenie[cm]'
    set grid
    plot './Grafy/rownolegle/statyczna/data.csv' title "" with linespoints, 0.206*x + -0.556