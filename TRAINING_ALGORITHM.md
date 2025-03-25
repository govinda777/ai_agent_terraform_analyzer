# Algoritmos de Aprendizado de Máquina

A seguir, apresento uma série de exemplos de algoritmos de aprendizado de máquina – do básico ao avançado – representados por diagramas de classes em Mermaid. Cada exemplo ilustra, de forma simplificada, como os componentes (classes) interagem para formar o pipeline ou a estrutura interna do algoritmo.

---

### 1. Regressão Linear (Básico)
**Contexto:** Previsão de preços de casas usando uma relação linear entre as variáveis.

```mermaid
classDiagram
    class Dataset {
      +loadData()
      +splitData()
    }
    class Preprocessor {
      +cleanData()
      +normalizeData()
    }
    class LinearRegression {
      +train()
      +predict()
      -weights: float[]
    }
    class Evaluator {
      +calculateMSE()
    }
    Dataset --> Preprocessor : "prepara"
    Preprocessor --> LinearRegression : "treina"
    LinearRegression --> Evaluator : "avalia"
```

---

### 2. Regressão Logística (Básico/Intermediário)
**Contexto:** Classificação de emails como spam ou não, com base em uma função logística.

```mermaid
classDiagram
    class Dataset {
      +loadData()
      +splitData()
    }
    class Preprocessor {
      +cleanData()
      +tokenize()
    }
    class LogisticRegression {
      +train()
      +predictProbability()
      -weights: float[]
    }
    class Evaluator {
      +calculateAccuracy()
      +plotROC()
    }
    Dataset --> Preprocessor : "prepara"
    Preprocessor --> LogisticRegression : "treina"
    LogisticRegression --> Evaluator : "avalia"
```

---

### 3. Árvore de Decisão (Intermediário)
**Contexto:** Aprovação de empréstimos com base em critérios como renda e histórico de crédito.

```mermaid
classDiagram
    class Dataset {
      +loadData()
      +splitData()
    }
    class Preprocessor {
      +cleanData()
    }
    class DecisionTree {
      +buildTree()
      +predict()
      -root: TreeNode
    }
    class TreeNode {
      +splitCriterion
      +left: TreeNode
      +right: TreeNode
    }
    class Evaluator {
      +calculateGini()
      +calculateEntropy()
    }
    Dataset --> Preprocessor : "prepara"
    Preprocessor --> DecisionTree : "treina"
    DecisionTree --> TreeNode : "compõe"
    DecisionTree --> Evaluator : "avalia"
```

---

### 4. k-Nearest Neighbors (KNN) (Intermediário)
**Contexto:** Classificação de flores em espécies (ex.: conjunto Iris) com base na similaridade entre as instâncias.

```mermaid
classDiagram
    class Dataset {
      +loadData()
      +splitData()
    }
    class Preprocessor {
      +cleanData()
      +normalizeData()
    }
    class DistanceCalculator {
      +calculateEuclideanDistance(a, b)
    }
    class KNN {
      +k: int
      +predict()
    }
    class Evaluator {
      +calculateAccuracy()
    }
    Dataset --> Preprocessor : "prepara"
    Preprocessor --> KNN : "alimenta"
    KNN --> DistanceCalculator : "usa"
    KNN --> Evaluator : "avalia"
```

---

### 5. Máquina de Vetores de Suporte (SVM) (Intermediário/Avançado)
**Contexto:** Reconhecimento de dígitos manuscritos com a utilização de kernels para encontrar o hiperplano ótimo.

```mermaid
classDiagram
    class Dataset {
      +loadData()
      +splitData()
    }
    class Preprocessor {
      +cleanData()
      +scaleFeatures()
    }
    class SVM {
      +kernel: Kernel
      +train()
      +predict()
      -supportVectors: float[][]
    }
    class Kernel {
      <<interface>>
      +compute(x, y)
    }
    class LinearKernel {
      +compute(x, y)
    }
    class RBFKernel {
      +compute(x, y)
    }
    class Evaluator {
      +calculateMargin()
      +calculateAccuracy()
    }
    Dataset --> Preprocessor : "prepara"
    Preprocessor --> SVM : "treina"
    SVM --> Kernel : "usa"
    Kernel <|-- LinearKernel
    Kernel <|-- RBFKernel
    SVM --> Evaluator : "avalia"
```

---

### 6. Random Forest (Avançado)
**Contexto:** Diagnóstico médico utilizando o ensemble de múltiplas árvores de decisão para maior robustez.

