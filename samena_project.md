
### AUTO ASSIGNMENT  VALUATION SYSTEM USING ARTIFICIAL INTELLIGENCE AND MACHINE LEARNING

By


### Romania Akram

2022-ag-6340


### A research report submitted in partial fulfillment of the requirements for the degree

of


### Bachelor of Science

in


### Computer Science


### UNIVERSITY OF AGRICULTURE FAISALABAD


### CONSTITUENT COLLEGE TOBA TEK SINGH

2026


### CERTIFICATE

To,


### The Controller of Examinations,


### University of Agriculture,


### Faisalabad Constituent College Toba Tek Singh.

We, the advisory committee, certify that the contents and form of this report submitted by Romania Akram, 2022-AG-6340 has been found satisfactory and recommend that it be processed for evaluation for the award of the degree.


### ADVISORY COMMITTEE:


### Advisor                                                                                        __________________

Mr. Syed Ali Imran


### Member                                                                                           __________________

Mr. Muhammad Shan Afzal


### DECLARATION


### The project work described above was undertaken by us under the guidance of Mr. Syed Ali Imran University of Agriculture, Faisalabad. We, the undersigned, do hereby declare that the “Auto Assignment  Valuation System Using Artificial Intelligence And Machine Learning ” and the project work above is the result of our own research. We also do hereby declare that the above project work has not been presented by us for the award of any other degree or diploma. Any incorrect information may lead to action by the University at any stage.


### Romania Akram

2022-ag- 6340

O, ALLAH


### You could have left me in darkness,


### But you didn’t.I


### am grateful


### All Praise is Yours


### ALHAMDULILLAH                           DEDICATED

TO


### HOLY PROPHET

(S.A.W) MY


### FAMILY MY


### TEACHERS &


### MY FRIENDS


### WHO ENCOURAGED ME AT


### EVERY STEP OF THE DEGREE


### ACKNOWLEDGEMENT


### I take this opportunity to express my profound gratitude and deep regards to my guiders MR. Syed. Ali Imran, for their exemplary guidance, monitoring and constant encouragement throughout the course of this project. Their contribution in stimulating suggestions and encouragement helped me to coordinate my project, especially in writing this report. I have made an effort in this project. However, it would not have been possible without the kind support and help of my mentor. I would like to extend my sincere thanks to them. Lastly, I thank ALLAH ALMIGHTY, my parents, brothers, and friends for their constant encouragement and kind cooperation without which assignment would not be possible.


### Romania

2022-AG-6340


## Abstract


### This report presents the design, development, and implementation of an Auto Assignment Valuation System, an AI-powered platform that automates the evaluation of student assignments using natural language processing (NLP) and machine learning (ML). The system addresses critical challenges in educational assessment, including grading inconsistency, instructor workload, and delayed feedback, by providing an automated, scalable, and objective evaluation mechanism. It compares student responses with model answers using semantic similarity analysis, performs grammar and content coherence checks, and generates instant scores and personalized feedback. Developed with Python, NLP libraries (spaCy/NLTK), machine learning frameworks (scikit-learn/TensorFlow), and transformer models (BERT/RoBERTa), the platform features a cloud-based architecture with role-specific dashboards for teachers and students. Aligned with Sustainable Development Goal 4 (Quality Education) and Goal 9 (Industry, Innovation, and Infrastructure), this project contributes to the digital transformation of education by promoting efficient, unbiased, and accessible assessment practices. The system demonstrates the practical application of AI in real-world educational contexts, offering a prototype for scalable, intelligent assessment solutions in academic institutions.Keywords: Automated Assessment, AI in Education, Natural Language Processing, Machine Learning, Assignment Valuation, Semantic Similarity, Educational Technology, SDG 4, SDG 9.


## Table of Contents


## Table of Contents


## Table of Contentsvii


## Chapter 11

1.Introduction1


### 1.1  Background and Context1


### 1.2 Problem Statement2


### 1.2.1 High Instructor Workload and Time Constraints2


### 1.2.2 Inconsistency and Subjectivity in Grading:3


### 1.2.3 Delayed and Inadequate Feedback:3


### 1.2.4 Scalability Challenges in Growing Educational Systems:3


### 1.2.5 Limited Analytical Insights:3


### 1.2.6 Resource Inequality:3


### 1.3 Research Objectives4


### 1.3.1 Primary Objective:4


### 1.4 Scope and Limitations6


### 1.4.1 Scope of the Project6


### 1.4.2 Limitations and Delimitations:7


### 1.5 Significance of the Study8


### 1.5.1 Academic and Research Significance:8


### 1.5.2 Pedagogical and Educational Significance8


### 1.5.3 Technological and Practical Significance:9


### 2.1 Evolution of Educational Assessment Systems10


### 2.2 Artificial Intelligence in Education (AIED)12


### 2.3 Natural Language Processing (NLP) in Automated Grading13


### 2.4 Machine Learning Approaches for Text Evaluation15


### 2.5 Existing Automated Assessment Systems17


