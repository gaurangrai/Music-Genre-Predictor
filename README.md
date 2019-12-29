{\rtf1\ansi\ansicpg1252\cocoartf2511
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica-Bold;\f1\froman\fcharset0 Times-Roman;\f2\froman\fcharset0 Times-Bold;
\f3\fswiss\fcharset0 Helvetica;\f4\fnil\fcharset0 HelveticaNeue;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue0;\red27\green31\blue34;\red255\green255\blue255;
}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c0;\cssrgb\c14118\c16078\c18039;\cssrgb\c100000\c100000\c100000;
}
\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\b\fs36 \cf0 Music Genre Predictor
\fs28  \
\
\pard\pardeftab720\sl360\sa240\partightenfactor0

\f1\b0 \cf2 \expnd0\expndtw0\kerning0
We are in an age in which we have millions of option for music and limited time to decide whether we like or dislike a song, it would be sad if we miss out on some excellent songs, because we didn\'92t tumble upon them accidentally, while creating a collection which we will be using for years to come. \
Genre recommendation, can be used in music recommendation, automated radio, something new to explore and many more options. \
The purpose of this project is to find relation between songs and its genre, and create a model which can predict whether a song belongs to Folk, Electronic, Pop or Rock genre. \

\fs32 \

\f2\b\fs36 Data-Source:
\fs32 \
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\pardirnatural\partightenfactor0
{\field{\*\fldinst{HYPERLINK "https://os.unil.cloud.switch.ch/fma/fma_small.zip"}}{\fldrslt 
\f3\b0\fs28 \cf0 \kerning1\expnd0\expndtw0 fma_small.zip}}
\f4\b0\fs28 \cf3 \cb4 : 8,000 tracks of 30s, 8 balanced genres (GTZAN-like) (7.2 GiB)\
\

\f2\b\fs36 Usage:\
\

\f1\b0\fs28 python Code/CleanData.py\
python Code/MatrixGenerator.py\
python Code/DecisionTree.py\
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\pardirnatural\partightenfactor0
\cf3 python Code/ForestPredictor.py\
python Code/KNN.py
\f3\fs24 \cf0 \cb1 \kerning1\expnd0\expndtw0 \
\
\
\
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\pardirnatural\partightenfactor0

\f1 \cf2 \expnd0\expndtw0\kerning0
\
}