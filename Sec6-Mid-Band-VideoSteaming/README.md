## Sec. 6 Video Streaming over 5G Mid-Band
___

### Key Insight or Takeaway
> The (aggregate) 5G PHY throughput strongly contributes to the (average) bitrate
> attained by video ABR algorithms, whereas channel variability
> greatly affects video stall time performance. Based on this, we
> suggest a using smaller chunks sizes for better channel variability
> adaptation to improve video streaming QoE performance over 5G Mid-Band.

### Results Summary

1. Figure 15: Using six representative traces using Vodafone from Italy (V_It), and 
Orange Spain (O_Sp), we analyzed the average QoE in terms of average
bitrate and stall time (in ms). 

2. Figure 16: We Further visually demonstrate how the 5G PHY throughput and channel variability
directly affect the video streaming QoE (particularly the stall time) and the ABR decision process. 

3. Figure 17: Shows a simple application level adaptation to enhance video streaming QoE given the insights 
about channel variability and their impact on the ABR decision making process. 

### Generating plot
In the project terminal, navigate to this folder and run:

1. Figure 15: ```jupyter notebook fig15.ipynb ```
2. Figure 16: ```jupyter notebook fig16.ipynb ```
3. Figure 17: ```jupyter notebook fig17.ipynb ```

Then run the ``>>`` to _'Restart the kernel and run all cells'_

---