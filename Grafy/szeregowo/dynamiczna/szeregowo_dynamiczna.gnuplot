set terminal epslatex
set output './Grafy/szeregowo/dynamiczna/graf.tex'
    set title "Otrzymane wyniki za pomocą metody dynamicznej"
    set xlabel 'Masa ciężarków[g]'
    set ylabel 'Czas wykonywania 20 wachań[s]'
    set grid
    plot './Grafy/szeregowo/dynamiczna/data.csv' using 1:(($2 + $3 + $4) / 3.0) title "" with linespoints, 0.061*x + 1.862