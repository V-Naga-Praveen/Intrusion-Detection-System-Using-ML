# Intrusion-Detection-System-Using-ML
Intrusion Detection System (IDS) Using Advanced Machine Learning Techniques(MTH framework)
1. Purpose
The purpose of this project is to develop a sophisticated Intrusion Detection System (IDS) that leverages advanced machine learning techniques to accurately detect and classify signature-based cyber-attacks. By employing a Multi-Threaded Hybrid (MTH) framework and optimizing model performance through Bayesian Optimization with a Tree-based Parzen Estimator (BO-TPE), the project aims to enhance the reliability and effectiveness of cybersecurity measures. The inclusion of a user-friendly graphical interface built with Tkinter ensures practical usability, allowing for efficient processing of input attributes and precise attack identification.

2. Scope of Project
The scope of this project includes:

Developing a comprehensive IDS focused on detecting signature-based attacks.
Implementing and ensembling machine learning models like Random Forest, Extra Trees, XGBoost, and Decision Tree.
Training and validating models using the CICIDS2017 dataset.
Performing hyperparameter tuning using Bayesian Optimization with a Tree-based Parzen Estimator (BO-TPE).
Creating a user-friendly graphical interface with Tkinter to process 77 input attributes for accurate attack identification.
Excluding the detection of anomaly-based attacks and alarm generation functionalities.
3. Project Features
3.1 Multi-Tiered Hybrid Framework
Utilizes a comprehensive MTH framework to develop and ensemble multiple machine learning models for effective intrusion detection.
3.2 Ensemble Learning
Incorporates diverse machine learning algorithms including Random Forest, Extra Trees, XGBoost, and Decision Tree for enhanced detection of signature-based attacks.
3.3 Hyperparameter Optimization
Implements Bayesian Optimization with a Tree-based Parzen Estimator (BO-TPE) to fine-tune model parameters.
3.4 Graphical User Interface (GUI)
Develops a user-friendly GUI using Tkinter, facilitating easy input of 77 attributes and providing clear output regarding detected attack types.
3.5 Focused Approach
Concentrates solely on signature-based attack detection, excluding anomaly-based attacks, to provide precise and efficient cybersecurity measures.
3.6 Dataset Utilization
Leverages the CICIDS2017 dataset for training and validation, ensuring robustness and reliability in detecting known signature-based attacks.
4. Proposed System
The proposed intrusion detection system revolutionizes threat detection by leveraging advanced machine learning techniques. Unlike conventional signature-based systems, this approach emphasizes the utilization of ensemble learning models, including Random Forest, Extra Trees, XGBoost, and Decision Tree. Trained on a comprehensive dataset, these models can detect known attacks with higher accuracy while also adapting to novel threats.

Key to this system is the integration of Bayesian Optimization with a Tree-based Parzen Estimator (BO-TPE) for hyperparameter tuning. This optimization technique enhances model performance by fine-tuning parameters, improving their ability to distinguish between genuine threats and benign network traffic.

Additionally, the system features a user-friendly graphical interface developed using Tkinter, enabling users to input network traffic attributes and receive real-time feedback on detected attacks. Focusing on accurate detection of known signature-based attacks and providing a seamless user experience, this system aims to significantly enhance cybersecurity measures in modern networks.

5. Technologies Used
The project incorporates a blend of cutting-edge technologies to deliver an efficient and robust intrusion detection system:

5.1 Machine Learning Models
Random Forest, Extra Trees, XGBoost, Decision Tree: These models form the backbone of the intrusion detection system, leveraging ensemble learning techniques to enhance detection accuracy.
5.2 Bayesian Optimization with Tree-based Parzen Estimator (BO-TPE)
This optimization technique plays a crucial role in fine-tuning the hyperparameters of the machine learning models.
5.3 Tkinter (GUI Development)
Tkinter is utilized to create an intuitive graphical user interface (GUI) for the intrusion detection system.
5.4 Python Programming Language
Python serves as the primary programming language for implementing various components of the system.
5.5 CICIDS2017 Dataset
The project relies on the CICIDS2017 dataset for training and validation purposes.
6. Project Structure
ids-code.ipynb: Jupyter notebook containing the project code.
gui-code.ipynb: Jupyter notebook containing the GUI code.
joblib files: Contains the 6 pre-trained model files.
dataset: Contains the CICIDS2017 dataset.
7. Usage
Clone the repository:

sh
Copy code
git clone https://github.com/yourusername/your-repository.git
cd your-repository
Install the required dependencies:

sh
Copy code
pip install -r requirements.txt
Run the Jupyter notebooks:
Open ids-code.ipynb and gui-code.ipynb in Jupyter Notebook and run the cells to execute the project code and the GUI.

8. Contact
For any questions or further information, please contact [vajjanagapraveen@gmail.com].
