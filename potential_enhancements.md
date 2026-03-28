# Documentation Enhancement Recommendations

This document identifies specific locations in the SafeSurf documentation where additional content, technical diagrams, or visual assets could significantly improve the academic quality and clarity of the report.

## Chapter 3: System Analysis & Requirement Analysis
- **Sequence Diagram**: 
  - *Location*: After section 3.2.
  - *Description*: A diagram showing the chronological flow of a URL request from the **Chrome Extension** to the **FastAPI Backend**, through the **DNS Guard**, into **Feature Extraction**, and finally receiving the **ML Ensemble Verdict**.
- **Use Case Diagram**:
  - *Location*: Near the beginning of the chapter.
  - *Description*: Visualizing the interaction between the 'User' and the 'System' (e.g., Analyzing URL, Viewing Metrics, Receiving Alerts).

## Chapter 4: System Design
- **Data Flow Diagram (DFD) Level 1**:
  - *Location*: After the System Architecture diagram.
  - *Description*: Detailed flow of data showing how the URL string is transformed into a 111-feature vector and a Bag-of-Words matrix.
- **Database/Storage Schema**:
  - *Location*: Section 4.5.
  - *Description*: Even if a traditional DB isn't used, a diagram showing the **LRU Cache** (TTL Bucket) structure or the **Model Serialization (.pkl)** storage relationship would be beneficial.

## Chapter 5: Implementation
- **Project Structure Tree**:
  - *Location*: Section 5.1.
  - *Description*: A visual folder structure of the backend (FastAPI) and frontend (React) to show modularity.
- **Chrome Extension Architecture**:
  - *Location*: Section 5.3.
  - *Description*: A small diagram explaining the relationship between `manifest.json`, the `background script`, and the `content script` for real-time monitoring.
- **Hyperparameter Table**:
  - *Location*: Section 5.5.
  - *Description*: A table listing the finalized XGBoost hyperparameters (e.g., `learning_rate: 0.1`, `max_depth: 6`, `n_estimators: 100`) used to achieve the 97.35% accuracy.

## Chapter 6: Testing
- **Integration Test Trace**:
  - *Location*: Section 6.4.
  - *Description*: A screenshot or table showing a series of 10-20 URLs being processed in a batch, demonstrating system stability under load.
- **Component Test Table**:
  - *Location*: Section 6.2.
  - *Description*: Break down the "Pass/Fail" status of individual modules like the `DnsGuardService` or `EnsembleFusionService`.

## Chapter 7: Result Analysis
- **Feature Importance Plot**:
  - *Location*: Section 7.2.
  - *Description*: A bar chart showing the **Top 10 Most Influential Features** (e.g., URL length, Dots count, Domain Age) as determined by the XGBoost gain metric.
- **Performance Comparison Table**:
  - *Location*: Section 7.4.
  - *Description*: A table comparing SafeSurf's results (Accuracy: 97.35%, F1: 96.65%) against standard baseline models or similar academic papers.
- **Inference Latency Breakdown**:
  - *Location*: Section 7.3.
  - *Description*: A pie chart or bar chart showing the time spent in:
    1. Lexical Extraction (<5ms)
    2. Infrastructure Queries (200-400ms)
    3. Model Prediction (<50ms)

## Visual Design Tips
> [!TIP]
> **Consistency**: Ensure all diagrams use the same color palette as the rest of the document (e.g., using the `collegeblue` and `namegreen` defined in `main.tex`).
> 
> **Captions**: Use descriptive captions that explicitly link the figure to the text analysis.