### 2.6 Text Similarity and Semantic Analysis Techniques18


### 2.7 Educational Data Mining and Learning Analytics20


### 2.8 Trust, Fairness, and Bias in AI-Based Assessment21


### 2.9  Research Gap and Contribution23


## Chapter 1


## Introduction


### 1.1  Background and Context


### The landscape of education has undergone profound transformation over the past two decades, driven by digitalization, increased accessibility to technology, and evolving pedagogical approaches. Within this evolving ecosystem, assessment remains a cornerstone of the learning process, serving as a critical mechanism for evaluating student comprehension, providing feedback, and guiding instructional improvement. Traditional methods of assessment, particularly for written assignments, have largely relied on manual grading by educators—a process that is not only time-consuming and labor-intensive but also susceptible to inconsistencies, subjective bias, and delays in feedback delivery. As class sizes expand in both physical and virtual learning environments, and as the demand for personalized and timely educational experiences grows, the limitations of conventional grading practices become increasingly apparent.


### The integration of Artificial Intelligence (AI) and Machine Learning (ML) into educational technology (EdTech) presents a paradigm shift in how assessments can be administered, evaluated, and analyzed. AI-driven systems have demonstrated remarkable potential in automating repetitive and analytical tasks, offering scalability, consistency, and data-driven insights. In the context of assignment valuation, AI can process natural language, evaluate content relevance, assess structural and grammatical correctness, and even gauge conceptual understanding through advanced semantic analysis. This capability aligns with the broader movement toward Learning Analytics and Educational Data Mining, where data generated from student interactions is used to enhance learning outcomes, tailor instructional strategies, and improve educational systems.


### The concept of automated essay scoring (AES) and assignment evaluation is not entirely new; early systems like Project Essay Grader (PEG) emerged in the 1960s. However, recent advancements in Natural Language Processing (NLP), deep learning, and transformer-based models (e.g., BERT, GPT) have dramatically improved the accuracy, nuance, and applicability of such systems. These technologies enable more sophisticated analysis beyond simple keyword matching, allowing for the evaluation of argument coherence, factual accuracy, creativity, and adherence to rubrics. Consequently, there is a growing academic and commercial interest in developing intelligent assessment tools that can support educators, empower students, and optimize institutional resources.


### Furthermore, the global commitment to the United Nations Sustainable Development Goals (SDGs), particularly SDG 4: Quality Education and SDG 9: Industry, Innovation, and Infrastructure, underscores the need for innovative solutions that make education more inclusive, equitable, and effective. An automated, AI-based valuation system directly contributes to these goals by increasing the efficiency and fairness of assessments, enabling educators to focus more on teaching and mentorship, and providing students with immediate, actionable feedback that supports continuous learning. By leveraging cutting-edge AI/ML technologies, this project, titled the "Auto Assignment Valuation System," seeks to operationalize these principles, offering a practical, scalable tool designed for modern educational environments.


### 1.2 Problem Statement


### Despite the critical role of assessments in education, the current manual grading paradigm is fraught with significant challenges that hinder educational efficiency, equity, and effectiveness. These challenges are particularly acute in contexts involving large volumes of text-based assignments, such as essays, short answers, and reports. The core problems that this project aims to address are multi-faceted:


### 1.2.1 High Instructor Workload and Time Constraints: Educators spend an inordinate amount of time grading assignments, which detracts from other essential activities such as lesson planning, one-on-one student support, and professional development. In large classes or massive open online courses (MOOCs), this workload becomes unsustainable, often leading to grading fatigue, reduced feedback quality, and significant delays in returning evaluated work to students.


### 1.2.2 Inconsistency and Subjectivity in Grading: Human grading is inherently subjective. Different instructors, or even the same instructor at different times, may apply scoring rubrics inconsistently. Factors such as handwriting quality, writing style preferences, fatigue, or unconscious bias can influence scores, compromising the fairness and reliability of assessments. This inconsistency can undermine student trust in the evaluation process and create perceptions of inequity.


### 1.2.3 Delayed and Inadequate Feedback: Timely feedback is crucial for effective learning, as it allows students to understand their mistakes, correct misconceptions, and improve subsequent performance. Manual grading processes often result in feedback delays of days or even weeks, diminishing the learning impact. Moreover, due to time pressures, feedback may be limited to brief comments or numerical scores, lacking the depth and personalization needed for meaningful learning progress.


### 1.2.4 Scalability Challenges in Growing Educational Systems: With the expansion of higher education and the rise of digital and distance learning models, educational institutions are required to assess an ever-growing number of students efficiently. Traditional manual methods do not scale effectively, creating bottlenecks that can affect course pacing, student satisfaction, and institutional reputation.


### 1.2.5 Limited Analytical Insights: Manual grading typically culminates in a final score without systematically capturing or analyzing patterns in student responses. Valuable data regarding common misconceptions, difficulty levels of questions, or the effectiveness of teaching materials remain untapped. This lack of analytics limits evidence-based improvements in curriculum design and instructional methods.


