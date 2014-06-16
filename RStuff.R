
setwd('/Users/Teetor/Documents/Seventh Semester/Natural Language Processing/final project/code')

require(ggplot2)

CORPSDATA <- read.csv('corpusData.csv')
METHDATA <- read.csv('methodData.csv')

project.Data <- cbind(CORPSDATA[METHDATA$FileName,],METHDATA[,-1])
attach(project.Data)

# how well did they all do?
mean(PCPResult)
mean(MCSResult)
mean(FSTResult)
mean(ChanceResult)

mean(PCPScore)
mean(PCPActual)

mean(MCSScore)
mean(MCSActual)

mean(FSTScore)
mean(FSTActual)

sum(ifelse(PCPScore>PCPActual,1,0))
sum(ifelse(MCSScore>MCSActual,1,0))
sum(ifelse(FSTScore>FSTActual,1,0))

# PCP
ggplot(project.Data) +
  geom_point(aes(y=PCPScore,x=1:length(PCPResult),color='Predicted')) +
  geom_point(aes(y=PCPActual,x=1:length(PCPActual),color="Actual",alpha=0.9)) +
  ylim(0,3) +
  scale_color_discrete("Score Type") +
  labs(y="Score\n",x="\nFiles") +
  theme_bw()

# MCS
ggplot(project.Data) +
  geom_line(aes(y=MCSScore,x=1:length(MCSResult),color='Predicted')) +
  geom_line(aes(y=MCSActual,x=1:length(MCSActual),color="Actual")) +
  scale_color_discrete("Type") +
  labs(y="Score\n",x="\nTrial") +
  theme_bw()

a.subcorps <- CORPSDATA[CORPSDATA$WordCount<5000 & CORPSDATA$NumPara<100,]

qplot(NumPara,WordCount,data=project.Data[project.Data$NumPara<150,],
      size=factor(AvgParaSize),alpha=factor(Total*0.5),geom="jitter") +
  theme_bw() +
  theme(legend.position='none')


b.subcorps <- CORPSDATA[CORPSDATA$Nouns<5000,]
ggplot(project.Data) +
  geom_bar(aes(x=Verbs,fill='Verbs',position='dodge'),binwidth=50) +
  geom_bar(aes(x=Nouns,fill='Nouns',position='dodge'),binwidth=50) +
  geom_bar(aes(x=Adjectives,fill='Adjectives'),binwidth=50) +
  geom_bar(aes(x=Adverbs,fill='Adverbs'),binwidth=50) +
  labs(x="\nTarget Parts of Speech",y="Count") +
  scale_fill_discrete('Part of\nSpeech')
    
ggplot(b.subcorps,aes(x=c(Nouns,Verbs)) +
  geom_bar(position="dodge")
  

CORPSDATA[CORPSDATA$NumPara>400,]
CORPSDATA[CORPSDATA$Nouns>10000,]
