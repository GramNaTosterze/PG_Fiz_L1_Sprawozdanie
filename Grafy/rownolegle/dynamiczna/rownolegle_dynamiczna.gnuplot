set terminal epslatex
set output './Grafy/rownolegle/dynamiczna/graf.tex'
    set title "Otrzymane wyniki za pomocą metody dynamicznej"
    set xlabel 'Masa ciężarków[g]'
    set ylabel 'Czas wykonywania 20 wachań[s]'
    set grid
    plot './Grafy/rownolegle/dynamiczna/data.csv' using 1:(($2 + $3 + $4) / 3.0) title "" with linespoints, 0.117*x + 3.269