### 1.2.6 Resource Inequality: High-quality, prompt assessment is resource-intensive. Well-resourced institutions may manage better than under-resourced ones, exacerbating educational inequalities. An automated system can help level the playing field by providing a consistent, high-quality assessment tool accessible to a wider range of institutions.


### The Auto Assignment Valuation System is conceived as a direct response to these interconnected problems. It proposes to leverage Artificial Intelligence specifically Natural Language Processing and Machine Learning to automate the evaluation of text-based assignments. The system is designed to provide instant, consistent, and rubric-aligned scoring along with detailed feedback, thereby alleviating instructor burden, enhancing grading fairness, accelerating the feedback loop, and generating valuable learning analytics. By addressing these core issues, the project aims to contribute to a more efficient, equitable, and data-informed educational assessment ecosystem.


### 1.3 Research Objectives


### The primary aim of this project is to design, develop, and evaluate a fully functional, AI-driven Auto Assignment Valuation System that automates the assessment of student-written assignments. This overarching goal is decomposed into the following specific, measurable, and technically grounded objectives:


### 1.3.1 Primary Objective:


### To develop an integrated web-based software application that utilizes Natural Language Processing (NLP) and Machine Learning (ML) algorithms to automatically evaluate text-based student assignments, generate scores, and provide constructive feedback.


### 1.3.2 Technical Development Objectives:


### To design and implement a robust system architecture that supports multi-user roles (Student, Teacher, Admin), secure data handling, and scalable cloud-based operations.


### To develop a core NLP pipeline for preprocessing assignment text, including tokenization, stop-word removal, stemming/lemmatization, and part-of-speech tagging using libraries such as spaCy or NLTK.


### To implement a semantic similarity assessment module using state-of-the-art transformer-based models (e.g., Sentence-BERT, RoBERTa) to compare student answers against model answers or rubric-defined key concepts.


### To integrate grammatical and structural analysis features that evaluate writing quality, including grammar checking, spelling correction, and coherence scoring.


### To engineer a machine learning-based scoring engine that combines multiple features (semantic similarity, grammar score, content coverage, keyword presence) into a final, rubric-weighted grade. This may involve regression models or rule-based scoring algorithms.


### To develop an automated feedback generation component that produces specific, actionable comments for students based on the analysis of their submissions (e.g., "Consider expanding on the concept of X," "Check subject-verb agreement in paragraph 2").


### To create intuitive user interfaces (dashboards) for teachers to upload assignments, set rubrics, review automated grades, and provide overrides, and for students to submit work and view grades/feedback.


### To implement a secure backend database (using MySQL or Firebase) for storing user data, assignments, model answers, grading results, and feedback history.


### 1.3.3 Evaluation and Validation Objectives:


### To validate the system's performance by comparing its automated grades against a benchmark set of manually graded assignments by experienced educators. Key metrics will include accuracy, precision, recall, F1-score, and correlation coefficients (e.g., Pearson's r).


### To assess the system's utility and usability through pilot testing with a group of teachers and students, gathering feedback on interface design, feedback relevance, grading fairness, and overall system effectiveness.


### 1.3.4 Alignment and Contribution Objectives:


### To ensure the project aligns with Sustainable Development Goals: Specifically, to contribute to SDG 4 (Quality Education) by enhancing assessment efficiency and feedback quality, and to SDG 9 (Industry, Innovation, and Infrastructure) by building a novel AI-powered educational tool.


### To produce comprehensive project documentation, including a final report, system design specifications, user manuals, and source code, to facilitate future development and academic reference.


### These objectives collectively guide the project from conception through implementation to validation, ensuring the delivery of a technically sound, educationally valuable, and practically usable system


### 1.4 Scope and Limitations


### 1.4.1 Scope of the Project:


### The development of the Auto Assignment Valuation System will encompass the following defined boundaries and deliverables:


### Application Type: A web-based application accessible via standard browsers. Responsive design principles will be applied for usability on tablets, but a dedicated mobile app is out of scope.


### Core Functionality:


### User Role Management: Three primary roles: Student (submit, view feedback), Teacher (upload assignments/rubrics, monitor grading, override scores), Administrator (manage users, system settings).


### Assignment Handling: Support for text-based assignments (essays, short answers, paragraphs). File upload will be limited to text inputs or document formats like `.txt` and `.pdf` (with text extraction).


### AI Evaluation Engine: Automatic scoring based on:


### Semantic Similarity: Primary method for content valuation.


### Grammar & Mechanics: Basic error detection.


### Keyword/Concept Presence: As defined in rubrics.


### Feedback Generation: Automated comments linked to specific scoring dimensions (content, grammar, structure).


### Dashboard & Reporting: Teachers can view class statistics; students see their grades and feedback.


### Technical Stack: Python (Django/Flask for backend), NLP libraries (spaCy, NLTK), ML frameworks (scikit-learn, Transformers library for BERT/RoBERTa), Frontend (HTML, CSS, JavaScript), Database (MySQL or Firebase Firestore).


