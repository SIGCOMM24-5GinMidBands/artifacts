
## Unveiling the 5G Mid-Band Landscape: From Network Deployment to Performance and Application QoE

In this repository, we release the dataset and artifacts of the conference paper 
[Unveiling the 5G Mid-Band Landscape: From Network Deployment to Performance and Application QoE](https://github.com/SIGCOMM24-5GinMidBands/artifacts/blob/main/5G_EU_US_Configuration_Comparative_Study.pdf) published at [SIGCOMM 2024](https://conferences.sigcomm.org/sigcomm/2024/). 

This is a measurement paper with various types of data processed for different purposes having different methodologies. In out GitHub,
we group the artifacts by Section number and name. There are README files with each Section folder with more specific
instructions to validate our experimental results. Lastly, here are some generic principles we followed for releasing the artifacts:

---

### Abstract  
> 5G in mid-bands has become the dominant deployment of choice in the world. We present – to the best of our knowledge – the first 
> comprehensive and comparative cross-country measurement study 
> of commercial mid-band 5G deployments in Europe and the U.S., 
> filling a gap in the existing 5G measurement studies. We unveil the 
> key 5G mid-band channels and configuration parameters used by 
> various operators in these countries, and identify the major factors 
> that impact the observed 5G performance both from the network 
> (physical layer) perspective as well as the application perspective. 
> We characterize and compare 5G mid-band throughput and latency 
> performance by dissecting the 5G configurations, lower-layer parameters
> as well as deployment settings. By cross-correlating 5G parameters with the application decision process, we demonstrate how 
> 5G parameters affect application QoE metrics and suggest a simple 
> approach for QoE enhancement. Our study sheds light on how to 
> better configure and optimize 5G mid-band networks, and provides 
> guidance to users and application developers on operator choices 
> and application QoE tuning. We released the datasets and artifacts 
> at https://github.com/SIGCOMM24-5GinMidBands/artifacts.

---

### Dataset Sizes/Data Analysis
- We included the curated dataset file in this repository.
- If the dataset files are huge, we use a small sample of the dataset in the repository to demonstrate the functionality/correctness.
- If data analysis is involved, our instructions will contain information on how to process the data.
- No matter what the dataset size is, we provide the fully generated results and/or plots. If you decide to run the analysis
and/or plotting scripts, the outcome of processing will create
the raw results files in the repository. Artifacts and Info

### NOTE: We ONLY include the curated dataset in this repo. If you are interested in the raw data, please contact us. 

---


### Paper Structure to Folder Structure
 
  

|                Content in Paper                |                                                    Folder in Repo.                                                     | Section Description                                                                          |
|:----------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------:|----------------------------------------------------------------------------------------------|
|          Section 4.1 (Figures 1 - 8)           | [EU vs. US Phy DL Tput](https://github.umn.edu/fezeu001/5G-Mid-Band/blob/main/Sec4-Mid-Band-PhyPerformance/README.md)  | PHY DL Throughput Performance.                                                               |
|         Section 4.2 (Figures 9 and 10)         | [EU vs. US Phy UL Tput](https://github.umn.edu/fezeu001/5G-Mid-Band/blob/main/Sec4-Mid-Band-PhyPerformance/README.md)  | PHY UL Throughput Performance.                                                               |
|            Section 4.3 (Figure 11)             |   [Phy Layer Latency](https://github.umn.edu/fezeu001/5G-Mid-Band/blob/main/Sec4-Mid-Band-PhyPerformance/README.md)    | PHY Latency Performance.                                                                     |
|       Section 5 (Figure 12, 13, and 14)        | [Scaled Channel Variability](https://github.umn.edu/fezeu001/5G-Mid-Band/blob/main/Sec5-Channel-Variability/README.md) | 5G Mid-Band Channel Variability.                                                             |
|       Section 6 (Figure 15, 16, and 17)        |      [Mid-Band QoE](https://github.umn.edu/fezeu001/5G-Mid-Band/blob/main/Sec6-Mid-Band-VideoSteaming/README.md)       | Video Streaming Over 5G Mid-Band.                                                            |
|          Section 7 (Figure 18 and 19)          |     [Mid-band vs. mmWave](https://github.umn.edu/fezeu001/5G-Mid-Band/blob/main/Sec7-MidBand-vs-mmWave/README.md)      | 5G Mid-Band vs. 5G mmWave Channel Variability.                                               |
---

### Instructions on how to validate these artifacts
1. Clone this repo: ``git clone``
2. Run ``chmod +x setup-venv.sh``
3. Run ``./setup-venv.sh``
4. Run ``source /venv/bin/activate``
5. Run ``pip install -r requirements.txt --break-system-packages``
6. Navigate to each Section folder and follow the README file

NOTE: \
If ``SHOW_PLOT_FLAG = True``, the figure will be display\
If ``SHOW_PLOT_FLAG = False``, the figure will be saved in ``Finals_Plots`` folder in the parent directory.

---

As always, if there are any questions, feel free to reach out to us [Rostand A. K. Fezeu](mailto:fezeu001@umn.edu?cc=claudio.fiandrino@imdea.org&cc=eman@cs.umn.edu&bcc=zhang089@umn.edu&subject=[5G-Mid-Band]%SIGCOMM'24%Paper).
