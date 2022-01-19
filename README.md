# votation_project
This project is to find affinity between users and parties in a given country using python data libraries: numpy and pandas.
<br>
The laws where gathered from the website of the congress in Peru, and from there the laws which had more relevance (there was
some expert advise in this matter) where gathered to create the model.
<br>
The model is prety simple, it gathers the information of the user on how much they are in favor or against the law 
and then it contrast them with the average score each party gave that law through votation.
<br>
The idea behind this model where twofold. First the model had to be prety simple so people could understand how was it
working under the hood. The second, was that we wanted to use real decisions on laws, and not only propposals. In spanish there is 
this saying: 'Entre el dicho y el hecho hay un gran trecho.' Which means that there is a great distance between what people
do and what people say they are going to do. Our hope was that at somedays our politicians think on their people
before casting their votes, and vote more similar to what they would have voted in their position. As Brandon Sanderson says "Politicians, it
seemed, often shared more with one another than they did with the people they represented." (Brandon Sanderson, The Dark Talent, p17)
<br>
The biggest problem that my project face, was a way to explain the law that wasn't very technical. The laws are pretty complex in
their nature and there was a lot of help by real lawyers in this aspect. I want to give a special thank to Antonella Putriano, for her hours 
checking my initial ideas of which laws to include. Any deficiency about any law is mine and not hers.
<br>
Finally, there are some ideas to improve the model. 
<br>1)First of all, I wanted to have a way to include more laws inside the mix, giving 
the code some connections to a database. 
<br>2) I want to have a way to filter the laws that are only procedures.
<br>3) I want to gives the user a way to create their own forms so they can share them.
<br>4) I want to have a way that people could give a ranking on how much the law is important.