### Evaluation: Performance validation using a curated dataset of student assignments with human-graded benchmarks. Pilot testing in a controlled academic setting (e.g., within the university department).


### 1.4.2 Limitations and Delimitations:


### To ensure project feasibility within the academic timeline and available resources, the following are explicitly out of scope for the initial version (Minimum Viable Product - MVP):


### Subject and Language Limitation: The system will be designed and validated primarily for English language assignments. Support for other languages or highly domain-specific technical jargon (e.g., advanced medical or legal terminology) is not included.


### Assignment Format: The focus is on textual content. Evaluation of mathematical equations, code snippets, diagrams, hand-drawn figures, or oral presentations is beyond the system's capabilities.


### Deep Conceptual Understanding: While the system assesses semantic similarity and keyword coverage, it does not possess genuine comprehension or critical thinking. It cannot judge the philosophical depth, creative originality, or ethical reasoning in an essay at a human-expert level.


### Plagiarism Detection: Although related, a comprehensive plagiarism detection module integrating with external databases (like Turnitin) is a separate complex system and is not part of this MVP.


### Full Emotional or Stylistic Nuance: The system will not evaluate writing style, persuasiveness, humor, or emotional tone in a sophisticated manner.


### Complete Autonomy: The system is designed as an aid for teachers, not a replacement. Teachers will have the final authority to review and modify any automated score or feedback.


### Large-Scale Deployment Infrastructure: While the architecture will be cloud-ready, enterprise-level features like load balancing across multiple servers, advanced cybersecurity audits, and integration with existing Learning Management Systems (LMS) like Moodle or Canvas are considered future enhancements.


### Longitudinal Learning Analytics: Basic reporting is included, but advanced predictive analytics on student learning trajectories over time is out of scope.


### This clear scoping ensures the project is focused, achievable, and demonstrates core competencies in AI, software engineering, and user-centered design, while providing a solid foundation for future research and development.


### 1.5 Significance of the Study


### The development of the Auto Assignment Valuation System carries substantial importance across academic, pedagogical, technological, and societal dimensions.


### 1.5.1 Academic and Research Significance:


### Applied AI Research: This project represents a concrete application of advanced AI sub-fields—Natural Language Processing and Machine Learning—to a real-world problem in educational technology. It contributes to the growing body of research on Automated Essay Scoring (AES) and intelligent tutoring systems.


### Interdisciplinary Integration: It bridges computer science with education science, demonstrating how technical solutions can be designed with pedagogical principles in mind.


### Benchmark for Future Work: The system, its architecture, and validation results can serve as a benchmark or reference implementation for other researchers and students working on similar problems in automated assessment.


### 1.5.2 Pedagogical and Educational Significance:


### Reducing Administrative Burden: By automating the initial grading and feedback process, the system can free up significant time for educators, allowing them to focus on higher-value activities like interactive teaching, curriculum development, and personalized student mentoring.


### Enhancing Feedback Quality and Timeliness: Instant, consistent, and detailed automated feedback can accelerate the learning cycle, enabling students to understand and correct errors while the learning context is still fresh.


### Promoting Fairness and Consistency: An AI grader applies the same criteria uniformly to all submissions, reducing subjective bias and increasing the perceived fairness of the assessment process.


### Facilitating Differentiated Instruction: By quickly identifying common errors or misconceptions across a class (through aggregated analytics), teachers can adjust their instruction to target specific areas of need.


### 1.5.3 Technological and Practical Significance:


### Demonstration of Modern Tech Stack: The project showcases the practical integration of a modern development stack (Python, NLP libraries, Transformer models, web frameworks) to build a complex, AI-driven application.


### Scalable Solution Prototype: It provides a working prototype for a scalable assessment tool that could be adapted and deployed in various educational settings, from secondary schools to universities and corporate training.


### Open-Source Contribution Potential: The development approach and findings can be shared with the open-source community, encouraging collaboration and improvement in the field of educational AI.


## Chapter 2:


## Literature Review


### 2.1 Evolution of Educational Assessment Systems


### The history of educational assessment is a narrative of shifting paradigms, from oral examinations in ancient academies to standardized testing in the industrial age, and now toward digital and adaptive assessment in the information age. The primary driver of this evolution has been the dual need for scalability and objectivity.


### Figure 2.1: Evolution of Educational Assessment Systems


### The paper-and-pencil testing model, dominant for centuries, introduced standardization but remained labor-intensive to grade and limited in the types of skills it could assess (multiple-choice vs. constructed response).


### The advent of Computer-Based Testing (CBT) in the late 20th century marked the first major digital shift. It automated test administration and the scoring of selected-response items but left the evaluation of essays and open-ended answers untouched. This limitation spurred the initial research into Automated Essay Scoring (AES). The landmark project, Project Essay Grader (PEG)** by Ellis Page in 1966, used simple statistical models based on surface features like word length, sentence complexity, and vocabulary richness to predict human scores. While pioneering, PEG and its early successors were criticized as "bag-of-words" models that could be gamed and lacked true understanding.


