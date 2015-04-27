library(RWeka)

bi_gram = read.csv('fixed bigrams.txt', row.names = 1)
tri_gram = read.csv('fixed trigrams.txt', row.names = 1)
four_gram = read.csv('fixed four_grams.txt', row.names = 1)
five_gram = read.csv('fixed 5_grams.txt', row.names = 1)
grams = list(bi_gram,tri_gram,four_gram,five_gram)

prep_input<-function(x){
        #process the incoming string
        x<-tolower(x)
        
        #tokenize
        y<- NGramTokenizer(x, control=Weka_control(min = 1, max = 1, delimiters = " .',;:()?!"))
        return(y)}

predict = function(x){
        X_vector = prep_input(x)
        for (i in c(3,2,1,0)) {
                if (length(X_vector) > i) {
                        X = paste(tail(X_vector,i+1), collapse = ' ')
                        n_gram = grams[[i+1]]
                        if (!is.na(n_gram[X,])) {
                                output = n_gram[X,]
                                output = as.character(output)
                                return(output)
                        }
                }
        }
        return('the')        
}