```mermaid
classDiagram
    class Dataset {
      +loadData()
      +splitData()
    }
    class Preprocessor {
      +cleanData()
    }
    class DecisionTree {
      +buildTree()
      +predict()
    }
    class RandomForest {
      +numTrees: int
      +trees: DecisionTree[]
      +train()
      +predict()
    }
    class Evaluator {
      +calculateAccuracy()
      +plotROC()
    }
    Dataset --> Preprocessor : "prepara"
    Preprocessor --> RandomForest : "treina"
    RandomForest --> DecisionTree : "compõe (ensemble de)"
    RandomForest --> Evaluator : "avalia"
```

---

### 7. Redes Neurais Artificiais (Avançado)
**Contexto:** Reconhecimento de padrões em imagens ou outros dados por meio de múltiplas camadas de processamento.

```mermaid
classDiagram
    class Dataset {
      +loadData()
      +splitData()
    }
    class Preprocessor {
      +cleanData()
      +normalizeData()
    }
    class NeuralNetwork {
      +layers: Layer[]
      +train()
      +predict()
    }
    class Layer {
      +neurons: Neuron[]
      +forward(input)
    }
    class Neuron {
      +weights: float[]
      +activate()
    }
    class Optimizer {
      +updateWeights(network: NeuralNetwork)
    }
    class Evaluator {
      +calculateLoss()
      +calculateAccuracy()
    }
    Dataset --> Preprocessor : "prepara"
    Preprocessor --> NeuralNetwork : "treina"
    NeuralNetwork --> Layer : "compõe"
    Layer --> Neuron : "contém"
    NeuralNetwork --> Optimizer : "otimiza"
    NeuralNetwork --> Evaluator : "avalia"
```

---

### 8. Redes Neurais Convolucionais (CNN) (Muito Avançado)
**Contexto:** Identificação de objetos em imagens utilizando camadas especializadas para extração e redução de características.

```mermaid
classDiagram
    class Dataset {
      +loadImages()
      +splitData()
    }
    class Preprocessor {
      +resizeImages()
      +normalizeImages()
    }
    class ConvolutionalLayer {
      +filters: float[][][]
      +applyConvolution(input)
    }
    class PoolingLayer {
      +applyPooling(input)
    }
    class FullyConnectedLayer {
      +weights: float[][]
      +forward(input)
    }
    class CNN {
      +convLayers: ConvolutionalLayer[]
      +poolLayers: PoolingLayer[]
      +fcLayers: FullyConnectedLayer[]
      +train()
      +predict()
    }
    class Evaluator {
      +calculateAccuracy()
      +calculateLoss()
    }
    Dataset --> Preprocessor : "prepara"
    Preprocessor --> CNN : "treina"
    CNN --> ConvolutionalLayer : "compõe"
    CNN --> PoolingLayer : "compõe"
    CNN --> FullyConnectedLayer : "compõe"
    CNN --> Evaluator : "avalia"
```

---

### 9. Redes Neurais Recorrentes com LSTM (Muito Avançado)
**Contexto:** Processamento de sequências temporais ou texto, capturando dependências de longo prazo.

```mermaid
classDiagram
    class Dataset {
      +loadSequences()
      +splitData()
    }
    class Preprocessor {
      +tokenize()
      +normalizeData()
    }
    class LSTMLayer {
      +cells: LSTMCell[]
      +forward(sequence)
    }
    class LSTMCell {
      +inputGate()
      +forgetGate()
      +outputGate()
    }
    class RNN {
      +lstmLayers: LSTMLayer[]
      +train()
      +predict()
    }
    class Evaluator {
      +calculatePerplexity()
      +calculateMAE()
    }
    Dataset --> Preprocessor : "prepara"
    Preprocessor --> RNN : "treina"
    RNN --> LSTMLayer : "compõe"
    LSTMLayer --> LSTMCell : "contém"
    RNN --> Evaluator : "avalia"
```

---

### 10. Aprendizado por Reforço (Reinforcement Learning) (Avançado)
**Contexto:** Treinamento de um agente para aprender estratégias em um ambiente simulado, como jogos ou robótica.

```mermaid
classDiagram
    class Environment {
      +state: State
      +step(action)
      +reset()
    }
    class Agent {
      +policy: Policy
      +learn()
      +act(state)
    }
    class Policy {
      +selectAction(state)
      +update()
    }
    class RewardFunction {
      +calculateReward(state, action)
    }
    class Evaluator {
      +evaluatePerformance()
    }
    Agent --> Policy : "utiliza"
    Environment --> RewardFunction : "usa"
    Agent --> Evaluator : "avalia"
```

---

Cada diagrama de classe acima representa, de forma simplificada, os componentes principais e as relações existentes no fluxo de trabalho ou na estrutura interna dos algoritmos de aprendizado de máquina, permitindo visualizar como os dados, o pré-processamento, o treinamento e a avaliação se interconectam em cada cenário. Esses modelos podem ser expandidos ou adaptados conforme as necessidades específicas de uma implementação real.