### The 21st century brought the internet, cloud computing, and big data into education, leading to Learning Management Systems (LMS) like Moodle and Blackboard. These platforms digitized the entire assignment lifecycle—distribution, submission, and manual grading—but the core act of evaluation remained human. Concurrently, the field of  Educational Data Mining (EDM) and Learning Analytics (LA) emerged, focusing on extracting insights from educational data. This created a fertile ground for integrating AI into the assessment loop, not just for scoring, but for diagnostic and predictive analytics. Today, the evolution continues toward AI-Enhanced Assessment, which seeks to provide continuous, formative, and multi-modal evaluation, moving beyond summative end-of-unit tests to support the learning process itself. This historical context frames the current project as part of the ongoing quest to make assessment more intelligent, integrated, and informative.


### 2.2 Artificial Intelligence in Education (AIED)


### Artificial Intelligence in Education is a well-established interdisciplinary field that explores the application of AI techniques to solve educational problems and understand learning processes.


### Figure 2.2: Key Domains of AI in Education and the Hybrid Intelligence Model


### Burdened by administrative tasks and the challenge of personalizing instruction for diverse learners, education is a prime domain for AI augmentation. Key research areas within AIED include Intelligent Tutoring Systems (ITS), which provide customized instruction and feedback; Adaptive Learning Platforms, which adjust content difficulty based on learner performance; and Automated Assessment, which is the direct focus of this project.


### The theoretical underpinning for applying AI to assessment often draws from Cognitive Science and Learning Theories. For instance, AES systems implicitly model the cognitive processes a human grader undertakes: parsing text, identifying key concepts, evaluating argument structure, and checking for errors. Modern AIED systems also embrace Socio-Constructivist principles by aiming to provide timely feedback that scaffolds learning. However, a critical tension exists in AIED between automation and pedagogical soundness. The goal is not to replace the teacher but to create a "hybrid intelligence" system where AI handles repetitive, data-intensive tasks, and the teacher provides empathy, moral support, and high-level guidance. The Auto Assignment Valuation System is situated within this paradigm, aiming to be a teacher's aid that handles initial scoring and feedback generation, thereby enabling the teacher to engage in more meaningful pedagogical interactions.


### 2.3 Natural Language Processing (NLP) in Automated Grading


### Natural Language Processing is the cornerstone technology enabling computers to understand, interpret, and generate human language. Its application to automated grading has evolved through several technological waves:


### Figure 2.3: Evolution of NLP Techniques in Automated Grading

1.  Rule-Based and Statistical Methods (1990s-2000s): Early AES systems like PEG and its successors relied on shallow features: word count, average sentence length, vocabulary diversity, presence of prompt-specific keywords, and basic grammatical error detection using rule-based checkers. Statistical models (e.g., Linear Regression, Bayesian Networks) were trained to map these feature vectors to human scores. While faster than manual grading, these systems were brittle and easily fooled by verbose, off-topic text stuffed with keywords.

2. Machine Learning and Feature Engineering (2000s-2010s): The introduction of more sophisticated ML algorithms (Support Vector Machines, Decision Trees) allowed for better modeling. Researchers engaged in extensive feature engineering, creating hundreds of linguistic, syntactic, and semantic features. These included:


### Lexical Features: Type-token ratio, word frequency distributions.


### Syntactic Features: Parse tree depth, part-of-speech tag n-grams.


### Discourse Features: Cohesion metrics, transition word usage.


### Content-Based Features: Latent Semantic Analysis (LSA), a statistical method for representing the conceptual meaning of texts by analyzing word co-occurrence patterns. LSA was a significant step toward measuring semantic content.

3. Deep Learning and Neural Networks (2010s-Present): The deep learning revolution transformed NLP. Recurrent Neural Networks (RNNs) and Long Short-Term Memory (LSTM) networks could model word sequences and capture context better than bag-of-words models. However, the true breakthrough came with the Transformer architecture and pre-trained language models  like BERT (Bidirectional Encoder Representations from Transformers), GPT, and RoBERTa. These models, trained on massive text corpora, develop a deep, contextual understanding of language. For AES, they enable highly accurate semantic similarity scoring comparing the meaning of a student's answer to a model answer at a sophisticated level. They can also be fine-tuned for specific grading tasks, making them the current state-of-the-art foundation for projects like the one proposed here.


### 2.4 Machine Learning Approaches for Text Evaluation


### Beyond the NLP pipeline, specific machine learning paradigms are employed to synthesize various features into a final score or feedback.


### Figure 2.4: Machine Learning Approaches for Automated Text Evaluation


### Supervised Learning for Score Prediction: This is the most common approach. A dataset of student answers paired with human-assigned scores is used to train a regression model (to predict a continuous score) or a classification model (to assign a letter grade or rubric level). The model learns the complex, often non-linear, relationship between the extracted text features (from NLP) and the target score. Algorithms range from Random Forests and Gradient Boosting Machines (XGBoost) to Neural Networks. The choice depends on dataset size, interpretability needs, and performance.


