set terminal epslatex
set output './Grafy/pierwsza/statyczna/graf.tex'
    set title "Otrzymane wyniki za pomocą metody statycznej"
    set xlabel 'Masa ciężarków[g]'
    set ylabel 'Wydłużenie[cm]'
    set grid
    plot './Grafy/pierwsza/statyczna/data.csv'  title "" with linespoints, 0.100*x + 0.040
    
    
    
        
