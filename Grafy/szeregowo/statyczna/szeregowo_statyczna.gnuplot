set terminal epslatex
set output './Grafy/szeregowo/statyczna/graf.tex'
    set title "Otrzymane wyniki za pomocą metody statycznej"
    set xlabel 'Masa ciężarków[g]'
    set ylabel 'Wydłużenie[cm]'
    set grid
    plot './Grafy/szeregowo/statyczna/data.csv' title "" with linespoints, 0.051*x + -0.119