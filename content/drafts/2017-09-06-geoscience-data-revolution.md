title: The Reasonable Effectiveness of Open Geoscience Data
slug: effectiveness-open-data
category: article
tags: open data, geoscience, machine learning, data science
date: 2019-02-10
modified: 2019-02-10
status: draft

## Intro

- It has been about two years since the SEG machine learning contest wrapped up.  
- This contest was proposed in the facies classification tutorial I wrote for the October 2016 issue of the leading edge.
- This tutorial showed how to create a simple machine learning model to predict lithofacies from well logs using a small dataset from southwest Kansas (Dubois et al. 2007).
- Editor Matt Hall issued a challenge to see who could create an improved model
- The response was enthusiastic to say the least.  Over 300 entries were submitted by 40 teams from all over the world.
- The contest was run with in the spirit of collaboration, with teams submitting their models to the contest github repo and building on each others ideas.  
- This resulted in impressive innovations in feature engineering and model design. 
Check out the [summary article](https://library.seg.org/doi/pdf/10.1190/tle36030267.1) for more details on the contest results.

- During the past two years researchers, students and professionals have continued to use this dataset to learn about machine learning and develop improved facies prediction models, providing an example of how a simple, small but well curated dataset can fire the imaginations of geoscientists eager to develop their machine learning skills and spur an impressive amount of innovation.
- The developments I’ve observed can be can be divided into three main categories: Innovation, Community and Education.

## Innovation
The most satisfying outcome of the contest is the quality and quantity of subsequent projects it has inspired.  Students, researchers and enthusiasts from all over the world have continued to develop the ideas generated during the contest, applying new technologies and improving on the contest results.  Quite a few papers 

Bestagini, P., Lipari, V. & Tubaro, S. (2017) [A machine learning approach to facies classification using well logs](https://doi.org/10.1190/segam2017-17729805.1). SEG Technical Program Expanded Abstracts 2017: pp. 2137-2142.

Zhang, L. & Zhan, C. (2017) [Machine learning in rock facies classification: An application of XGBoost](https://doi.org/10.1190/IGC2017-351). International Geophysical Conference, Qingdao, China, 17-20 April 2017: pp. 1371-1374.

Tschannen, V., Delescluse, M., Rodriguez, M. & Keuper, J. (2017). [Facies classification from well logs using an inception convolutional network](https://arxiv.org/abs/1706.00613). arXiv preprint arXiv:1706.00613.

Chen, J. & Zeng, Y. (2018). [Application of Machine Learning in Rock Facies Classification with Physics-Motivated Feature Augmentation](https://arxiv.org/abs/1808.09856). arXiv preprint arXiv:1808.09856.

Shashank, S. & Mahapatra, M. P. (2018, November). [Boosting Rock Facies Prediction: Weighted Ensemble of Machine Learning Classifiers](https://doi.org/10.2118/192930-MS). In Abu Dhabi International Petroleum Exhibition & Conference. Society of Petroleum Engineers.  

Imamverdiyev, Y. & Sukhostat, L. (2019). [Lithological facies classification using deep convolutional neural network](https://doi.org/10.1016/j.petrol.2018.11.023). Journal of Petroleum Science and Engineering, 174, 216-228. 




## The importance of benchmarks
SPE reservoir simulation datasets
SEAM models

- what is a benchmark?
- dataset that can be used to evaluate new methods, improve old ones
common framework to facilitate discussion
- difference between benchmarks and open (or almost open) data repositories like Poseidon and Volve.


## Community

- community (swung)
- check it out, plenty of conversations about cutting edge work being done in computational geoscience

## Education
- dataset started out on a class website, continues to be used to benchmark
low barrier to entry for people using datasets
- Clean dataset, labeled and ready to be used
- straightforward tutorial example showing how to use dataset in 20 lines of Python code.

of course, oil and gas companies can't make all their data open to the public I'm not advocating this and it isn't a good idea
there is too much of it, and companies derive much value from their proprietary data
there is a wealth of open geoscience data out there
innovation in data science can happen with small, tidy, well curated datasets that have a purpose
small/convenient - easy to obtain and quick to start using
tidy - require a minimum of data cleaning to start using effectively. More on this in the next post
well curated - have documentation and tutorial articles for how to get started using the dataset
If you're working on a project with open data, I encourage you to share your story; what you did to clean it up, how you structured it, and what you did with it.
Just as with the Kansas dataset, each of these datasets has a potential to spark a revolution on its on
For the forseeable future, this blog will focus on sharing other open datasets that I have found and worked with. I hope you will use them as part of your own projects, share your results, and join the discussion.

Machine learning was already becoming a hyped subject two years ago, a trend that shows no signs of slowing.
The pace of technology development in this area is disorientingly fast, changing the way we work, play, drive and vote.  All these developments (for better or worse), have one thing in common: they depend on high quality data.  
Datasets like ImageNet with millions of labeled images have fueled the development of CNNs and which are an essential component to the AI in self-driving cars.
geoscientists typically have access to plenty of data, but not always in a form immediately suitable for machine learning.  
the data may messy, unorganized and not in digital form.  It is often unlabeled, a prerequisite for supervised learning methods such as facies classification.  And quite often the data is not open so that it can be freely used and shared by anyone interested.


## References
Dubois, M. K., Bohling, G. C. and Chakrabarti, S. (2007). [Comparison of four approaches to a rock facies classification problem](http://dx.doi.org/10.1016/j.cageo.2006.08.011). Computers & Geosciences, 33(5), 599–617.

Hall, M. and Hall, B. (2017) [Distributed collaborative prediction: Results of the machine learning contest](https://doi.org/10.1190/tle36030267.1). The Leading Edge, 36(3), 267--269. 


