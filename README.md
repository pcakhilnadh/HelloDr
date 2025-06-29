# HelloDr - Homeopathic Medicine Recommendation System

## Overview
This GitHub project scrapes homoeopathic medicine data from online sources to create a structured dataset containing details like medicine names, symptoms, uses, potencies, etc. The dataset is designed for machine learning applications such as symptom-based recommendations, pattern analysis, and knowledge discovery in homoeopathy.

The core focus of the project is building and serving a machine learning model via an API that suggests suitable homoeopathic medicines based on plain English symptom descriptions.

## Key Features
- 🌐 **Web Scraping**: Automated data collection from homeopathic medicine sources
- 📊 **Data Structuring**: Clean, organized dataset with medicine details and symptom mappings
- 🤖 **ML Recommendations**: Intelligent symptom-based medicine suggestions
- 🔍 **Pattern Analysis**: Discovery of relationships between symptoms and treatments
- 🚀 **API Service**: RESTful API for real-time medicine recommendations
- 📝 **Natural Language Processing**: Plain English symptom input processing

## Project Structure

```
HelloDr/
├── data/                          # Homeopathic medicine data storage
│   ├── raw/                       # Scraped medicine data (JSON, CSV)
│   ├── interim/                   # Cleaned and structured data
│   ├── processed/                 # Final medicine-symptom datasets
│   └── external/                  # Additional homeopathic references
├── notebooks/                     # Analysis and model development
│   ├── exploratory/              # Medicine-symptom pattern analysis
│   ├── modeling/                 # Recommendation model development
│   └── rag/                      # Semantic symptom matching
├── src/                          # Core application code
│   ├── data/                     # Data loading and processing
│   ├── features/                 # Symptom and medicine feature engineering
│   ├── models/                   # ML recommendation models
│   ├── rag/                      # Semantic search implementation
│   └── utils/                    # Helper functions and NLP utilities
├── models/                       # Trained recommendation models
├── reports/                      # Analysis and model performance reports
│   ├── figures/                  # Medicine pattern visualizations
│   └── documents/                # Research findings and model docs
├── config/                       # Configuration for scrapers and models
├── tests/                        # Unit tests for scrapers and models
├── scripts/                      # Web scraping and automation scripts
└── requirements.txt              # Python dependencies
```

## Getting Started

### 1. Environment Setup
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Data Exploration
- Place your raw dataset in `data/raw/`
- Start with notebooks in `notebooks/exploratory/` for initial data analysis
- Use the data exploration template to understand your data structure

### 3. Development Path Selection
After data exploration, choose your approach:
- **Traditional ML**: Use `notebooks/modeling/` for symptom-medicine classification models
- **RAG Application**: Use `notebooks/rag/` for semantic symptom matching and knowledge retrieval
- **Hybrid Approach**: Combine ML classification with semantic search for enhanced recommendations

## Expected Data Structure
The scraped and processed data will include:
- **Medicine Details**: Names, potencies, forms (tablets, drops, etc.)
- **Symptom Mappings**: Detailed symptom descriptions and associated medicines
- **Usage Instructions**: Dosage, frequency, and administration guidelines
- **Therapeutic Categories**: Body systems, conditions, and treatment areas
- **Source Metadata**: Data provenance and confidence scores

## API Endpoints (Planned)
- `POST /recommend` - Get medicine recommendations from symptom descriptions
- `GET /medicines` - List all available medicines with details
- `GET /symptoms` - Search symptoms and associated treatments
- `GET /medicine/{id}` - Detailed medicine information
- `POST /feedback` - Submit recommendation feedback for model improvement

## Technical Capabilities
- 📊 Comprehensive data exploration and medicine-symptom analysis
- 🕷️ Web scraping pipeline for homeopathic data collection
- 🤖 ML model development for symptom-based recommendations
- 🧠 RAG support for semantic symptom matching
- 📈 Automated reporting and treatment pattern visualization
- 🧪 Testing framework for model validation
- 🔧 Configurable parameters for different homeopathic sources

## Next Steps
1. Install dependencies: `pip install -r requirements.txt`
2. **Web Scraping**: Implement scrapers in `scripts/` to collect homeopathic medicine data
3. **Data Processing**: Add scraped data to `data/raw/` and clean it in `data/processed/`
4. **Exploration**: Run the data exploration notebook to analyze medicine-symptom relationships
5. **Model Development**: Build recommendation models based on exploration insights
6. **API Development**: Create API endpoints for real-time medicine recommendations
7. **Testing**: Validate model accuracy with known symptom-medicine pairs

## Contributing
- Follow the established folder structure
- Document your code and notebooks
- Add tests for new functionality
- Update this README as the project evolves 