### Unsupervised and Semi-Supervised Learning: In scenarios where labeled grading data is scarce, unsupervised methods like clustering can group similar-quality answers. Semi-supervised learning can leverage a small set of graded answers to label a larger ungraded set. Word Embeddings (Word2Vec, GloVe) and sentence embeddings (from BERT) are often used as feature inputs in these settings.


### Deep Learning Architectures: For end-to-end grading, specialized neural architectures are explored. These might combine a BERT layer for text encoding with a fully connected regression head for scoring. Some research uses Siamese Networks or Sentence BERTspecifically to learn a semantic space where distances between student and model answers correlate with score differences.


### Explainable AI (XAI) for Feedback: Modern ML approaches also focus on interpretability. It's not enough to give a score; the system should explain why. Techniques like LIME (Local Interpretable Model-agnostic Explanations) or SHAP (SHapley Additive exPlanations) can be used to identify which words or phrases in a student's answer most influenced the score (positively or negatively), enabling the generation of specific, data-driven feedback.


### 2.5 Existing Automated Assessment Systems


### A review of commercial and academic systems provides context for the proposed project's positioning.


### Figure 2.5: Landscape of Existing Automated Assessment Systems


### Commercial Tools:


### Turnitin's Revision Assistant and Gradescope: While Turnitin is famous for plagiarism detection, its tools have evolved. Gradescope streamlines manual grading but also uses AI for answer grouping (clustering similar answers) to speed up rubric application. It is more of a grading workflow optimizer than a fully automatic scorer for open-ended text.

ETS's e-rater: Used in the GMAT and TOEFL exams, e-rater is one of the most established commercial AES engines. It analyzes grammar, usage, mechanics, style, organization, and development. It represents the culmination of decades of rule-based and statistical ML research.


### Pearson's Intelligent Essay Assessor (IEA): Uses Latent Semantic Analysis (LSA) to measure content quality and has been integrated into various educational products.


### Academic and Open-Source Projects:


### Moodle's Essay Autograde Plugin: A simple plugin that uses keyword matching, serving as a basic example but lacking semantic understanding.


### Research Prototypes (e.g., Sherlock): Numerous university research projects have built AES systems. For example, some use LSTM networks to model essay coherence or BERT for content scoring. These often publish their methodologies and sometimes their code, providing valuable blueprints.


### Critical Analysis: Commercial systems are often "black boxes" with proprietary algorithms, making them difficult to study, customize, or integrate into novel workflows for research purposes. They are also typically expensive. Academic prototypes demonstrate advanced techniques but may lack the polish, user interface, and robust architecture needed for real-world classroom use. The gap, therefore, lies in developing an open, transparent, and end-to-end system that leverages the latest AI techniques (like transformers) while being built with a user-centered design, accessible for academic study and capable of being deployed in a practical setting. This is precisely the niche the Auto Assignment Valuation System aims to fill.


### 2.6 Text Similarity and Semantic Analysis Techniques


### At the heart of content-based auto-grading is the ability to measure how similar a student's answer is to a reference answer or a set of key concepts. This has evolved from simple lexical overlap to deep semantic matching.


### Figure 2.6: Hierarchy of Text Similarity and Semantic Analysis Techniques

1.  Lexical Methods:

n-gram Overlap: Measures the overlap of word sequences (unigrams, bigrams) between texts. Simple but ignores synonyms and word order.

TF-IDF (Term Frequency-Inverse Document Frequency) with Cosine Similarity: Represents texts as vectors weighted by word importance. Better than raw overlap but still lexical.

2.  Statistical Semantic Methods:


### Latent Semantic Analysis (LSA):Uses Singular Value Decomposition (SVD) on a term-document matrix to project texts into a lower-dimensional "concept" space. Similarity is the cosine of the angle between concept vectors. It can capture synonymy to some extent but is based on co-occurrence statistics from a training corpus.

3.  Word Embedding-Based Methods:


### Word2Vec/GloVe Vector Averaging: Represents each word by a dense vector (embedding) capturing its meaning. A document's vector is the average of its word vectors. Similarity is computed between document vectors. This captures semantic relationships between words better than TF-IDF.

4.  Deep Semantic Methods (State-of-the-Art):


### Sentence Embeddings with BERT/RoBERTa: This is the current gold standard. Models like Sentence-BERT (SBERT) are fine-tuned specifically to produce semantically meaningful sentence embeddings. The similarity between two sentences is computed as the cosine similarity between their SBERT embeddings. This method excels because it understands context (e.g., "bank" in "river bank" vs. "money bank") and captures complex paraphrasing.


### Cross-Encoders: While SBERT is efficient for comparing many sentences, a BERT cross-encoder (which processes the student and model answer together as input) can often provide even more accurate similarity scores for pairwise comparison, though it is computationally heavier.


### For the Auto Assignment Valuation System, employing Sentence-BERT for semantic similarity scoring is a recommended, modern approach that balances high accuracy with reasonable computational requirements for a web application.


### 2.7 Educational Data Mining and Learning Analytics


### Automated assessment systems are potent generators of structured educational data. Every submission, score, and generated feedback point becomes a data point. This aligns the project closely with the fields of Educational Data Mining (EDM) and Learning Analytics (LA)

`


### Figure 2.7: Data Pipeline from Automated Assessment to Learning Analytics


### EDM focuses on developing methods for exploring data from educational settings to understand students and their learning environments. An auto-grading system can feed into EDM by providing clean, structured data on student performance at a granular level (per question, per concept).


### LA is the measurement, collection, analysis, and reporting of this data about learners and their contexts, for purposes of understanding and optimizing learning. The dashboard component of the proposed system is a basic LA tool. It can show teachers:


### Class-wide performance distributions.


### Common error hotspots (e.g., which grammar rule is most frequently broken, which concept is most misunderstood).


### Individual student progress over time.


### This capability transforms assessment from a purely summative judgment into a formative diagnostic tool. The system doesn't just assign a grade; it helps identify why a class or student is struggling, enabling targeted intervention. This is a powerful value-add that moves the project beyond mere automation toward learning enhancement.


### 2.8 Trust, Fairness, and Bias in AI-Based Assessment


### The deployment of AI in high-stakes assessment raises serious ethical and practical concerns that must be addressed in the system's design.


### Figure 2.8: Ethical Challenges and Mitigation Strategies in AI-Based Assessment


### Algorithmic Bias: If the training data for the ML models is biased (e.g., over-representing answers from a particular demographic or writing style), the system may perpetuate or even amplify these biases, unfairly penalizing certain groups of students. Mitigation strategies include using diverse, representative training data, applying bias detection and correction algorithms, and ensuring transparency.


### Lack of Transparency ("Black Box"): Many advanced ML models, especially deep neural networks, are difficult to interpret. A student who receives a low score deserves to know why. Integrating Explainable AI (XAI)  techniques, as mentioned earlier, is crucial for building trust.


### Gaming the System: Students may try to trick the AI by using complex vocabulary incorrectly, repeating key phrases, or employing other strategies learned from "Adversarial Attacks" on NLP models. Robust system design involves using multiple, complementary features (not just keywords) and potentially including mechanisms to detect nonsensical or off-topic text.


### Teacher-in-the-Loop: The most critical design principle for fairness is to not treat the AI score as final. The system must be designed as an assistant, with an easy and clear workflow for teachers to review, modify, or reject any automated grade. This human oversight is the ultimate safeguard.


### 2.9  Research Gap and Contribution


### Figure 2.10: Synthesis of Research Gaps and Project ContributionFigure 2.10: Synthesis of Research Gaps and Project ContributionSynthesizing the literature reveals a clear, multi-dimensional gap that this project aims to addres:


### Figure 2.10: Synthesis of Research Gaps and Project Contribution


### Figure 2.10: Synthesis of Research Gaps and Project Contribution

1.  Technology-Application Gap: While state-of-the-art NLP models (BERT, etc.) exist, their integration into a complete, usable, and open educational application designed for real classroom contexts is not commonplace. Many advanced models remain in research papers or Jupyter notebooks.

2.  Accessibility Gap: Commercial solutions are closed and expensive. There is a need for a system whose architecture, methodology, and (potentially) code are transparent and accessible for academic scrutiny, adaptation, and use in resource-constrained settings.

3.  Design Gap: Many systems focus purely on the scoring algorithm. A holistic system that thoughtfully integrates the AI engine with teacher and student dashboards, a feedback generation mechanism, and a practical workflow that respects the teacher's ultimate authority is needed.

4.  SDG-Alignment Gap: Few student-level projects explicitly design, develop, and articulate their work's contribution to the Sustainable Development Goals.


### Therefore, the novel contribution of this project is: The development of a fully-functional, open-architecture, AI-powered assignment valuation system that not only implements modern transformer-based NLP for grading but also embeds this technology within a user-centered web application designed to support pedagogical workflows, with explicit design considerations for fairness and a clear alignment with SDGs 4 and 9.


## References


### Attali, Y., & Burstein, J. (2006). Automated essay scoring with e-rater® V.2. The Journal of Technology, Learning and Assessment, 4(3), 1–30.


### Baker, R. S., & Inventado, P. S. (2014). Educational data mining and learning analytics. In J. A. Larusson & B. White (Eds.), Learning analytics: From research to practice (pp. 61–75). Springer.


### Bridgeman, B., Trapani, C., & Attali, Y. (2012). Comparison of human and machine scoring of essays: Differences by gender, ethnicity, and country. Applied Measurement in Education, 25(1), 27–40


### Brown, T., Mann, B., Ryder, N., Subbiah, M., Kaplan, J. D., Dhariwal, P., ... & Amodei, D. (2020). Language models are few-shot learners. Advances in Neural Information Processing Systems, 33, 1877–1901.


### Chung, G. K. W. K., & Baker, E. L. (2003). An exploratory study to examine the feasibility of measuring problem-solving processes using a click-through interface. Journal of Technology, Learning, and Assessment, 2(2), 1–31.


### Devlin, J., Chang, M. W., Lee, K., & Toutanova, K. (2019). BERT: Pre-training of deep bidirectional transformers for language understanding. Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long and Short Papers), 4171–4186.


### Gikandi, J. W., Morrow, D., & Davis, N. E. (2011). Online formative assessment in higher education: A review of the literature. Computers & Education, 57(4), 2333–2351.


### Hattie, J., & Timperley, H. (2007). The power of feedback. Review of Educational Research, 77(1), 81–112.


### Hochreiter, S., & Schmidhuber, J. (1997). Long short-term memory. Neural Computation, 9(8), 1735–1780.


### Kaplan, A., & Haenlein, M. (2019). Siri, Siri, in my hand: Who's the fairest in the land? On the interpretations, illustrations, and implications of artificial intelligence. Business Horizons, 62(1), 15–25.


### Knight, S., & Buckingham Shum, S. (2017). Theory and learning analytics. In C. Lang, G. Siemens, A. Wise, & D. Gašević (Eds.), Handbook of learning analytics (pp. 17–22). Society for Learning Analytics Research.


### Koedinger, K. R., & Aleven, V. (2016). An unfolding story: A review of the Handbook of Research on Learning and Instruction (2nd ed.). Educational Researcher, 45(1), 47–49.


### Landauer, T. K., Foltz, P. W., & Laham, D. (1998). An introduction to latent semantic analysis. Discourse Processes, 25(2-3), 259–284.

Liu, O. L., Brew, C., Blackmore, J., Gerard, L., Madhok, J., & Linn, M. C. (2014). Automated scoring of constructed-response science items: Prospects and obstacles. Educational Measurement: Issues and Practice, 33(2), 19–28.


### Lundberg, S. M., & Lee, S. I. (2017). A unified approach to interpreting model predictions. Advances in Neural Information Processing Systems, 30, 4765–4774.


### McNamara, D. S., Crossley, S. A., & Roscoe, R. (2013). Natural language processing in an intelligent writing strategy tutoring system. Behavior Research Methods, 45(2), 499–515.


### Merrill, M. D. (2002). First principles of instruction. Educational Technology Research and Development, 50(3), 43–59.


### Mikolov, T., Chen, K., Corrado, G., & Dean, J. (2013). Efficient estimation of word representations in vector space. arXiv preprint arXiv:1301.3781.


### Pennington, J., Socher, R., & Manning, C. D. (2014). GloVe: Global vectors for word representation. Proceedings of the 2014 Conference on Empirical Methods in Natural Language Processing (EMNLP), 1532–1543.


### Ramesh, D., & Sanampudi, S. K. (2022). An automated essay scoring systems: A systematic literature review. Artificial Intelligence Review, 55(3), 2495–2527.


### Reimers, N., & Gurevych, I. (2019). Sentence-BERT: Sentence embeddings using Siamese BERT-networks. *Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP)*, 3982–3992.


### Ribeiro, M. T., Singh, S., & Guestrin, C. (2016). "Why should I trust you?" Explaining the predictions of any classifier. Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, 1135–1144.


### Romero, C., & Ventura, S. (2020). Educational data mining and learning analytics: An updated survey. Wiley Interdisciplinary Reviews: Data Mining and Knowledge Discovery, 10(3), e1355.


### Shermis, M. D., & Burstein, J. (Eds.). (2013). Handbook of automated essay evaluation: Current applications and new directions. Routledge.


### Shute, V. J. (2008). Focus on formative feedback. Review of Educational Research, 78(1), 153–189.


### Siemens, G., & Long, P. (2011). Penetrating the fog: Analytics in learning and education. EDUCAUSE Review, 46(5), 30–32.


### United Nations. (2015). Transforming our world: The 2030 agenda for sustainable development. United Nations Department of Economic and Social Affairs.


### Wang, Y., & Heffernan, N. T. (2013). The student skill model. In R. Azevedo & V. Aleven (Eds.), International handbook of metacognition and learning technologies (pp. 367–382). Springer.


### Wiliam, D. (2011). What is assessment for learning? Studies in Educational Evaluation, 37(1), 3–14


### Wolf, M. K., & Leon, S. (2009). An investigation of the language demands in content assessments for English language learners. Educational Assessment, 14(3-4), 139–159.


### Woolf, B. P. (2010). Building intelligent interactive tutors: Student-centered strategies for revolutionizing e-learning. Morgan Kaufmann.


### Zawacki-Richter, O., Marín, V. I., Bond, M., & Gouverneur, F. (2019). Systematic review of research on artificial intelligence applications in higher education – where are the educators? International Journal of Educational Technology in Higher Education, 16(1), 1–27.


### Zhai, X., & Nehm, R. H. (2023). AI and formative assessment: The train has left the station. Journal of Research in Science Teaching, 60(6), 1390–1398.
